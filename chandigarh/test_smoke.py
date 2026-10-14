"""Run with python -m unittest -v test_smoke (no live database needed)."""
import os
import re
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

os.environ.setdefault('SECRET_KEY', 'test-only-do-not-deploy')
from app import app

class SmokeTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_public_pages_and_css(self):
        for path in ['/', '/guest', '/login', '/signup', '/health/', '/health/emergency', '/healthz']:
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200, path)
            for link in re.findall(r'href="(/static/[^\"]+)"', response.text):
                with self.client.get(link) as asset:
                    self.assertEqual(asset.status_code, 200, link)
                # Explicit case-sensitive component check, including on Windows.
                current = Path(__file__).parent
                for part in link.lstrip('/').split('/'):
                    self.assertIn(part, [p.name for p in current.iterdir()])
                    current /= part

    def test_protected_pages(self):
        for path in ['/dashboard', '/documents/', '/documents/files', '/health/add', '/health/my-appointments']:
            self.assertEqual(self.client.get(path).status_code, 302, path)
        self.assertEqual(self.client.post('/ai/chat', json={'message':'hello'}).status_code, 401)

    def test_authenticated_pages_with_empty_database(self):
        conn = MagicMock()
        conn.cursor.return_value.fetchall.return_value = []
        with self.client.session_transaction() as session:
            session['user_id'] = 1
            session['user_name'] = 'Test'
        with patch('health_care.get_connection', return_value=conn), patch('documents.get_connection', return_value=conn):
            for path in ['/dashboard','/health/find','/health/add','/health/appointment','/health/my-hospitals','/health/my-appointments','/documents/','/documents/files','/documents/upload','/documents/scan','/documents/ocr','/documents/reader','/ai/']:
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200, path)

    def test_invalid_signup(self):
        with patch('app.get_connection') as database:
            self.assertEqual(self.client.post('/signup', data={'email':'bad'}).status_code,200)
            database.assert_not_called()

    def test_sql_initialization(self):
        conn = MagicMock()
        with patch('manage.get_connection',return_value=conn):
            result=app.test_cli_runner().invoke(args=['init-db'])
            self.assertEqual(result.exit_code,0,result.output)
            self.assertEqual(conn.cursor.return_value.__enter__.return_value.execute.call_count,4)

if __name__ == '__main__':
    unittest.main()
