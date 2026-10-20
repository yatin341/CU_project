
# 🏙️ Chandigarh Civic Services Portal

### AI-Powered Access to Public Services, Healthcare & Citizen Support

A web-based civic services platform designed to help citizens in Chandigarh discover public services, understand government schemes, validate documents, and access healthcare information through a single interface.

The project aims to make essential services easier to discover and navigate through AI-assisted guidance, document validation, and a centralized citizen experience.

## ✨ Key Features

### 🤖 AI Civic Assistant
- Conversational assistance for citizen queries.
- Helps users understand public services and application requirements.
- Provides easy-to-understand responses.
- Designed to guide users toward relevant official information.

### 🔎 Public Service Discovery
- Search for relevant government services.
- Access service information and documentation requirements.
- Support for Chandigarh-specific services and selected central government services.
- Helps citizens find the appropriate official portal.

### 📄 Document Validation
- Document-processing workflow using OCR technology.
- Extracts text from supported uploaded documents.
- Supports preliminary document checks.
- Helps identify potential missing information before an application is submitted.

> Document checks are intended to assist users and should not be treated as official government verification.

### 🏥 Healthcare Services
- Access information about approved hospitals listed in the application.
- Search hospital information.
- Support for appointment-related workflows.

### 👤 User Authentication
- User registration and login.
- Session-based authentication.
- Password hashing for account security.
- Guest access, where enabled.

### 📊 Citizen Dashboard
- Centralized interface for accessing available services.
- Convenient navigation between service discovery, healthcare, and AI assistance.
- Designed to simplify the citizen's digital-service journey.

## 🎯 Problem Statement

Citizens often struggle to find accurate information about government services, eligibility requirements, supporting documents, and application procedures. Information can be distributed across multiple websites, making the process confusing and time-consuming.

This project addresses that challenge by bringing service discovery, AI assistance, document checks, and healthcare-related features together in one web application.

## 💡 Our Solution

The Chandigarh Civic Services Portal provides a unified digital experience that helps users:

1. Discover relevant public services.
2. Understand application and documentation requirements.
3. Check uploaded documents for potential issues.
4. Find listed healthcare facilities and access appointment features.
5. Navigate public-service information with AI-assisted guidance.

The goal is to make digital public services more accessible, understandable, and convenient.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Flask | Web application and backend routing |
| MySQL | Relational database |
| HTML, CSS & JavaScript | Web interface |
| Groq API | AI-assisted responses, where configured |
| OCR / Tesseract | Document text extraction, where configured |
| Python-dotenv | Environment-variable configuration |
| Werkzeug Security | Password hashing and verification |

*The listed technologies reflect the intended project architecture; confirm them against the current source code before treating this list as final.*

## 📁 Project Structure

```text
chandigarh/
├── app.py
├── ai_assistant.py
├── benefits.py
├── health_care.py
├── ocr_validator.py
├── db.py
├── documents.py
├── templates/
├── static/
├── requirements.txt
├── .env.example
└── README.md
```

Some filenames and directories may differ in your repository. Keep the structure in this README synchronized with the actual project files.

## ⚙️ Getting Started

### Prerequisites

Install the following before running the application:

- Python 3.11
- MySQL Server
- Git
- Tesseract OCR, if required by the document-validation module

### 1. Clone the Repository

```bash
git clone https://github.com/yatin341/CU_project.git
cd CU_project/chandigarh
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the virtual environment's Python executable directly instead.

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the directory expected by the application.

Example configuration:

```env
SECRET_KEY=replace_with_a_secure_random_value

DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name

GROQ_API_KEY=your_groq_api_key
```

Use the exact environment-variable names expected by your source code. Additional settings may be required for other integrations.

**Security:** Never commit `.env`, database passwords, API keys, or other secrets to GitHub. Store production secrets in your hosting provider's environment settings.

### 5. Set Up the Database

1. Start your MySQL server.
2. Create the database configured in your `.env` file.
3. Configure the database credentials.
4. Run the initialization or migration process provided by the project.

Use the database initialization command defined by your application rather than assuming a particular command.

### 6. Start the Application

If the Flask application exposes `app` from `app.py`, run:

```bash
flask --app app run --debug
```

Open the local address shown in the terminal, usually:

http://127.0.0.1:5000

Use debug mode for local development only, not for production deployment.

## 🌐 Deployment

The application can be prepared for deployment on a suitable Python hosting platform, such as Render.

A production deployment generally requires:

1. A valid Python build environment.
2. All required Python dependencies.
3. Production environment variables.
4. A reachable MySQL database.
5. OCR system packages, if document processing depends on Tesseract.
6. A production WSGI server such as Gunicorn.
7. Correct configuration for uploaded files and persistent storage.

Deployment commands and database settings should match the repository's actual configuration.

## 🔐 Security & Privacy

- Keep API keys and database credentials in environment variables.
- Use secure password hashing.
- Validate uploaded files and restrict upload sizes.
- Apply appropriate authentication and authorization checks.
- Avoid exposing personal or sensitive information in logs.
- Use HTTPS in production.
- Verify government-service information against official sources.
- Do not treat AI-generated guidance or OCR output as an official decision.

## 🚀 Future Improvements

- Multilingual AI assistance.
- More comprehensive government-service discovery.
- Improved document-quality and completeness checks.
- Application-status tracking through authorized integrations.
- Notifications for relevant application updates.
- Accessibility improvements for users with different needs.
- Integration with verified government APIs where access is available.
- Expanded healthcare search and appointment management.
- Better automated testing and monitoring.

## 🎯 Project Goals

- Simplify access to public services.
- Reduce confusion around documentation requirements.
- Improve discoverability of relevant information.
- Make citizen-facing digital services easier to use.
- Explore responsible AI integration in public-service workflows.

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make and test your changes.
4. Submit a pull request describing the improvements.

## ⚠️ Disclaimer

This is a software project intended to assist users in navigating public-service information. It is not an official Chandigarh Administration website unless formally authorized. Service availability, eligibility, documentation requirements, and application decisions must be confirmed with the relevant official authority.

## 👨‍💻 Author

**GitHub:** [@yatin341](https://github.com/yatin341)

## 📄 License

Add a license to the repository if you intend to publish the project for reuse. Until a license is specified, do not assume that others have permission to redistribute or modify the code.
