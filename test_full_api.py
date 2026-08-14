import requests
import json
import sys

API_URL = "http://127.0.0.1:8000"

def run_tests():
    print("--- STARTING FULL TASKFLOW API INTEGRATION TESTS ---")

    # 1. Check list tasks (initial state)
    try:
        res = requests.get(f"{API_URL}/tasks")
        if res.status_code != 200:
            print(f"FAIL: /tasks status {res.status_code}")
            sys.exit(1)
        tasks = res.json()
        print(f"PASS: Fetch tasks count initially: {len(tasks)}")
    except Exception as e:
        print(f"FAIL: Cannot connect to API: {e}")
        sys.exit(1)

    # 2. Get project statistics
    res = requests.get(f"{API_URL}/projects/statistics")
    assert res.status_code == 200, "Stats failed"
    stats = res.json()
    print(f"PASS: Statistics fetched: {stats}")

    # 3. Create a new task (standard)
    new_task_payload = {
        "title": "Integration Test Task",
        "priority": "medium",
        "due_date": "next week",
        "project_id": 1
    }
    res = requests.post(f"{API_URL}/tasks", json=new_task_payload)
    assert res.status_code == 201, f"Create task failed: {res.text}"
    created_task = res.json()
    task_id = created_task["id"]
    assert created_task["title"] == "Integration Test Task"
    assert created_task["priority"] == "medium"
    assert created_task["due_date"] == "next week"
    assert created_task["project_id"] == 1
    print(f"PASS: Created task id {task_id}")

    # 4. Search task (linear search)
    res = requests.get(f"{API_URL}/tasks/search?title=Integration Test Task&algo=linear")
    assert res.status_code == 200, f"Search failed: {res.text}"
    searched_task = res.json()
    assert searched_task["id"] == task_id
    print("PASS: Search task (linear) succeeded")

    # 5. Search task (binary search)
    res = requests.get(f"{API_URL}/tasks/search?title=Integration Test Task&algo=binary")
    assert res.status_code == 200, f"Search failed: {res.text}"
    searched_task_bin = res.json()
    assert searched_task_bin["id"] == task_id
    print("PASS: Search task (binary) succeeded")

    # 6. Update task title
    update_payload = {
        "title": "Integration Test Task Updated",
        "priority": "high",
        "due_date": "tomorrow"
    }
    res = requests.put(f"{API_URL}/tasks/{task_id}", json=update_payload)
    assert res.status_code == 200, f"Update task failed: {res.text}"
    updated_task = res.json()
    assert updated_task["title"] == "Integration Test Task Updated"
    assert updated_task["priority"] == "high"
    assert updated_task["due_date"] == "tomorrow"
    print("PASS: Task update succeeded")

    # 7. Sort tasks by priority (high should be first)
    res = requests.get(f"{API_URL}/tasks?sort=priority")
    assert res.status_code == 200, f"Sort failed: {res.text}"
    sorted_tasks = res.json()
    assert len(sorted_tasks) > 0
    # First item must be 'high' priority since we updated a task to 'high'
    assert sorted_tasks[0]["priority"] == "high", "First task not high priority"
    print("PASS: Task sorting by priority verified")

    # 8. Delete task
    res = requests.delete(f"{API_URL}/tasks/{task_id}")
    assert res.status_code == 200, f"Delete task failed: {res.text}"
    print("PASS: Task deletion succeeded")

    # 9. Verify task is actually deleted from server
    res = requests.get(f"{API_URL}/tasks/{task_id}")
    assert res.status_code == 404, "Task still exists after deletion"
    print("PASS: Clicked deleted task responds with 404")

    # 10. Quick Add Task
    quick_payload = {
        "description": "urgent complete review next monday",
        "project_id": 1
    }
    res = requests.post(f"{API_URL}/tasks/quick-add", json=quick_payload)
    assert res.status_code == 201, f"Quick add failed: {res.text}"
    quick_task = res.json()
    assert quick_task["title"] == "complete review", f"Expected title 'complete review', got '{quick_task['title']}'"
    assert quick_task["priority"] == "high" # "urgent" maps to high
    assert quick_task["due_date"] == "next monday"
    print("PASS: Quick-add task parsed and created successfully")

    # Delete the quick-added task to leave database clean
    res = requests.delete(f"{API_URL}/tasks/{quick_task['id']}")
    assert res.status_code == 200

    print("--- ALL INTEGRATION TESTS PASSED WITH 100% ACCURACY! ---")

if __name__ == "__main__":
    run_tests()
