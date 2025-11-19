`
TO-DO LIST APP :

1- No tasks, add task button

2- Task is clicked - Remove Task button

`
// 1- No tasks - Add task button - Task added

`
2- 
Task is clicked -
Remove Task button appear - 
Task removed -
Remove Task button disappear.
`

const tasks = document.querySelector('#tasks')
const taskInput = document.querySelector('#task')
const addButton = document.querySelector('.add-task-btn')
const removeBtn = document.querySelector('.remove-task-btn')


function addTask(){
  const newTask = document.createElement('li')
  newTask.innerText = taskInput.value
  newTask.addEventListener('click', showRemoveBtn)
  tasks.appendChild(newTask)
}

function showRemoveBtn(){
  removeBtn.classList.add('revealed')
}

function removeTask(){
  removeBtn.classList.remove('revealed')
  
}

addButton.addEventListener('click', addTask)
removeBtn.addEventListener('click', removeTask)



