# ES6 Basics

## Learning Objectives
At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- What ES6 is
- New features introduced in ES6
- The difference between a constant and a variable
- Block-scoped variables
- Arrow functions and function parameters default to them
- Rest and spread function parameters
- String templating in ES6
- Object creation and their properties in ES6
- Iterators and for-of loops

### 1. What ES6 is
ES6, or ECMAScript 2015, is the sixth edition of the ECMAScript language specification. It provides major enhancements over ES5, including syntactic sugar that makes the language more readable and maintainable, and new features that extend its processing capability.

### 2. New Features Introduced in ES6
Some of the most impactful features introduced in ES6 include:
- `Let and Const for variable declarations`
- `Arrow functions`
- `Template literals`
- `Destructuring assignment`
- `Default function parameters`
- `Rest and Spread operators`
- `Enhanced object literals`
- `Promises for asynchronous programming`
- `Modules`
- `Classes`
- `Iterators and Generators`
- `For-of loop`

### 3. The Difference Between a Constant and a Variable
- `Variables` (declared with `let`) can have their values changed over time. They are mutable and provide block scope.
- `Constants` (declared with `const`) must be initialized at the time of declaration and cannot be reassigned. Like `let`, `const` also provides block scope but is used to declare values meant to remain constant through their lifetime.

### 4. Block-Scoped Variables
`let` and `const` are both block-scoped. This means they are only accessible within the block (`{}`) where they were declared. This is different from `var`, which is function-scoped.

### 5. Arrow Functions and Function Parameters Default to Them
Arrow functions provide a more concise syntax for writing functions. They also do not have their own `this` context, instead inheriting it from the enclosing execution context. An example of using default parameters with arrow functions:
```bash
const greet = (name = 'Guest') => `Hello, ${name}!`;
```

### 6. Rest and Spread Function Parameters
- `Rest parameters` (`...args`) allow you to handle function parameters as a single array.
- `Spread operator` (`...`) allows an iterable such as an array or string to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected.

### 7. String Templating in ES6
Template literals use backticks (\`\`\`\`) instead of quotes to define strings. They can contain placeholders (`${expression}`) for embedding expressions directly within the string.
```bash
const name = "world";
console.log(`Hello, ${name}!`);
```

### 8. Object Creation and Their Properties in ES6
ES6 introduced enhanced object literals that make it easier to quickly define objects with properties, including dynamic property names, computed properties, and method shorthand.
```bash
const propertyName = "status";
const obj = {
  [propertyName]: "active",
  sayStatus() {
    return this.status;
  }
};
```

### 9. Iterators and For-Of Loops
- `Iterators` are objects that know how to access items from a collection one at a time, while keeping track of their current position.
- `For-of loop` is used to loop over iterable objects (like arrays, strings, etc.) directly:
```bash
const array = [10, 20, 30];
for (const value of array) {
  console.log(value);
}
```

These enhancements not only make JavaScript more powerful but also improve the clarity and quality of code, promoting best practices in coding.

## Setup

### Install NodeJS 12.11.x
(in your home directory):
```bash
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```
```bash
$ nodejs -v
v12.11.1
$ npm -v
6.11.3
```

### Install Jest, Babel, and ESLint
in your project directory:
- Install Jest using: `npm install --save-dev jest`
- Install Babel using: `npm install --save-dev babel-jest @babel/core @babel/preset-env`
- Install ESLint using: `npm install --save-dev eslint`

## Configuration files
Please create the following 3 files (with the provided contents) in the project directory:

### package.json
```bash
{
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "dev": "npx babel-node",
    "test": "jest",
    "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
  },
  "devDependencies": {
    "@babel/core": "^7.6.0",
    "@babel/node": "^7.8.0",
    "@babel/preset-env": "^7.6.0",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "jest": "^24.9.0"
  }
}
```

### babel.config.js
```bash
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};
```

### .eslintrc.js
```bash
module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  },
  overrides:[
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    }
  ]
};
```

### Finally…
Don’t forget to run `npm install` from the terminal of your project folder to install all necessary project dependencies.
