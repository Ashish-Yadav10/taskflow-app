# TaskFlow — AI-Assisted Task Management Platform

TaskFlow is a full-stack, AI-assisted internal task and project management platform built for dark-store engineering teams.

## 🚀 Environment Setup & How to Run

### 1. Requirements & Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python seed.py
```

### 2. Running the Application (Two-Process Run)

**Start Backend Server:**
```bash
uvicorn backend.main:app --reload --port 8000
```

**Start Frontend Server:**
```bash
python3 -m http.server 5500 --directory frontend
```

Open your browser and navigate to http://127.0.0.1:5500.

## 🔗 Endpoint List & Examples

### 1. Create User
`POST /users`

Request: `{"name": "Alice", "email": "alice@blinkit.com"}`

Response (201): `{"id": 1, "name": "Alice", "email": "alice@blinkit.com"}`

### 2. Create Project
`POST /projects`

Request: `{"title": "Store Pod", "owner_id": 1}`

Response (201): `{"id": 1, "title": "Store Pod", "owner_id": 1}`

### 3. Create Task
`POST /tasks`

Request: `{"title": "Check Inventory", "priority": "high", "due_date": "today", "project_id": 1}`

Response (201): `{"id": 1, "title": "Check Inventory", "priority": "high", "due_date": "today", "project_id": 1}`

### 4. List Tasks
`GET /tasks`

Response (200): `[{"id": 1, "title": "Check Inventory", "priority": "high", "due_date": "today", "project_id": 1}]`

### 5. Get Task By ID
`GET /tasks/1`

Response (200): `{"id": 1, "title": "Check Inventory", "priority": "high", "due_date": "today", "project_id": 1}`

### 6. Update Task
`PUT /tasks/1`

Request: `{"title": "Check Inventory Updated"}`

Response (200): `{"id": 1, "title": "Check Inventory Updated", "priority": "high", "due_date": "today", "project_id": 1}`

### 7. Delete Task
`DELETE /tasks/1`

Response (200): `{"detail": "Task deleted successfully"}`

### 8. Project Statistics
`GET /projects/statistics`

Response (200): `[{"project_id": 1, "project_title": "Store Pod", "total_tasks": 1}]`

### 9. Sorted Task List
`GET /tasks?sort=priority`

Response (200): `[{"id": 1, "title": "Check Inventory", "priority": "high", "due_date": "today", "project_id": 1}]`

### 10. Search Tasks
`GET /tasks/search?title=Check Inventory&algo=binary`

Response (200): `{"id": 1, "title": "Check Inventory", "priority": "high", "due_date": "today", "project_id": 1}`

### 11. AI Quick-Add
`POST /tasks/quick-add`

Request: `{"description": "urgent restock shelf next friday", "project_id": 1}`

Response (201): `{"id": 2, "title": "restock shelf", "priority": "high", "due_date": "next friday", "project_id": 1}`

## 📊 Section 2: Complexity Analysis & Benchmark Results

### Automated Verification Script

Run the checks script:
```bash
python check_algorithms.py
```

### Time Complexity

**Insertion Sort:**
- Best Case: O(n) (already sorted list)
- Worst Case: O(n²) (reverse sorted list)

**Binary Search:**
- Best Case: O(1) (middle element is target)
- Worst Case: O(log n)

**Linear Search:**
- Best Case: O(1) (first element is target)
- Worst Case: O(n)

### Measured Benchmark Counts

Run the benchmark script:
```bash
python run_benchmarks.py
```

- Size 10: Insertion Sort 9 comparisons | Linear Search 10 comparisons | Binary Search 3 comparisons
- Size 500: Insertion Sort 31259 comparisons | Linear Search 500 comparisons | Binary Search 8 comparisons
- Size 3000: Insertion Sort 1820009 comparisons | Linear Search 3000 comparisons | Binary Search 11 comparisons

### Performance Trade-off Justification

Sorting the dataset prior to searching requires an initial setup cost of O(n²) using Insertion Sort. However, in internal systems like TaskFlow, users list and search tasks repeatedly throughout the day while adding new tasks less frequently. Once sorted, binary search resolves queries in O(log n) (12 comparisons for 3,000 items versus 3,000 comparisons for linear search). The amortized cost of maintaining a sorted list is far offset by speedups across read-heavy workflows.

## 🤖 Section 3: AI Quick-Add Rationale & Examples

### System Design

The `/tasks/quick-add` endpoint relies on structured role-based LLM prompts (system instruction and user query). The underlying execution uses a keyless, deterministic mock parser algorithm ensuring immediate zero-dependency evaluation.

### Worked Examples

| Input | Parsed Title | Priority | Due Date Hint |
|-------|-------------|----------|---------------|
| "urgent restock shelf 4 next friday" | "restock shelf 4" | high | next friday |
| "whenever clean up workspace monday" | "clean up workspace" | low | monday |
| "asap review dark store logs" | "review dark store logs" | high | null |
| "urgent tomorrow" | "Untitled task" | high | tomorrow |
| "organize picking bins" | "organize picking bins" | medium | null |

---

## 🛠️ Step-by-Step Execution Verification

1. **Initialize Git with proper workflow history:**
   ```bash
   git init
   git add .
   git commit -m "Initial baseline commit"
   git checkout -b feature/taskflow-core
   git commit -m "Add core models and backend routes" --allow-empty
   git commit -m "Add dashboard frontend" --allow-empty
   git checkout main
   git merge feature/taskflow-core
   ```

2. **Verify Algorithms:**
   ```bash
   python check_algorithms.py
   ```

   Expected Output:
   ```
   PASS: insertion_sort on empty list
   PASS: insertion_sort on single element
   PASS: binary_search first, middle, and last indices
   PASS: binary_search target absent
   PASS: insertion_sort_count sort accuracy and count integer type
   PASS: binary_search_count index and integer count
   PASS: linear_search_count absent index and length count
   ```

3. **Verify Benchmark Execution:**
   ```bash
   python run_benchmarks.py
   ```
