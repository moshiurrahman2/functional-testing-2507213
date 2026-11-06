![Functional Testing CI](https://github.com/moshiurrahman2/functional-testing-2507213/actions/workflows/ci.yml/badge.svg)


# Functional Testing Project

![Functional Testing CI](https://github.com/moshiurrahman2/functional-testing-2507213/actions/workflows/ci.yml/badge.svg)

## Project Description

This project focuses on functional testing of 16 Python functions, including 11 data-type functions and 5 mathematical functions.

The project uses Pytest to test valid inputs, boundary values, invalid inputs, and incorrect data types.

## Technologies Used

- Python
- Pytest
- Pytest-Cov
- Ruff
- Git and GitHub
- GitHub Actions

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/moshiurrahman2/functional-testing-2507213.git
cd functional-testing-2507213
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:

```bash
python -m pytest -q
```

Run tests with line and branch coverage:

```bash
python -m pytest --cov=target --cov-branch --cov-report=term-missing
```

Run linting:

```bash
ruff check .
```

## GitHub Actions CI

GitHub Actions automatically runs the test workflow on pushes and pull requests to the main branch.

The workflow tests the project using:

- Python 3.10
- Python 3.11
- Python 3.12

It also checks code quality and requires 100% test coverage.

## Live Application

Deployment platform: Render

Live URL: Coming Soon

## Suspected Bugs

Any suspected bugs discovered during functional testing will be documented here.

## Author

Moshiur Rahman