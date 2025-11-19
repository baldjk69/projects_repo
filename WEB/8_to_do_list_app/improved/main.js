// 1- No tasks - Add task button - Task added

`
2- 
Task is clicked -
Remove Task button appear - 
Task removed -
Remove Task button disappear.
`

const tasks = document.querySelector('#tasks')
let taskInput = document.querySelector('#taskInput')
const addBtn = document.querySelector('.add-task-btn')
const removeBtn = document.querySelector('.remove-task-btn')

let selectedTask = null

function addTask(){
  taskText = taskInput.value.trim()
  if(taskText === ""){
    alert('Task cannot be empty')
    return
  } 

  const newTask = document.createElement('li')
  newTask.innerText = taskText
  newTask.addEventListener('click', showRemoveBtn)

  tasks.appendChild(newTask)
  
}

function showRemoveBtn(e){
  selectedTask = e.target
  removeBtn.classList.add('revealed')
}

function removeTask(){
  if(selectedTask){
    selectedTask.remove()
    selectedTask = null
  }
  removeBtn.classList.remove('revealed')
  
}

addBtn.addEventListener('click', addTask)
removeBtn.addEventListener('click', removeTask)



