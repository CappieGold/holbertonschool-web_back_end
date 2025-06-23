# User Authentication Service

## Background Context
In this project, you will implement a user authentication service using Flask and SQLAlchemy. You will learn how to build secure authentication mechanisms including password hashing, session management, and user registration/login workflows.

## Resources
Read or watch:

- [Flask documentation](https://flask.palletsprojects.com/)
- [Requests module](https://docs.python-requests.org/en/latest/)
- [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- You should use SQLAlchemy
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)
- All your functions should be type annotated
- The flask app should only interact with Auth and never with DB directly
- Only public methods of Auth and DB should be used outside these classes

## Setup

You will need to install bcrypt:

```bash
pip3 install bcrypt
```

## Installation

```bash
# Clone the repository
git clone https://github.com/CappieGold/holbertonschool-web_back_end.git
cd user_authentication_service

# Install dependencies
pip3 install -r requirements.txt
```

## Usage

```bash
# Run the Flask application
python3 app.py
```

## Project Structure

```
user_authentication_service/
├── app.py                 # Flask application
├── auth.py               # Authentication logic
├── db.py                 # Database operations
├── user.py               # User model
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Features

- User registration with email validation
- Secure password hashing using bcrypt
- Session management with cookies
- Password reset functionality
- User profile management
- Type annotations throughout the codebase
- Comprehensive error handling

## Code Style

This project follows the `pycodestyle` guidelines. To check your code:

```bash
pycodestyle *.py
```

## Database

The project uses SQLAlchemy ORM with SQLite database. The database schema includes:

- User table with fields: id, email, hashed_password, session_id, reset_token

## Security Features

- Password hashing with bcrypt
- Session-based authentication
- Secure cookie handling
- Input validation and sanitization

## Author

Carpentier Jérémy: [CappieGold](https://github.com/CappieGold)
