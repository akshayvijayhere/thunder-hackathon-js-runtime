# Thunder Hackathon 2.0 – Build Your Own JavaScript

## Overview

This project is a Python-based JavaScript Runtime that accepts JavaScript code as input, executes it, and displays the output.

The runtime is designed to provide a simple execution environment for JavaScript programs while using Python as the primary implementation language.

---

## Features

* Execute JavaScript code
* Supports variables (`let`, `const`)
* Supports conditionals (`if`, `else if`, `else`)
* Supports loops (`for`, `while`, `do...while`)
* Supports functions and callbacks
* Supports arrays and objects
* Supports string operations
* Supports Math operations
* Supports Date operations
* Supports spread and rest operators
* Displays execution output
* Handles JavaScript runtime errors

---

## Requirements

* Python 3.x
* Node.js

Check installation:

```bash
python3 --version
node -v
```

---

## How to Run

Start the runtime:

```bash
python3 runtime.py
```

Paste your JavaScript code.

Type:

```text
RUN
```

on a new line to execute the program.

---

## Example

Input:

```javascript
let num = 7;

if (num % 2 === 0) {
    console.log(num + " is Even");
} else {
    console.log(num + " is Odd");
}

RUN
```

Output:

```text
7 is Odd
```

---

## Architecture

```text
JavaScript Source Code
          ↓
Python Runtime
          ↓
JavaScript Execution Engine
          ↓
Output Capture
          ↓
Console Output
```

---

## Tested Concepts

* Variables
* Operators
* Conditional Statements
* Loops
* Functions
* Arrays
* Strings
* Objects
* Math Operations

---

## Author

Akshay Vijayvargiya

Submission for Thunder Hackathon 2.0


