# Session authentication

# Session authentication

## Background Context
In this project, you will implement a Session Authentication. You are not allowed to install any other module.

In the industry, you should not implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: Flask-HTTPAuth). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

## Resources
Read or watch:

- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY) - Only the session auth part
- [HTTP Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- [Flask](https://palletsprojects.com/p/flask/)
- [Flask Cookie](https://flask.palletsprojects.com/en/2.3.x/quickstart/#cookies)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

## Requirements

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)

## Installation

```bash
$ pip3 install -r requirements.txt
```

## Usage

```bash
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

## Project Structure

```
Session_authentication/
├── api/
│   └── v1/
│       ├── app.py
│       ├── auth/
│       │   ├── auth.py
│       │   └── session_auth.py
│       └── views/
│           ├── index.py
│           ├── users.py
│           └── session_auth.py
├── models/
│   ├── base.py
│   └── user.py
├── requirements.txt
└── README.md
```

## Features

- Session authentication
- Cookie management
- REST API for authentication
- User management
- Secured endpoints

## Main Routes

- `POST /auth_session/login`: Login with session authentication
- `DELETE /auth_session/logout`: Logout and session removal
- `GET /api/v1/users/me`: Get current user information

## Testing

To test the API, you can use `curl` or any other HTTP client:

```bash
# Login
$ curl -X POST http://0.0.0.0:5000/auth_session/login -d "email=test@test.com" -d "password=test" -c cookie.txt

# Access protected route
$ curl -X GET http://0.0.0.0:5000/api/v1/users/me -b cookie.txt

# Logout
$ curl -X DELETE http://0.0.0.0:5000/auth_session/logout -b cookie.txt
```

## Author

Carpentier Jérémy: [CappieGold](https://github.com/CappieGold)
