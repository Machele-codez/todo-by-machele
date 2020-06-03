//Ajax Delete
function deleteTask(pk, text, url){
    const confirmDelete = confirm(`Are you sure you want to delete this task?\n${text}`);
    if (confirmDelete){
        $.ajax({
            url: url,
            data: {
                task_pk: pk,
            },
            dataType: 'json',
            success: (data) => {
                if (data.deleted){
                    $(`#task_${pk}`).remove();
                    console.log("Task Removed")
                }
            }
        })
    }
}

//Ajax Complete
function completeTask(pk, url, priority){
    console.log(pk, url)
    // $.ajax({
    //     url: url,
    //     data: {
    //         task_pk: pk,
    //     },
    //     success: updateToCompletedTaskAppearance(),
    // })

    // function updateToCompletedTaskAppearance(){
        
    // }
    //code below must be in the function: updateToCompletedTaskAppearance
    $(`#task_${pk} .task .task-priority`)[0].classList.remove(priority)
    $(`#task_${pk} .task .task-priority`)[0].classList.add('completed-priority')
    
    $(`#task_${pk} .task-time .due-time`)[0].classList.remove("due" || "not-due")
    $(`#task_${pk} .task-time .due-time`)[0].classList.add("completed-due")
    $(`#task_${pk} .task-time .due-time`)[0].innerHTML = '<b>Completed</b>'

    $(`#task_${pk} .task-options .option-complete`)[0].onclick = "undoComplete({{task.pk}}, `{% url 'tasks:undocomplete' %}`, priority={{task.priority}})"
    $(`#task_${pk} .task-options .option-complete`)[0].title = "Undo Complete"
    $(`#task_${pk} .task-options .option-complete`)[0].innerHTML = '<i class="fas fa-undo"></i>'
    $(`#task_${pk} .task-options .option-complete`)[0].classList.replace("option-complete", "option-undocomplete")
    

}