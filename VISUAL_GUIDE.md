# 📚 TASKFLOW - COMPLETE VISUAL GUIDE

## 👇 FOLLOW THESE EXACT STEPS

---

## 🎯 STEP-BY-STEP EXECUTION

### STEP 1️⃣: Open PowerShell and Navigate
```
┌─────────────────────────────────────────┐
│ Click Start Menu                        │
│ Type: powershell                        │
│ Press Enter                             │
│                                         │
│ You should see:                         │
│ PS C:\Users\username>                  │
└─────────────────────────────────────────┘

Type this command:
═══════════════════════════════════════════
cd d:\taskflow-app
═══════════════════════════════════════════

Expected output:
PS D:\taskflow-app>
```

---

### STEP 2️⃣: Install Dependencies
```
Command:
═══════════════════════════════════════════
pip install -r requirements.txt
═══════════════════════════════════════════

This will show:
Requirement already satisfied: fastapi>=0.100.0
Requirement already satisfied: uvicorn>=0.22.0
Requirement already satisfied: sqlalchemy>=2.0.0
Requirement already satisfied: pydantic>=2.0.0

⏱️ Takes: 5-10 seconds
✅ Status: DONE
```

---

### STEP 3️⃣: Seed Database
```
Command:
═══════════════════════════════════════════
python seed.py
═══════════════════════════════════════════

This will show:
Database successfully seeded!

⏱️ Takes: 2-3 seconds
✅ Status: DONE
```

---

### STEP 4️⃣: START BACKEND SERVER (Keep This Terminal Open)

```
Command:
═══════════════════════════════════════════
uvicorn backend.main:app --reload --port 8000
═══════════════════════════════════════════

This will show:
INFO:     Will watch for changes in these directories: ['D:\taskflow-app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [20684] using WatchFiles
INFO:     Started server process [5196]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

🟢 Status: BACKEND IS NOW RUNNING ON PORT 8000

⚠️  DO NOT CLOSE THIS TERMINAL!
    DO NOT PRESS CTRL+C!
    KEEP IT RUNNING IN THE BACKGROUND!
```

---

### STEP 5️⃣: OPEN SECOND TERMINAL (NEW PowerShell Window)

```
┌─────────────────────────────────────────┐
│ Click Start Menu                        │
│ Type: powershell                        │
│ Press Enter  (AGAIN - new window)       │
│                                         │
│ You now have 2 terminals open!          │
│ Terminal 1: Running Backend ✅          │
│ Terminal 2: Empty (new window) ✅       │
└─────────────────────────────────────────┘

In the NEW Terminal 2, type:
═══════════════════════════════════════════
cd d:\taskflow-app\frontend
═══════════════════════════════════════════

Expected output:
PS D:\taskflow-app\frontend>
```

---

### STEP 6️⃣: START FRONTEND SERVER

```
In Terminal 2, type:
═══════════════════════════════════════════
python -m http.server 5500
═══════════════════════════════════════════

This will show:
Serving HTTP on :: port 5500 (http://[::]:5500/) ...
Serving HTTP on 0.0.0.0 port 5500 (http://0.0.0.0:5500/) ...

🟢 Status: FRONTEND IS NOW RUNNING ON PORT 5500

⚠️  DO NOT CLOSE THIS TERMINAL!
    DO NOT PRESS CTRL+C!
    KEEP IT RUNNING IN THE BACKGROUND!
```

---

## 🌐 NOW YOU'RE READY TO USE THE APP!

```
┌────────────────────────────────────────────────────────┐
│  OPEN YOUR BROWSER AND GO TO:                          │
│                                                        │
│  🔗 http://127.0.0.1:5500                            │
│                                                        │
│  You should see the TaskFlow Dashboard!               │
│  (With task list and controls)                        │
└────────────────────────────────────────────────────────┘
```

---

## 📊 YOUR SCREEN WILL LOOK LIKE THIS:

### Terminal 1 (BACKEND) - Showing this:
```
PS D:\taskflow-app> uvicorn backend.main:app --reload --port 8000
INFO:     Will watch for changes in these directories: ['D:\taskflow-app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [20684] using WatchFiles
INFO:     Started server process [5196]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

(Waiting for requests...)
```

### Terminal 2 (FRONTEND) - Showing this:
```
PS D:\taskflow-app\frontend> python -m http.server 5500
Serving HTTP on :: port 5500 (http://[::]:5500/) ...
Serving HTTP on 0.0.0.0 port 5500 (http://0.0.0.0:5500/) ...

(Waiting for browser requests...)
```

### Browser - Showing this:
```
┌────────────────────────────────────────────────┐
│ http://127.0.0.1:5500                          │
│                                                │
│  🚀 TASKFLOW DASHBOARD                         │
│                                                │
│  [Create Task Form]                            │
│                                                │
│  [Search Box]                                  │
│                                                │
│  Task 1: Check Inventory - High                │
│  Task 2: Check Payment - Medium                │
│  Task 3: Update Database - Low                 │
│  Task 4: Deploy - High                         │
│                                                │
└────────────────────────────────────────────────┘
```

