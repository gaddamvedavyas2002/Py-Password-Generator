# 🔐 Password Generator

A simple and interactive Python Password Generator that creates secure passwords based on user preferences. Users can choose the number of letters, numbers, and symbols to include, and the program generates a randomized password while also checking its strength.

---

## 📌 Features

* Generate random passwords
* Customize the number of:

  * Letters (A-Z, a-z)
  * Numbers (0-9)
  * Symbols (!, @, #, $, etc.)
* Input validation to prevent invalid entries
* Password strength checker
* Easy-to-understand and beginner-friendly code
* Uses Python's built-in libraries only

---

## 🛠 Technologies Used

* Python 3
* `random` module
* `string` module

---

## 📂 Project Structure

```text
password_generator.py
```

### Main Components

#### 1. `generate_password()`

Generates a random password using the specified number of letters, numbers, and symbols.

```python
generate_password(letters, numbers, symbols)
```

#### 2. `check_strength()`

Determines whether the generated password is Weak, Medium, or Strong.

```python
check_strength(total, numbers, symbols)
```

#### 3. `get_input()`

Validates user input and ensures only non-negative integers are accepted.

```python
get_input(prompt)
```

---

## 🚀 How It Works

1. The user enters:

   * Number of letters
   * Number of numbers
   * Number of symbols

2. The program:

   * Generates random characters
   * Combines them into a list
   * Shuffles the list for randomness
   * Converts the list into a password string

3. The strength checker evaluates the password based on:

   * Total password length
   * Presence of numbers
   * Presence of symbols

---

## 🔑 Password Strength Rules

| Condition                                  | Strength  |
| ------------------------------------------ | --------- |
| Length ≥ 12 and contains numbers & symbols | 💪 Strong |
| Length ≥ 8                                 | 😒 Medium |
| Length < 8                                 | 😿 Weak   |

---

## ▶️ Example Usage

```text
🔐 Password Generator
──────────────────────────────

How many letters? : 6
How many numbers? : 3
How many symbols? : 2

──────────────────────────────
Password : aF8#K2@Lm7P
Length   : 11
Strength : 😒 Medium
──────────────────────────────
```

---

## 🧠 Concepts Used

This project demonstrates:

* Functions
* Loops
* Conditional Statements
* Exception Handling
* User Input Validation
* String Manipulation
* Randomization
* Python Standard Library Usage

---

## 📈 Future Improvements

* Copy password to clipboard
* Save generated passwords to a file
* Password history feature
* GUI using Tkinter
* Web version using Flask or Django
* Custom strength scoring system

---

## 🎯 Learning Outcomes

By building this project, you will learn:

* How to create reusable functions
* Input validation techniques
* Working with lists and strings
* Random password generation
* Basic cybersecurity concepts
* Writing clean and maintainable Python code

---

## 📄 License

This project is open-source and available for educational and personal use.

---

### Author

Developed using Python 🐍 for learning and practicing programming fundamentals.
