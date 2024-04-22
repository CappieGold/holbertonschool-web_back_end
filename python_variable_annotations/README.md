# Python - Variable Annotations

## Learning Objectives
- At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
  - Type annotations in Python 3
  - How you can use type annotations to specify function signatures and variable types
  - Duck typing
  - How to validate your code with mypy

Type annotations in Python 3 provide a way to explicitly define the types of variables, function parameters, and return values. They help with code clarity and can also assist in catching certain types of errors before runtime. Here's a breakdown of how you can utilize type annotations along with some insights into duck typing and code validation using mypy.

### Using Type Annotations
- Type annotations allow developers to specify what type of data each part of their code is supposed to handle.

#### 1. Basic Annotations:
```bash
age: int = 24
name: str = "Alice"
```

#### 2. Function Annotations:
- You can annotate the arguments and the return type of functions.
```bash
def greet(name: str) -> str:
    return f"Hello, {name}"
```

### Duck Typing
- Python is known for its use of duck typing, a type of dynamic typing where the type or class of an object is less important than the methods it defines. Using Python, if an object performs a required behavior (methods or properties), it can be used as an argument for a function, regardless of its type.
```bash
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm mimicking a duck!"

def make_it_quack(duck: Duck):
    print(duck.quack())

duck = Duck()
person = Person()
make_it_quack(duck)  # Outputs: Quack!
make_it_quack(person)  # Outputs: I'm mimicking a duck!
```

### Validating Code with Mypy
- Mypy is a static type checker for Python. You can use it to ensure that your type annotations are correct.

#### Installation:
```bash
pip install mypy
```

#### Usage:
- To check a file for type consistency, run:
```bash
mypy your_script.py
```

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`, `VsCode`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
