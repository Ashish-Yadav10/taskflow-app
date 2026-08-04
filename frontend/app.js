const API_URL = "http://127.0.0.1:8000";
const DEFAULT_PROJECT_ID = 1;

document.addEventListener("DOMContentLoaded", () => {
    const taskForm = document.getElementById("add-task-form");
    const titleInput = document.getElementById("task-title");
    const priorityInput = document.getElementById("task-priority");
    const dueInput = document.getElementById("task-due");
    const titleError = document.getElementById("title-error");
    const taskContainer = document.getElementById("task-container");

    // Section 1 Task 6: LocalStorage Cache First
    const cachedTasks = localStorage.getItem("taskflow_tasks");
    if (cachedTasks) {
        renderTasks(JSON.parse(cachedTasks));
    }

    fetchTasks();

    // Client-side Validation & Form Submission
    taskForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        titleError.textContent = "";

        const titleVal = titleInput.value.trim();
        if (!titleVal) {
            titleError.textContent = "Title is required";
            return;
        }

        const newTask = {
            title: titleVal,
            priority: priorityInput.value,
            due_date: dueInput.value.trim() || null,
            project_id: DEFAULT_PROJECT_ID
        };

        try {
            const res = await fetch(`${API_URL}/tasks`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(newTask)
            });

            if (res.ok) {
                titleInput.value = "";
                dueInput.value = "";
                fetchTasks();
            }
        } catch (err) {
            console.error("Failed to add task:", err);
        }
    });

    async function fetchTasks() {
        try {
            const res = await fetch(`${API_URL}/tasks`);
            if (res.ok) {
                const tasks = await res.json();
                localStorage.setItem("taskflow_tasks", JSON.stringify(tasks));
                renderTasks(tasks);
            }
        } catch (err) {
            console.error("Error fetching tasks:", err);
        }
    }

    function renderTasks(tasks) {
        taskContainer.innerHTML = "";
        
        if (tasks.length === 0) {
            const emptyMsg = document.createElement("p");
            emptyMsg.textContent = "No tasks available.";
            taskContainer.appendChild(emptyMsg);
            return;
        }

        tasks.forEach(task => {
            const card = document.createElement("div");
            card.className = "task-card";

            const infoDiv = document.createElement("div");
            const titleEl = document.createElement("strong");
            titleEl.textContent = task.title;

            const metaEl = document.createElement("p");
            metaEl.textContent = `Priority: ${task.priority} | Due: ${task.due_date || 'N/A'}`;

            infoDiv.appendChild(titleEl);
            infoDiv.appendChild(metaEl);

            const actionsDiv = document.createElement("div");
            actionsDiv.className = "task-actions";

            const editBtn = document.createElement("button");
            editBtn.textContent = "Edit";
            editBtn.addEventListener("click", () => editTask(task));

            const deleteBtn = document.createElement("button");
            deleteBtn.textContent = "Delete";
            deleteBtn.className = "btn-delete";
            deleteBtn.addEventListener("click", () => deleteTask(task.id));

            actionsDiv.appendChild(editBtn);
            actionsDiv.appendChild(deleteBtn);

            card.appendChild(infoDiv);
            card.appendChild(actionsDiv);
            taskContainer.appendChild(card);
        });
    }

    async function deleteTask(id) {
        try {
            const res = await fetch(`${API_URL}/tasks/${id}`, { method: "DELETE" });
            if (res.ok) fetchTasks();
        } catch (err) {
            console.error("Error deleting task:", err);
        }
    }

    async function editTask(task) {
        const newTitle = prompt("Edit Task Title:", task.title);
        if (newTitle !== null && newTitle.trim() !== "") {
            try {
                const res = await fetch(`${API_URL}/tasks/${task.id}`, {
                    method: "PUT",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ title: newTitle.trim() })
                });
                if (res.ok) fetchTasks();
            } catch (err) {
                console.error("Error updating task:", err);
            }
        }
    }
});
