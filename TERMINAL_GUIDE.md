# 🚀 TaskFlow Project - Complete Terminal Guide

## 📋 Complete Step-by-Step Process to Run the Project

### ✅ STEP 1: Navigate to Project Directory
```powershell
cd d:\taskflow-app
```
**Expected Output:**
```
PS D:\taskflow-app>
```

---

### ✅ STEP 2: Check Python Installation
```powershell
python --version
```
**Expected Output:**
```
Python 3.12.0 (or higher)
```

---

### ✅ STEP 3: Install Dependencies
```powershell
pip install -r requirements.txt
```
**Expected Output:**
```
Requirement already satisfied: fastapi>=0.100.0 in c:\users\...\python312\site-packages (0.136.1)
Requirement already satisfied: uvicorn>=0.22.0 in c:\users\...\python312\site-packages (0.47.0)
Requirement already satisfied: sqlalchemy>=2.0.0 in c:\users\...\python312\site-packages (2.0.51)
Requirement already satisfied: pydantic>=2.0.0 in c:\users\...\python312\site-packages (2.13.4)
```

---

### ✅ STEP 4: Initialize Database with Sample Data
```powershell
python seed.py
```
**Expected Output:**
```
Database successfully seeded!
```

---

### ✅ STEP 5: Start Backend Server (Terminal 1)
```powershell
uvicorn backend.main:app --reload --port 8000
```
**Expected Output:**
```
INFO:     Will watch for changes in these directories: ['D:\taskflow-app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [20684] using WatchFiles
INFO:     Started server process [5196]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
✅ Backend is now running on **http://127.0.0.1:8000**

---

### ✅ STEP 6: Start Frontend Server (Terminal 2 - OPEN NEW TERMINAL)
```powershell
cd d:\taskflow-app\frontend
python -m http.server 5500
```
**Expected Output:**
```
Serving HTTP on :: port 5500 (http://[::]:5500/) ...
Serving HTTP on 0.0.0.0 port 5500 (http://0.0.0.0:5500/) ...
```
✅ Frontend is now running on **http://127.0.0.1:5500**

---

## 🎯 Access the Application

### 🌐 Frontend (User Interface)
```
http://127.0.0.1:5500
```
Open this in your browser to see the TaskFlow dashboard

### 📚 Backend API Documentation (Swagger UI)
```
http://127.0.0.1:8000/docs
```
Interactive API testing and documentation

### 📊 Alternative API Docs (ReDoc)
```
http://127.0.0.1:8000/redoc
```

---

## 📞 Testing API Endpoints

### Test 1: Create a User
```powershell
curl -X POST http://127.0.0.1:8000/users `
  -H "Content-Type: application/json" `
  -d '{"name": "John Doe", "email": "john@example.com"}'
```
**Expected Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

### Test 2: Get All Users
```powershell
curl http://127.0.0.1:8000/users
```

### Test 3: Create a Project
```powershell
curl -X POST http://127.0.0.1:8000/projects `
  -H "Content-Type: application/json" `
  -d '{"title": "Store Pod", "owner_id": 1}'
```

### Test 4: Create a Task
```powershell
curl -X POST http://127.0.0.1:8000/tasks `
  -H "Content-Type: application/json" `
  -d '{"title": "Check Inventory", "priority": "high", "due_date": "today", "project_id": 1}'
```

---

## 🎮 Terminal Setup Summary

### Terminal 1: Backend Server
```
cd d:\taskflow-app
uvicorn backend.main:app --reload --port 8000
```
**Status:** Running on Port 8000 ✅

### Terminal 2: Frontend Server
```
cd d:\taskflow-app\frontend
python -m http.server 5500
```
**Status:** Running on Port 5500 ✅

### Terminal 3 (Optional): Testing/API Calls
```
cd d:\taskflow-app
python -m pytest  (if you want to run tests)
```

---

## 🛑 Stopping the Application

### Stop Backend Server
Press `Ctrl + C` in Terminal 1
```
Shutting down...
^CApplication shutdown complete.
```

### Stop Frontend Server
Press `Ctrl + C` in Terminal 2
```
^C
Keyboard interrupt received, exiting.
```

---

## 📁 Project Structure

```
d:\taskflow-app\
├── backend\
│   ├── main.py          (FastAPI app)
│   ├── models.py        (Database models)
│   ├── schemas.py       (Pydantic schemas)
│   ├── database.py      (SQLAlchemy setup)
│   ├── algorithms.py    (Business logic)
│   └── ai_parser.py     (AI parsing)
├── frontend\
│   ├── index.html       (UI)
│   ├── app.js          (JavaScript logic)
│   └── styles.css      (Styling)
├── requirements.txt     (Python dependencies)
├── seed.py             (Database seeding)
├── run_benchmarks.py   (Performance testing)
├── test_api.py         (API tests)
└── README.md
```

---

## 🔧 Troubleshooting

### Issue: Port 8000 Already in Use
```powershell
# Change port in command
uvicorn backend.main:app --reload --port 8001
```

### Issue: Port 5500 Already in Use
```powershell
# Change port in command
python -m http.server 5501 --directory frontend
```

### Issue: Module Not Found Error
```powershell
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Issue: Database Locked
```powershell
# Reseed database
python seed.py
```

---

## ✨ Features to Test

1. **Create Tasks** - Add new tasks via the UI
2. **View Tasks** - See all tasks in the dashboard
3. **Search Tasks** - Search by title or priority (if implemented)
4. **Update Tasks** - Modify existing tasks
5. **Delete Tasks** - Remove tasks
6. **Manage Users** - Create and view users
7. **Manage Projects** - Create projects and organize tasks

---

## 📊 Expected File Structure After Running

```
taskflow-app.db        (SQLite database - created by seed.py)
task.log              (Log file)
```

---

## 🎯 Quick Reference Commands

| Task | Command |
|------|---------|
| Navigate to project | `cd d:\taskflow-app` |
| Install deps | `pip install -r requirements.txt` |
| Seed database | `python seed.py` |
| Start backend | `uvicorn backend.main:app --reload --port 8000` |
| Start frontend | `python -m http.server 5500 --directory frontend` |
| Access UI | `http://127.0.0.1:5500` |
| Access API Docs | `http://127.0.0.1:8000/docs` |
| Stop server | `Ctrl + C` |

---

## ✅ Verification Checklist

- [ ] Python installed (3.8+)
- [ ] All dependencies installed
- [ ] Database seeded successfully
- [ ] Backend running on port 8000
- [ ] Frontend running on port 5500
- [ ] Can access http://127.0.0.1:5500 in browser
- [ ] Can access http://127.0.0.1:8000/docs in browser
- [ ] API endpoints responding correctly

---

**🚀 Your project is ready to run!**
