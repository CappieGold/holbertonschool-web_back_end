# Python - Async

## Learning Objectives
- At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
  - `async` and `await` syntax
  - How to execute an async program with `asyncio`
  - How to run concurrent coroutines
  - How to create `asyncio` tasks
  - How to use the `random` module

- Let's delve into using async and await with asyncio in Python, including how to manage concurrency with tasks, and a touch on using the random module within an asynchronous context:
### Async and Await Syntax
#### async
- is a keyword used to declare a function as a coroutine, which can be paused and resumed.
#### await
- is used to pause the execution of a coroutine until a given asynchronous operation completes. It can only be used inside async functions.

### Executing an Async Program with Asyncio
- To run an async program, you need to set up an event loop which handles all the operations:
```bash
import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(main())
```

### Running Concurrent Coroutines
- You can run coroutines concurrently using `asyncio.gather()` or by creating tasks:
```bash
async def main():
    await asyncio.gather(
        coroutine1(),
        coroutine2(),
        coroutine3()
    )

# or using tasks

async def main():
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())
    await asyncio.gather(task1, task2)
```

### Creating Asyncio Tasks
- Tasks are used to schedule coroutines concurrently:
```bash
async def my_task():
    await asyncio.sleep(1)
    return "Completed"

async def main():
    task = asyncio.create_task(my_task())
    result = await task
    print(result)

asyncio.run(main())
```

### Using the Random Module in Async Functions
- While the `random` module is not asynchronous, you can still use it in your asynchronous functions just like any regular Python function:
```bash
import asyncio
import random

async def display_random_int():
    await asyncio.sleep(1)
    print(random.randint(1, 100))

async def main():
    await display_random_int()

asyncio.run(main())
```
This setup will print a random integer after a delay of 1 second. Remember that using blocking operations like intensive computations or blocking I/O directly inside an async function can negate the benefits of asynchronous programming, but `random.randint()` does not block and is fast, so it’s fine to use in this context.
