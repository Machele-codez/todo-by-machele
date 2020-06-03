//|~~~~~~~~~~~~~~~~~~~~~~~STYLING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

//? placeholder for `set priority`
document.querySelector('select#id_priority').firstElementChild.innerHTML = 'set priority';
document.querySelector('select#id_priority').firstElementChild.disabled = true;
document.querySelector('select#id_priority').firstElementChild.style.color = 'gray';

//? left edge colour based on task priority 
// document.querySelectorAll('.A').forEach(elem => {
//     elem.style.borderColor = 'red'
// });
// document.querySelectorAll('.B').forEach(elem => {
//     elem.style.borderColor = 'orange'
// });
// document.querySelectorAll('.C').forEach(elem => {
//     elem.style.borderColor = '#ffef00'
// });
// document.querySelectorAll('.D').forEach(elem => {
//     elem.style.borderColor = 'gray'
// });


// | FORM ERRORS

// TODO handling task text errors
const 
taskTexts = document.querySelectorAll('.task-text'),
duplicateError = document.querySelector('.duplicate-error-msg');
addTaskButton = document.querySelector('button[type="submit"]');
taskPriority = document.querySelectorAll('.task-priority')

//? getting all the present tasks into one array
let presentTasks = [];
taskTexts.forEach(elem => {
    presentTasks.push(elem.textContent.trim().toLowerCase());
});

//? prompting user if task exists as user types in input box 
let input = document.querySelector('input[name="text"]');
const h = addTaskButton.style.height;

input.addEventListener('keyup', () => {
    duplicateError.hidden = false
    addTaskButton.style.height = h; //? maintain add task button's height when error message is added below input

    
    if (presentTasks.includes(input.value.trim().toLowerCase())) {
        duplicateError.classList.remove('alright');
        duplicateError.classList.add('already-present');
        duplicateError.innerHTML = 'Task already present';
    } else {
        duplicateError.classList.remove('already-present');
        duplicateError.classList.add('alright');
        duplicateError.innerHTML = 'Can be added';
    }

    if (input.value.trim() === ""){
        duplicateError.hidden = false;
        duplicateError.classList.remove('alright');
        duplicateError.classList.add('already-present');
        duplicateError.innerHTML = 'Task text cannot be empty';
        
    }else{
        document.getElementById('empty-task-alert').hidden = true;
    }

});

input.addEventListener('blur', () => {
    /* clear duplicate error message when input is not active*/
    duplicateError.hidden = true
});



// TODO handling task due datetime errors


const
dateInput = document.getElementById('id_due_date'),
timeInput = document.getElementById('id_due_time');

//TODO Displaying and dismissing alerts (upon firing submit)
addTaskButton.addEventListener('click', e => {
    
    // alert for empty task text submission
    if (input.value.trim() === ""){
        e.preventDefault();
        document.getElementById('empty-task-alert').hidden = false;
    }

    // alert for already present tasks
    // if (presentTasks.includes(input.value.trim().toLowerCase())) {
    //     e.preventDefault();
    //     document.getElementById('duplicate-alert').hidden = false;
    // }
    
    
    // alert for due datetime error
    let 
    dateSplit = dateInput.value.split("-"),
    timeSplit = timeInput.value.split(":"),
    inputDateTime = new Date(dateSplit[0], dateSplit[1] - 1, dateSplit[2], timeSplit[0], timeSplit[1]),
    currentDateTime = new Date();
    // inputDateTimeUTC = Date.UTC(inputDateTime.getFullYear(), inputDateTime.getMonth(), inputDateTime.getDate(), inputDateTime.getHours(), inputDateTime.getMinutes());
    // currentDateTimeUTC = Date.UTC(currentDateTime.getFullYear(), currentDateTime.getMonth(), currentDateTime.getDate(), currentDateTime.getHours(), currentDateTime.getMinutes());
    if (inputDateTime < currentDateTime) {
        e.preventDefault();
        document.getElementById('duedatetime-alert').hidden = false
        console.log("datetime error")
    } else {
        console.log("datetime okay")
    }
})

// dismiss alert for already present tasks
document.getElementById('duplicate-alert-dismiss').addEventListener('click', () =>{
    document.getElementById('duplicate-alert').hidden = true;    
})
// dismiss alert for due datetime error
document.getElementById('duedatetime-alert-dismiss').addEventListener('click', () =>{
    document.getElementById('duedatetime-alert').hidden = true;    
})
document.getElementById('empty-task-alert-dismiss').addEventListener('click', () =>{
    document.getElementById('empty-task-alert').hidden = true;    
})


























// //| form errors
// const fieldErrorDismiss = document.querySelector('.field-errors-close');
// fieldErrorDismiss.addEventListener('click', () => {
//     document.querySelector('.field-errors').style.display = 'none';
// })
