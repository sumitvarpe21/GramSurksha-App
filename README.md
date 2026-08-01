# GramSurksha - Real-Time Civic Issue Reporting System

GramSurksha is a Django-based web application developed to simplify the reporting of civic issues. The platform allows citizens to report public problems such as road damage, garbage collection, water leakage, street light failures, accidents, and other civic concerns by uploading issue details along with supporting images.

The application provides a centralized system where citizens can submit complaints while administrators can review and manage reported issues efficiently.

---

# Problem Statement

Citizens often face difficulties in reporting civic issues to the appropriate authorities. Traditional complaint systems are time-consuming and lack transparency.

GramSurksha provides a simple digital platform that enables citizens to report issues online, upload supporting images, and monitor the progress of their complaints.

---

# Features

- User Registration
- Secure Login & Logout
- Report Civic Issues
- Upload Images with Complaints
- Multiple Issue Categories
- View Submitted Complaints
- Admin Dashboard
- Manage Reported Issues
- Responsive User Interface

---

# Technology Stack

## Backend
- Python
- Django

## Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

## Database
- SQLite

---

# Project Structure

```
GramSurksha-App
│
├── gram_suraksha/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── report_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   └── migrations/
│
├── templates/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

# Modules

## User Module

- User Registration
- Login & Logout
- User Authentication

---

## Issue Module

Users can

- Report New Issues
- Upload Supporting Images
- Select Issue Categories
- View Submitted Complaints

---

## Admin Module

Administrator can

- View Reported Issues
- Manage User Complaints
- Update Complaint Details
- Delete Invalid Reports

---

# Supported Issue Categories

- Road Damage
- Garbage Collection
- Water Leakage
- Street Light Failure
- Animal Threat
- Accident
- Crime
- Other Civic Issues

---

# System Workflow

```
User
   │
   ▼
Register / Login
   │
   ▼
Report Civic Issue
   │
   ▼
Upload Image
   │
   ▼
Store in Database
   │
   ▼
Admin Reviews Complaint
   │
   ▼
Issue Managed
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/sumitvarpe21/GramSurksha-App.git
```

Navigate to project

```bash
cd GramSurksha-App
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

# Future Enhancements

- Email Notifications
- Live Location Support
- Mobile Application
- AI-Based Issue Classification
- Government Authority Dashboard
- Complaint Analytics

---

# My Contribution

- Developed the Django-based web application.
- Designed the database models using Django ORM.
- Implemented user authentication.
- Developed the issue reporting module.
- Integrated image upload functionality.
- Built the admin management features.
- Created responsive frontend pages using HTML, CSS, Bootstrap, and JavaScript.

---

# Author

**Sumit Varpe**

Information Technology Student

GitHub: https://github.com/sumitvarpe21