---

## 🧪 OPTIONAL: TEST THE API

Open a 3rd terminal and try these commands:

### Get All Users:
```powershell
curl http://127.0.0.1:8000/users
```

### Get All Tasks:
```powershell
curl http://127.0.0.1:8000/tasks
```

### View API Documentation:
```
Open browser and go to:
http://127.0.0.1:8000/docs
```

---

## 📊 COMPLETE SYSTEM ARCHITECTURE

```
┌──────────────────────────────────────────────────────────────┐
│                    USER'S COMPUTER                           │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           🌐 WEB BROWSER                            │   │
│  │  http://127.0.0.1:5500                             │   │
│  │  (Display: Tasks, Form, Search)                    │   │
│  └──────────────────────┬──────────────────────────────┘   │
│                         │                                  │
│                         ↓ (AJAX/Fetch Requests)            │
│                         │                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  📡 FRONTEND SERVER (Port 5500)                     │   │
│  │  Python HTTP Server                                │   │
│  │  - Serves: index.html, app.js, styles.css         │   │
│  └──────────────────────┬──────────────────────────────┘   │
│                         │                                  │
│                         ↓ (HTTP Requests)                  │
│                         │                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  🚀 BACKEND SERVER (Port 8000)                      │   │
│  │  FastAPI + Uvicorn                                 │   │
│  │  - Endpoints: /users, /tasks, /projects, /docs    │   │
│  │  - Auto-reload on file changes                     │   │
│  └──────────────────────┬──────────────────────────────┘   │
│                         │                                  │
│                         ↓ (SQL Queries)                    │
│                         │                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  💾 DATABASE (SQLite)                              │   │
│  │  taskflow-app.db                                   │   │
│  │  Tables: users, projects, tasks                    │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## ⏸️ HOW TO STOP THE PROJECT

### Stop Frontend (Terminal 2):
```
In Terminal 2, press:
Ctrl + C

You will see:
^CKeyboard interrupt received, exiting.
PS D:\taskflow-app\frontend>
```

### Stop Backend (Terminal 1):
```
In Terminal 1, press:
Ctrl + C

You will see:
^CShutting down...
Application shutdown complete.
PS D:\taskflow-app>
```

### Close Terminals:
```
Type: exit
Or click X button
```

---

## ✅ COMPLETE CHECKLIST

After following all steps, check these boxes:

```
[ ] Terminal 1 shows "Application startup complete"
[ ] Terminal 2 shows "Serving HTTP on :: port 5500"
[ ] Can access http://127.0.0.1:5500 in browser
[ ] See TaskFlow Dashboard with tasks
[ ] Can access http://127.0.0.1:8000/docs
[ ] API endpoints are working
```

---

## 🆘 TROUBLESHOOTING

### Problem: "Port 8000 already in use"
```
Solution: Use different port
uvicorn backend.main:app --reload --port 8001
```

### Problem: "No module named 'fastapi'"
```
Solution: Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Problem: "Can't connect to http://127.0.0.1:5500"
```
Solution: Make sure Terminal 2 (Frontend) is still running
Look for: "Serving HTTP on :: port 5500"
```

### Problem: "Database error"
```
Solution: Reseed the database
python seed.py
```

---

## 🎯 WHAT YOU CAN DO NOW

✅ **Create Tasks** - Add new tasks via the form  
✅ **View Tasks** - See all tasks in the dashboard  
✅ **Search Tasks** - Find specific tasks  
✅ **Create Users** - Add new users via API  
✅ **Create Projects** - Add new projects  
✅ **Test API** - Use /docs for interactive testing  
✅ **Edit Code** - Backend auto-reloads on save  

---

## 📱 IMPORTANT PORTS

| Service | Port | URL |
|---------|------|-----|
| Frontend | 5500 | http://127.0.0.1:5500 |
| Backend | 8000 | http://127.0.0.1:8000 |
| API Docs | 8000 | http://127.0.0.1:8000/docs |

---

## 📂 FILE LOCATIONS

```
Project Folder: d:\taskflow-app\
├── backend\main.py        ← FastAPI app
├── frontend\index.html    ← UI webpage
└── taskflow-app.db        ← Database (created)
```

---

## 🎬 QUICK DEMO FLOW

```
1. Open http://127.0.0.1:5500 in browser
2. Click "Add Task" button
3. Enter task details
4. Click "Add Task"
5. See new task in the list below
6. Try searching for tasks
7. Click API Docs: http://127.0.0.1:8000/docs
8. Test endpoints interactively
```

---

**🎉 Congratulations! Your TaskFlow Project is Running!** 🚀

For more info, check:
- QUICK_START.md (copy-paste commands)
- TERMINAL_GUIDE.md (detailed setup)
- PROCESS_DIAGRAM.md (system architecture)
