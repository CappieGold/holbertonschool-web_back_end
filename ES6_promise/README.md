# ES6 Promises

## Learning Objectives
At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- Promises (how, why, and what)
- How to use the `then`, `resolve`, `catch` methods
- How to use every method of the Promise object
- Throw / Try
- The await operator
- How to use an `async` function

### Promises: How, Why, and What

#### What:
A `Promise` is an object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value. It allows you to associate handlers with an asynchronous action's eventual success value or failure reason. This lets asynchronous methods return values like synchronous methods: instead of immediately returning the final value, the asynchronous method returns a promise to supply the value at some point in the future.

#### Why:
Promises are used to handle asynchronous operations in JavaScript, allowing better code management and avoiding the callback hell (deeply nested callbacks). They provide a cleaner and more robust way to handle asynchronous logic compared to traditional callback-based approaches.

#### How:
A Promise has three states:
- `Pending`: initial state, neither fulfilled nor rejected.
- `Fulfilled`: the operation completed successfully.
- `Rejected`: the operation failed.

### Using then, resolve, catch Methods

#### then():
Adds fulfillment and rejection handlers to the promise, and returns a new promise resolving to the return value of the called handler.
```bash
let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("Done!"), 1000);
});

promise.then(
    result => console.log(result), // shows "Done!" after 1 second
    error => console.log(error) // doesn't run
);
```

#### catch():
Is used for error handling in promise compositions. It's syntactic sugar for `then(undefined, rejection)`.
```bash
new Promise((resolve, reject) => {
    throw new Error("Error!");
}).catch(alert); // shows "Error: Error!" in an alert box
```

#### resolve():
A method of the Promise object that returns a Promise object that is resolved with a given value.
```bash
const resolvedPromise = Promise.resolve(123);
resolvedPromise.then(console.log); // logs 123
```

### Methods of the Promise Object
- `Promise.all([promisesArray])`: Waits for all promises to resolve or for any to reject. It returns a promise that resolves when all of the promises in the iterable argument have resolved, or rejects with the reason of the first passed promise that rejects.
- `Promise.race([promisesArray])`: Returns a promise that resolves or rejects as soon as one of the promises in the iterable resolves or rejects, with the value or reason from that promise.
- `Promise.allSettled([promisesArray])`: Returns a promise that resolves after all of the given promises have either resolved or rejected, with an array of objects that each describe the outcome of each promise.
- `Promise.any([promisesArray])`: Returns a promise that fulfills as soon as any of the promises in the iterable fulfills, with the value of the fulfilled promise.

### Throw / Try

#### try/catch:
The `try` statement lets you test a block of code for errors, and the catch statement lets you handle the error.
```bash
try {
  // Code to try
  throw new Error("An error occurred!");
} catch (e) {
  // Code to run if an error occurs
  console.log(e.message);
}
```

### The await Operator

#### await:
The `await` expression causes async function execution to pause until a Promise is settled (either resolved or rejected), and to resume execution of the async function after fulfillment. When resumed, the value of the `await` expression is that of the resolved Promise.
```bash
async function fetchData() {
  let response = await fetch('https://api.example.com/data');
  let data = await response.json();
  return data;
}
```

### Async Function

#### async function:
Declares a function that handles asynchronous operations using `await`.
```bash
async function loadData() {
  try {
    const data = await fetchData();
    console.log(data);
  } catch (error) {
    console.error("Failed to fetch data:", error);
  }
}
```

### Conclusion
Promises and the async/await syntax are powerful tools in JavaScript for managing asynchronous operations. They provide clear, concise, and robust code for handling operations that depend on external data sources, timers, or other asynchronous actions.
