# Password Strength Check

A simple Python CLI tool that evaluates password strength based on common security rules.

## Features
- Checks minimum password length (8 characters)
- Verifies presence of:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Provides a strength score and clear improvement suggestions

## Tech Stack
- Python 3
- Regular Expressions (`re` module)

## How It Works
The program analyzes the entered password against multiple validation rules.
Each satisfied rule increases the strength score, while unmet rules generate feedback.
