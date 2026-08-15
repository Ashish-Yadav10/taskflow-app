const API_URL = "http://127.0.0.1:8000";
const DEFAULT_PROJECT_ID = 1;

document.addEventListener("DOMContentLoaded", () => {

    const taskForm =
        document.getElementById("add-task-form");

    const titleInput =
        document.getElementById("task-title");

    const priorityInput =
        document.getElementById("task-priority");

    const dueInput =
        document.getElementById("task-due");

    const titleError =
        document.getElementById("title-error");

    const taskContainer =
        document.getElementById("task-container");


    /* ================================
       LOAD CACHE FIRST
    ================================= */

    const cachedTasks =
        localStorage.getItem("taskflow_tasks");

    if (cachedTasks) {

        try {

            renderTasks(JSON.parse(cachedTasks));

        } catch (error) {

            console.error(
                "Invalid cached tasks:",
                error
            );

        }

    }


    fetchTasks();


    /* ================================
       ADD TASK
    ================================= */

    taskForm.addEventListener(
        "submit",
        async (e) => {

            e.preventDefault();

            titleError.textContent = "";

            const titleVal =
                titleInput.value.trim();


            if (!titleVal) {

                titleError.textContent =
                    "⚠️ Task title is required.";

                titleInput.focus();

                return;
            }


            const newTask = {

                title: titleVal,

                priority:
                    priorityInput.value,

                due_date:
                    dueInput.value.trim() || null,

                project_id:
                    DEFAULT_PROJECT_ID

            };


            try {

                const res =
                    await fetch(
                        `${API_URL}/tasks`,
                        {
                            method: "POST",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body:
                                JSON.stringify(newTask)
                        }
                    );


                if (res.ok) {

                    titleInput.value = "";
                    dueInput.value = "";

                    priorityInput.value =
                        "medium";

                    titleInput.focus();

                    fetchTasks();

                } else {

                    console.error(
                        "Failed to add task."
                    );

                }

            } catch (err) {

                console.error(
                    "Failed to add task:",
                    err
                );

            }

        }
    );


    /* ================================
       FETCH TASKS
    ================================= */

    async function fetchTasks() {

        try {

            const res =
                await fetch(
                    `${API_URL}/tasks`
                );


            if (res.ok) {

                const tasks =
                    await res.json();


                localStorage.setItem(
                    "taskflow_tasks",
                    JSON.stringify(tasks)
                );


                renderTasks(tasks);

            }

        } catch (err) {

            console.error(
                "Error fetching tasks:",
                err
            );


            taskContainer.innerHTML = `

                <div class="connection-error">

                    <div class="error-icon">
                        ⚠️
                    </div>

                    <h3>
                        Server Connection Failed
                    </h3>

                    <p>
                        Make sure your backend server
                        is running on port 8000.
                    </p>

                </div>

            `;

        }

    }


    /* ================================
       RENDER TASKS
    ================================= */

    function renderTasks(tasks) {

        taskContainer.innerHTML = "";


        if (!tasks || tasks.length === 0) {

            taskContainer.innerHTML = `

                <div class="empty-state">

                    <div class="empty-icon">
                        📭
                    </div>

                    <h3>
                        No Tasks Yet
                    </h3>

                    <p>
                        Add your first task using
                        the form above.
                    </p>

                </div>

            `;

            return;
        }


        tasks.forEach(
            (task, index) => {

                const card =
                    document.createElement("div");

                card.className =
                    "task-card";


                card.style.animationDelay =
                    `${index * 0.08}s`;


                /* TASK INFO */

                const infoDiv =
                    document.createElement("div");

                infoDiv.className =
                    "task-info";


                /* TITLE */

                const titleEl =
                    document.createElement("strong");

                titleEl.className =
                    "task-title";

                titleEl.textContent =
                    task.title;


                /* META */

                const metaEl =
                    document.createElement("p");

                metaEl.className =
                    "task-meta";


                const priority =
                    task.priority || "medium";


                metaEl.innerHTML = `

                    <span class="
                        priority-badge
                        priority-${priority}
                    ">
                        ${priority}
                    </span>

                    <span class="due-info">
                        📅 ${task.due_date || "No due date"}
                    </span>

                `;


                infoDiv.appendChild(titleEl);
                infoDiv.appendChild(metaEl);


                /* ACTIONS */

                const actionsDiv =
                    document.createElement("div");

                actionsDiv.className =
                    "task-actions";


                /* EDIT */

                const editBtn =
                    document.createElement("button");

                editBtn.textContent =
                    "✏️ Edit";

                editBtn.className =
                    "edit-btn";


                editBtn.addEventListener(
                    "click",
                    () => editTask(task)
                );


                /* DELETE */

                const deleteBtn =
                    document.createElement("button");

                deleteBtn.textContent =
                    "🗑️ Delete";

                deleteBtn.className =
                    "btn-delete";


                deleteBtn.addEventListener(
                    "click",
                    () => deleteTask(task.id)
                );


                actionsDiv.appendChild(editBtn);
                actionsDiv.appendChild(deleteBtn);


                card.appendChild(infoDiv);
                card.appendChild(actionsDiv);


                taskContainer.appendChild(card);

            }
        );

    }


    /* ================================
       DELETE TASK
    ================================= */

    async function deleteTask(id) {

        const confirmDelete =
            confirm(
                "Are you sure you want to delete this task?"
            );


        if (!confirmDelete) {
            return;
        }


        try {

            const res =
                await fetch(
                    `${API_URL}/tasks/${id}`,
                    {
                        method: "DELETE"
                    }
                );


            if (res.ok) {

                fetchTasks();

            }

        } catch (err) {

            console.error(
                "Error deleting task:",
                err
            );

        }

    }


    /* ================================
       EDIT TASK
    ================================= */

    async function editTask(task) {

        const newTitle =
            prompt(
                "Edit Task Title:",
                task.title
            );


        if (
            newTitle !== null &&
            newTitle.trim() !== ""
        ) {

            try {

                const res =
                    await fetch(
                        `${API_URL}/tasks/${task.id}`,
                        {

                            method: "PUT",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body:
                                JSON.stringify({
                                    title:
                                        newTitle.trim()
                                })

                        }
                    );


                if (res.ok) {

                    fetchTasks();

                }

            } catch (err) {

                console.error(
                    "Error updating task:",
                    err
                );

            }

        }

    }

});