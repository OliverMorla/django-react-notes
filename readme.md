# django-react-notes

## Overview
Django-React-Notes is a full-stack application designed to streamline the process of note-taking. It allows users to create, view, update, and delete notes efficiently. The backend is powered by Django REST Framework and PostgreSQL, ensuring robust and scalable data handling. The frontend is built with React, Next.js, TypeScript, and Tailwind CSS, offering a responsive and user-friendly interface.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

## Features
- Create new notes
- View a list of all notes
- Update existing notes
- Delete notes

## Technologies
- **Backend:** Django REST Framework, PostgreSQL
- **Frontend:** React, Next.js, TypeScript, Tailwind CSS

## Installation

### Prerequisites
- Python 3.x
- Node.js
- PostgreSQL

### Backend Setup
```bash
git clone https://github.com/OliverMorla/django-react-notes.git
cd django-react-notes/backend

# Setup virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup and run PostgreSQL database
# [Add PostgreSQL setup instructions]

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

### Frontend Setup
```bash
cd django-react-notes/frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

## Usage
After installing both the backend and frontend:

1. Navigate to `http://localhost:3000` to access the frontend.
2. Use the application to create, view, update, and delete notes.

## Contributing
Contributions to Django-React-Notes are welcome! Please follow these steps to contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add a feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## Contact
For any questions or concerns, please reach out to Oliver Morla at olivermiguel1129@gmail.com.
