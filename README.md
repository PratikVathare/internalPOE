# MLOps-POE

This is a very simple beginner-friendly Python project for an MLOps practical exam.
It demonstrates basic Python execution, testing, Docker, and project structure without using any framework or model.

## Project structure

- `hello.py` - The main Python script that prints the message.
- `test_hello.py` - A simple pytest test to check the output.
- `Dockerfile` - Builds a Docker image for the project.
- `requirements.txt` - Lists the Python packages needed.
- `.gitignore` - Prevents unnecessary files from being uploaded to Git.
- `README.md` - Project documentation.

## Installation steps

1. Open Command Prompt or PowerShell.
2. Go to the project folder:
   ```bash
   cd MLOps-POE
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment on Windows:
   ```bash
   .venv\Scripts\Activate.ps1
   ```
   If PowerShell blocks activation, run:
   ```bash
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Git commands

Initialize Git:
```bash
git init
```

Check status:
```bash
git status
```

Add files:
```bash
git add .
```

Commit changes:
```bash
git commit -m "Initial project setup"
```

Create a branch (optional):
```bash
git checkout -b main
```

## Docker build and run commands

Build the Docker image:
```bash
docker build -t mlops-poe .
```

Run the Docker container:
```bash
docker run --rm mlops-poe
```

This will print:
```bash
Hello MLOps
```

## Pytest commands

Run tests:
```bash
pytest
```

If you want to see more details:
```bash
pytest -v
```

## Brief explanation of Jenkins usage

Jenkins is a tool used for automation in DevOps. It can run build, test, and deployment jobs automatically whenever code changes happen. In this simple project, Jenkins could be used to run `pytest` and check whether the code builds correctly. This is part of CI/CD practice in MLOps.

## Brief explanation of Evidently

Evidently is a Python library used to monitor machine learning models and data quality. It helps check if model performance or input data changes over time. In this beginner project, we only include it in the requirements list to show that it is a common MLOps tool, but we do not use an actual model.

## Simple project purpose

This project is designed to help beginners understand:
- Python basics
- Unit testing
- Docker containers
- Git essentials
- CI/CD concepts
- Common MLOps tools
