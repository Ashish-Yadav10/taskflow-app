import requests
import time
import subprocess
import json

backend = subprocess.Popen(["uvicorn", "backend.main:app", "--port", "8000"], cwd="d:/taskflow-app")
time.sleep(2)

try:
    # 1. Create a task
    print("Testing create task...")
    res = requests.post("http://127.0.0.1:8000/tasks", json={
        "title": "Check API",
        "priority": "low",
        "due_date": "today",
        "project_id": 1
    })
    print("CREATE TASK:", res.status_code)
    task_id = res.json().get("id")
    
    # 2. Add via Quick Add
    res = requests.post("http://127.0.0.1:8000/tasks/quick-add", json={
        "description": "urgent fix bugs next friday",
        "project_id": 1
    })
    print("QUICK ADD:", res.status_code, res.json())
    
    # 3. Search task
    res = requests.get("http://127.0.0.1:8000/tasks/search?title=Check API&algo=binary")
    print("SEARCH:", res.status_code, res.json())

    # 4. Sort tasks
    res = requests.get("http://127.0.0.1:8000/tasks?sort=priority")
    print("SORTED TASKS PRIORITY ORDER:")
    for t in res.json():
        print(f"[{t['priority']}] {t['title']}")

finally:
    backend.terminate()
