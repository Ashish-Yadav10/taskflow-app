import time
from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional

from backend.database import engine, Base, get_db
from backend.models import User, Project, Task
from backend.schemas import (
    UserCreate, UserResponse,
    ProjectCreate, ProjectResponse,
    TaskCreate, TaskUpdate, TaskResponse,
    QuickAddRequest
)
from backend.algorithms import insertion_sort, binary_search, linear_search
from backend.ai_parser import mock_ai_parse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow API")

# Section 1 Task 8: CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

# Section 1 Task 7: Custom Logging Middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    print(f"[{request.method}] {request.url.path} - Processing time: {process_time:.2f}ms")
    return response


# --- User Endpoints ---
@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()


# --- Project Endpoints ---
@app.post("/projects", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    owner = db.query(User).filter(User.id == project.owner_id).first()
    if not owner:
        raise HTTPException(status_code=404, detail="User owner not found")
    db_project = Project(title=project.title, owner_id=project.owner_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.get("/projects", response_model=List[ProjectResponse])
def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()


# --- Section 1 Task 5: Statistics Endpoint ---
@app.get("/projects/statistics")
def get_project_statistics(db: Session = Depends(get_db)):
    results = (
        db.query(
            Project.id.label("project_id"),
            Project.title.label("project_title"),
            func.count(Task.id).label("total_tasks")
        )
        .outerjoin(Task, Project.id == Task.project_id)
        .group_by(Project.id)
        .all()
    )
    return [
        {"project_id": r.project_id, "project_title": r.project_title, "total_tasks": r.total_tasks}
        for r in results
    ]


# --- Task Endpoints ---
@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    proj = db.query(Project).filter(Project.id == task.project_id).first()
    if not proj:
        raise HTTPException(status_code=404, detail="Project not found")
    db_task = Task(title=task.title, priority=task.priority, due_date=task.due_date, project_id=task.project_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# Section 2 Task 4: Custom sorted list endpoint using insertion_sort
@app.get("/tasks", response_model=List[TaskResponse])
def list_tasks(sort: Optional[str] = None, db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    task_dicts = [
        {"id": t.id, "title": t.title, "priority": t.priority, "due_date": t.due_date, "project_id": t.project_id}
        for t in tasks
    ]

    if sort == "priority":
        priority_map = {"high": 1, "medium": 2, "low": 3}
        for t in task_dicts:
            t["_rank"] = priority_map.get(t["priority"], 2)
        
        # In-place insertion sort execution
        insertion_sort(task_dicts, "_rank")
        
        for t in task_dicts:
            del t["_rank"]

    return task_dicts


@app.get("/tasks/search")
def search_tasks(title: str, algo: str = "binary", db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    index = [{"id": t.id, "title": t.title, "priority": t.priority, "due_date": t.due_date, "project_id": t.project_id} for t in tasks]

    matched_idx = -1
    if algo == "binary":
        insertion_sort(index, "title")
        matched_idx = binary_search(index, title, "title")
    else:
        matched_idx = linear_search(index, title, "title")

    if matched_idx == -1:
        raise HTTPException(status_code=404, detail="Task not found")

    return index[matched_idx]


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if task_update.title is not None:
        db_task.title = task_update.title
    if task_update.priority is not None:
        db_task.priority = task_update.priority
    if task_update.due_date is not None:
        db_task.due_date = task_update.due_date

    db.commit()
    db.refresh(db_task)
    return db_task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"detail": "Task deleted successfully"}


# --- Section 3 Task 1: AI Quick-Add Endpoint ---
@app.post("/tasks/quick-add", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def quick_add_task(payload: QuickAddRequest, db: Session = Depends(get_db)):
    proj = db.query(Project).filter(Project.id == payload.project_id).first()
    if not proj:
        raise HTTPException(status_code=404, detail="Project not found")

    # Structured role-based prompt definition
    messages = [
        {"role": "system", "content": "Extract task title, priority (low/medium/high), and due date phrase."},
        {"role": "user", "content": payload.description}
    ]

    parsed = mock_ai_parse(payload.description)

    db_task = Task(
        title=parsed["title"],
        priority=parsed["priority"],
        due_date=parsed["due_date_hint"],
        project_id=payload.project_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
