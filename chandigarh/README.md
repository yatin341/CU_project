# CivicLoop Chandigarh

## Run on your computer

Install Python 3.12 and Docker Desktop (with Linux containers), then open a terminal in this folder:

```sh
python setup.py
docker compose up --build -d
```

Open http://localhost:8080. MySQL tables are created automatically. Register your own account. The database starts empty; no real hospital listings or appointments have been invented. Files and database records persist in Docker volumes. Stop with `docker compose down`; do not add `-v` unless you intend to erase those volumes.

To enable general AI chat and AI document classification, set your own `GROQ_API_KEY` in `.env`, then run `docker compose up -d --force-recreate web`. Catalogue answers and local image OCR do not require an AI key. OCR uses Tesseract, installed by the Dockerfile; PDF validation accepts up to 20 pages. AI document analysis sends extracted text to Groq, with Aadhaar-like numbers masked; other personal details may remain in that text.

## Hospital verification

Submitted hospitals remain pending until the server operator verifies them. Run:

```sh
docker compose exec web flask --app app list-hospitals
docker compose exec web flask --app app approve-hospital 1
```

Replace `1` with the verified hospital's ID. Appointment submissions are requests recorded in this app; there is no hospital booking-system integration.

## Deploy to Railway

1. Create a Railway project and add a MySQL service. Upload this folder to your own GitHub repository and add a Railway service from that repository. The included Dockerfile is the build configuration.
2. Set `SECRET_KEY` to a new long random value in the web service variables. Set `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME` using reference variables from the MySQL service (`MYSQLHOST`, `MYSQLPORT`, `MYSQLUSER`, `MYSQLPASSWORD`, `MYSQLDATABASE`). Do not upload `.env` or reuse its local database credentials.
3. Set `COOKIE_SECURE=true`, `UPLOAD_ROOT=/app/uploads`, and optionally `GROQ_API_KEY`. Let Railway provide `PORT`.
4. Attach a persistent volume to the web service at `/app/uploads` before accepting uploads. Keep the MySQL service's data volume.
5. Deploy and generate a public domain. Startup creates missing tables, then starts Gunicorn. `/healthz` is a process health check, not a database readiness check. Verify signup, login, hospital submissions and document uploads on the deployed service.
6. Use the service shell to run `flask --app app list-hospitals` and `flask --app app approve-hospital ID` after reviewing submissions.

Railway requires your account and may charge for hosting. No hosting account or live deployment is included in this ZIP.

## Changes and limitations

- Added MySQL schema, initialization and hospital approval commands, Docker Compose, Dockerfile, Railway configuration and generated local secrets.
- Fixed the guest page, Linux CSS path case, environment-variable precedence and upload locations.
- Replaced the incomplete PaddleOCR setup with Tesseract and PDF rendering; added missing dependencies.
- Preserved the original service catalogue as supplied; its government-service information has not been independently verified.
- The original archive's `.env`, Git history and cached bytecode are excluded.

See `VERIFICATION.md` for executed checks and remaining verification. This is a deployment preparation package, not a completed production security audit.
