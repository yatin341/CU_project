from pathlib import Path
import click
from db import get_connection

def register_commands(app):
    @app.cli.command("init-db")
    def init_db():
        """Create missing tables without dropping existing data."""
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                for statement in Path(__file__).with_name("schema.sql").read_text().split(";"):
                    if statement.strip():
                        cursor.execute(statement)
            conn.commit()
        finally:
            conn.close()
        click.echo("Database tables ready.")

    @app.cli.command("list-hospitals")
    def list_hospitals():
        """List submissions for operator review."""
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, name, status FROM hospitals ORDER BY id")
                for row in cursor.fetchall():
                    click.echo(str(row))
        finally:
            conn.close()

    @app.cli.command("approve-hospital")
    @click.argument("hospital_id", type=int)
    def approve_hospital(hospital_id):
        """Approve a verified hospital by ID (server operator only)."""
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("UPDATE hospitals SET status='approved' WHERE id=%s", (hospital_id,))
                count = cursor.rowcount
            conn.commit()
        finally:
            conn.close()
        click.echo(f"Updated {count} hospital(s).")
