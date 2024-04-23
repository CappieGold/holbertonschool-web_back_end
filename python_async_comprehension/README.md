# Python - Async Comprehension

## Learning Objectives
- of this project, you are expected to be able to `explain to anyone`, without the help of Google:
  - How to write an asynchronous generator
  - How to use async comprehensions
  - How to type-annotate generators

### 1. Writing an Asynchronous Generator
- Asynchronous generators are similar to regular generators but are designed to work with asynchronous operations. They allow you to yield values in an asynchronous function, using the `async` and `await` syntaxes.
```bash
import asyncio

async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)
        yield i

# Usage
async def main():
    async for value in async_generator():
        print(value)

asyncio.run(main())
```

### 2. Using Async Comprehensions
- Async comprehensions provide a way to write asynchronous loops for creating collections (like lists, sets, dicts) in a more concise and readable way. You can use them with any object that supports asynchronous iteration, such as asynchronous generators.

#### Example of an async list comprehension:
```bash
import asyncio

async def fetch_data(x):
    await asyncio.sleep(1)
    return x * 2

async def use_async_comprehension():
    # Use async comprehension to build a list
    result = [await fetch_data(i) for i in range(5)]
    print(result)

asyncio.run(use_async_comprehension())
```

### 3. Type-Annotating Generators
- In Python, you can type-annotate generators to specify what types of values they yield, what type they receive from `send()`, and what type they return when the iteration ends.

#### Generator Syntax: Generator[YieldType, SendType, ReturnType]
- For an asynchronous generator, the syntax is a bit different as you only need to specify the type of values it yields because async generators cannot receive values via `send()` nor can they return a value other than `None` at the end.

#### Async Generator Syntax: AsyncGenerator[YieldType, None]
- Here's how to annotate an asynchronous generator:
```bash
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[int, None]:
    for i in range(3):
        await asyncio.sleep(1)
        yield i

async def main():
    async for value in async_generator():
        print(value)

asyncio.run(main())
```

These tools and techniques allow you to manage asynchronous code more effectively, making it easier to perform tasks that involve waiting for I/O operations without blocking the entire program's execution. The type annotations help improve code clarity and assist tools and other developers in understanding what the code is supposed to do.
