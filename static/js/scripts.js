// Função para adicionar uma nova tarefa via API
function addTask() {
    const title = document.getElementById('taskTitle').value;

    fetch('/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + localStorage.getItem('token')
        },
        body: JSON.stringify({ title: title })
    })
    .then(response => response.json())
    .then(data => {
        if (data.id) {
            // Atualiza a interface com a nova tarefa
            listTasks();
        }
    });
}

// Função para listar todas as tarefas
function listTasks() {
    fetch('/tasks', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('token')
        }
    })
    .then(response => response.json())
    .then(tasks => {
        const taskList = document.getElementById('taskList');
        taskList.innerHTML = '';  // Limpa a lista atual

        tasks.forEach(task => {
            const taskItem = document.createElement('li');
            taskItem.className = `task-item ${task.status}`;
            taskItem.textContent = task.title;

            // Adiciona à lista
            taskList.appendChild(taskItem);
        });
    });
}

// Função para atualizar o status de uma tarefa (pendente/completa)
function updateTask(id, status) {
    fetch(`/tasks/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + localStorage.getItem('token')
        },
        body: JSON.stringify({ status: status })
    })
    .then(response => response.json())
    .then(data => {
        listTasks();  // Atualiza a lista após a atualização
    });
}

// Função para deletar uma tarefa
function deleteTask(id) {
    fetch(`/tasks/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('token')
        }
    })
    .then(response => response.json())
    .then(data => {
        listTasks();  // Atualiza a lista após a remoção
    });
}

// Chama a listagem de tarefas quando a página é carregada
window.onload = listTasks;
