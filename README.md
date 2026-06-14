# Thunder Hackathon 2.0 - Build Your Own JavaScript

## Overview

This project is a Python-based JavaScript Runtime that accepts JavaScript code as input, executes it through a JavaScript execution engine, and prints the output to the console.

The goal of this project is to provide a lightweight runtime environment capable of executing JavaScript programs while keeping Python as the primary implementation language.

---

## Features

* Execute JavaScript code from input
* Supports variables (`let`, `const`)
* Supports conditionals (`if`, `else if`, `else`)
* Supports loops (`for`, `while`, `do...while`)
* Supports functions and callbacks
* Supports arrays and common array methods
* Supports objects
* Supports string operations
* Supports the `Math` object
* Supports the `Date` object
* Supports spread and rest operators
* Captures and displays program output
* Error reporting for invalid JavaScript code

---

## Project Structure

```text
.
├── runtime.py
├── README.md
└── testcases/
    ├── tc1.js
    ├── tc2.js
    ├── tc3.js
    ├── tc4.js
    └── tc5.js
```

---

## Requirements

* Python 3.8+
* Node.js

---

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd thunder-hackathon-js-runtime
```

2. Ensure Python and Node.js are installed

```bash
python3 --version
node -v
```

---

## Running the Runtime

### Execute a JavaScript file

```bash
python3 runtime.py program.js
```

### Example

Input (program.js):

```javascript
let num = 7;

if (num % 2 === 0) {
    console.log(num + " is Even");
} else {
    console.log(num + " is Odd");
}
```

Output:

```text
7 is Odd
```

---

## Test Cases

The runtime has been tested against:

* Odd/Even Checker
* Triangle Pattern
* Armstrong Number
* Array Reverse
* String Palindrome Check

---

## Design

The runtime follows a simple execution pipeline:

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

## Author

Akshay Vijayvargiya

Thunder Hackathon 2.0 Submission

