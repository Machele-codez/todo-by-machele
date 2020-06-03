const 
signupForm = document.forms['signup-form'],
username = signupForm['username'],
password = signupForm['password1'],
passwordConfirm = signupForm['password2'];

for (let i = 0; i < signupForm.length; i++){
    if (document.getElementById(`${signupForm[i].name}-help-text`)) {
        signupForm[i].addEventListener('keyup', () => {
            document.getElementById(`${signupForm[i].name}-help-text`).style.display = 'block';
        });
        signupForm[i].addEventListener('focus', () => {
            document.getElementById(`${signupForm[i].name}-help-text`).style.display = 'block';
        });
        signupForm[i].addEventListener('blur', () => {
            document.getElementById(`${signupForm[i].name}-help-text`).style.display = 'none';
        });
    }
}

const fieldErrorDismiss = document.querySelector('.field-errors-close');

fieldErrorDismiss.addEventListener('click', () => {
    document.querySelector('.field-errors').style.display = 'none';
})