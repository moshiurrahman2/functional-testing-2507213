# Functional Testing Project

[![Functional Testing CI](https://github.com/moshiurrahman2/functional-testing-2507213/actions/workflows/ci.yml/badge.svg)](https://github.com/moshiurrahman2/functional-testing-2507213/actions/workflows/ci.yml)
[![Render Deployment Pipeline](https://github.com/moshiurrahman2/functional-testing-2507213/actions/workflows/deploy.yml/badge.svg)](https://github.com/moshiurrahman2/functional-testing-2507213/actions/workflows/deploy.yml)

## Project Description

This project focuses on functional testing of 16 Python functions, including 11 data-type functions and 5 mathematical functions.

The project uses Pytest to test valid inputs, boundary values, invalid inputs, and incorrect data types.

It also includes a Flask-based web application that allows users to execute the Python functions through a web interface.

## Technologies Used

- Python
- Flask
- Pytest
- Pytest-Cov
- Ruff
- Git and GitHub
- GitHub Actions
- Render

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

### 3. Activate the virtual environment

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

## Running the Web Application Locally

Start the Flask application:

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000/
```

## GitHub Actions CI

GitHub Actions automatically runs the testing workflow on pushes and pull requests to the main branch.

The workflow tests the project using:

- Python 3.10
- Python 3.11
- Python 3.12

It also performs linting, checks line and branch coverage, and requires 100% coverage.

## Deployment Pipeline

The project uses GitHub Actions and Render for automated deployment.

The deployment workflow:

1. Checks whether the CI workflow succeeds.
2. Deploys the successful main branch commit to Render.
3. Waits for the deployed commit SHA to match the expected commit.
4. Runs three smoke tests against the live application.

Render automatic deployment is disabled so deployment is controlled by GitHub Actions.

## Live Application

**Deployment Platform:** Render

**Live URL:** https://functional-testing-2507213-2.onrender.com/

**Health Check:** https://functional-testing-2507213-2.onrender.com/health

The health endpoint returns the deployment status and deployed Git commit SHA.

## Suspected Bugs and Potential Edge Cases

The following potential issues should be investigated and tested:

1. The `common_items` endpoint assumes that two arguments are provided. Missing arguments may cause an unhandled `IndexError`.
2. The `common_items` endpoint converts its arguments into sets. Non-iterable inputs may cause a `TypeError`.
3. Sorting the returned set may fail if its elements contain incompatible data types.
4. Invalid or unexpected JSON request bodies should be tested to ensure the application returns appropriate error responses.

These are potential application-level issues identified during code review, not confirmed bugs in the 16 target functions.

## Author

Moshiur Rahman

## Troubleshooting

If the application does not start:

1. Activate the virtual environment.
2. Install dependencies using pip install -r requirements.txt.
3. Run python app.py.
4. Open http://127.0.0.1:5000/ in your browser.