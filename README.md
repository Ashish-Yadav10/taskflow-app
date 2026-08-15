# TaskFlow

TaskFlow is a full-stack task management dashboard built for operations teams. It includes a FastAPI backend, a static frontend, SQLite persistence, task tracking, and a lightweight AI-style quick-add flow.

## Features

- Create, update, and delete tasks
- Priority levels: low, medium, high
- Due date handling
- Created timestamp tracking for every task
- Project and user models
- Task search and sorting logic
- FastAPI Swagger API docs
- AI-inspired quick-add task parser
- Frontend dashboard with a glassmorphism-style UI

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- HTML / CSS / JavaScript
- GitHub Pages for static frontend hosting

## Project Structure

```text
.
├── backend/
│   ├── __init__.py
│   ├── ai_parser.py
│   ├── algorithms.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── frontend/
│   ├── app.js
│   ├── index.html
│   └── styles.css
├── docs/
│   ├── app.js
│   ├── index.html
│   └── styles.css
├── .gitignore
├── README.md
├── requirements.txt
├── seed.py
├── check_algorithms.py
├── run_benchmarks.py
├── taskflow.db
├── test_api.py
├── test_full_api.py
└── api_asserts.txt
```

## Quick Start

### 1. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Seed the database

```bash
python seed.py
```

### 4. Start the backend

```bash
uvicorn backend.main:app --reload --port 8000
```

### 5. Start the frontend

```bash
cd frontend
python -m http.server 5500
```

Then open:

```text
http://127.0.0.1:5500
```

## API Overview

### Base URL

```text
http://127.0.0.1:8000
```

### Endpoints

- POST /users
- GET /users
- POST /projects
- GET /projects
- GET /projects/statistics
- POST /tasks
- GET /tasks
- GET /tasks/{task_id}
- PUT /tasks/{task_id}
- DELETE /tasks/{task_id}
- GET /tasks/search
- POST /tasks/quick-add

### Example: create a task

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Review inventory",
    "priority": "high",
    "due_date": "today",
    "project_id": 1
  }'
```

## Documentation

This repository includes the implementation notes and algorithm validation files:

- `check_algorithms.py` for logic verification
- `run_benchmarks.py` for benchmark execution
- `test_api.py` and `test_full_api.py` for API checks
- `api_asserts.txt` for expected API behavior

## Deployment

### GitHub Pages deployment for the frontend

The repository includes a static frontend mirror under the `docs/` folder for GitHub Pages deployment.

Steps:

1. Push the repository to GitHub.
2. Open the GitHub repo.
3. Go to Settings → Pages.
4. Select the main branch and set the source folder to `docs`.
5. Save the configuration.

The deployed page will be available at:

```text
https://Ashish-Yadav10.github.io/taskflow-app/
```

> Note: GitHub Pages hosts the static frontend only. The Python FastAPI backend still needs to run locally or be hosted on a backend platform such as Render, Railway, or Fly.io.

## GitHub Workflow

```bash
git status
git add .
git commit -m "Prepare TaskFlow project for GitHub"
git push origin main
```

## License

This project is for educational and portfolio use.

## Author

Ashish Yadav
