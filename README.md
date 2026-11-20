# 🔢 Simple Python CLI Calculator

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg)](#)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)](https://github.com/harshita152/simple-calculator/pulls)

A lightweight, terminal-based calculator written in Python. It provides a clean, modular foundation for executing standard arithmetic operations directly from the command line.

---

## 📌 Features

- **Core Arithmetic**: Supports Addition (`+`), Subtraction (`-`), Multiplication (`*`), and Division (`/`).
- **Modular Design**: Arithmetic operations are isolated into reusable, standalone functions.
- **Zero External Dependencies**: Runs entirely on native Python without installing any third-party libraries.
- **Interactive Terminal Interface**: Simple, guided user prompt for operand and operator input.

---

## 📂 Project Structure

```text
simple-calculator/
├── calculator.py   # Main script with arithmetic functions & CLI driver
└── README.md       # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

* [Python 3.8+](https://www.python.org/downloads/) installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/harshita152/simple-calculator.git
   cd simple-calculator
   ```

2. **Run the calculator:**
   ```bash
   python calculator.py
   ```

---

## 💻 Usage Example

When you run the script, enter two numbers and choose your operation (`+`, `-`, `*`, or `/`):

```text
enter a number: 12
enter a number: 4
choose opertation : *
12*4=48
```

Another example (division):
```text
enter a number: 20
enter a number: 5
choose opertation : /
20/5=4.0
```

---

## 🧩 Code Architecture & API

The arithmetic logic can be imported and reused as a module in other Python scripts:

```python
from calculator import add, subtract, multiply, divide

print(add(10, 5))        # 15
print(subtract(10, 5))   # 5
print(multiply(10, 5))   # 50
print(divide(10, 5))     # 2.0
```

| Function | Operation | Example | Output |
| :--- | :--- | :--- | :--- |
| `add(x, y)` | Addition ($x + y$) | `add(7, 3)` | `10` |
| `subtract(x, y)` | Subtraction ($x - y$) | `subtract(7, 3)` | `4` |
| `multiply(x, y)` | Multiplication ($x \times y$) | `multiply(7, 3)` | `21` |
| `divide(x, y)` | Division ($x \div y$) | `divide(7, 2)` | `3.5` |

---

## 🗺️ Roadmap & Improvements

- [ ] **ZeroDivisionError Protection**: Handle division by zero gracefully.
- [ ] **Float Input Support**: Support decimal inputs (`float(input())`) alongside integers.
- [ ] **Continuous Calculation Loop**: Allow multiple calculations in one session with an `exit` option.
- [ ] **Advanced Operations**: Add modulus (`%`), exponentiation (`**`), and square root (`math.sqrt`).
- [ ] **Graphical User Interface (GUI)**: Build a desktop UI using `tkinter` or `PyQt`.

---

## 🤝 Contributing

Contributions are welcome! If you want to enhance the calculator:

1. Fork the Project
2. Create a Feature Branch (`git checkout -b feature/AddExponentiation`)
3. Commit your Changes (`git commit -m 'feat: add exponentiation operation'`)
4. Push to the Branch (`git push origin feature/AddExponentiation`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
