# Verification

Executed on 10 October 2026 with Python 3.12 on Windows:

- Dependencies installed successfully in an isolated environment.
- Five unittest smoke tests passed: public pages and CSS paths, login-required routes, authenticated pages with an empty mocked database, invalid signup validation, and the database initialization command with a mocked connection.
- CSS paths checked with exact filename case to catch Linux deployment issues.

Not executed here:

- Docker image build or Compose startup (Docker unavailable).
- Real MySQL schema execution, signup/login persistence, or database migrations.
- Tesseract image/PDF OCR or Groq API calls.
- Live Railway deployment, visual browser review, load testing or a production security audit.

Run `python -m unittest -v test_smoke` after installing requirements to repeat the smoke tests. Run the Docker setup in README.md, then verify real signup, login, file upload/download, hospital approval and appointment requests before sharing a public deployment.
