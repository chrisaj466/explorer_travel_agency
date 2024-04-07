//const form = document.getElementById('form');
//const username= document.getElementById("username")
//const password = document.getElementById("password")
//const submitButton = document.getElementById('submit');
//const validity = {
//    username: false,
//    password: false,
//
//};
//form.addEventListener('submit', e => {
//    e.preventDefault();
//
//    validateInputs();
//    submitButton.disabled = true;
//
//    // if (Object.values(validity).every(value => value)) {
//    //     // Redirect to the home page
//    //     openuserlogin()
//    // }
//
//
//});
//const setError = (element, message) => {
//    const inputControl = element.parentElement;
//    const errorDisplay = inputControl.querySelector('.error');
//
//    errorDisplay.innerText = message;
//    inputControl.classList.add('error');
//    inputControl.classList.remove('success')
//
//    validity[element.id] = false;
//
//    // submitButton.disabled = true;
//}
//const setSuccess = element => {
//    const inputControl = element.parentElement;
//    const errorDisplay = inputControl.querySelector('.error');
//
//    errorDisplay.innerText = '';
//    inputControl.classList.add('success');
//    inputControl.classList.remove('error');
//
//    validity[element.id] = true;
//
//    // if (Object.values(validity).every(value => value)) {
//    //     submitButton.disabled = false;
//    // }
//};
//const validateInputs = () => {
//    const usernameValue = username.value.trim();
//    const passwordValue = password.value.trim();
//    if(usernameValue === '') {
//        setError(username, 'Username is required');
//        value1=false
//    } else {
//        setSuccess(username);
//        value1=true
//    }
//
//    if(passwordValue === '') {
//        setError(password, 'Password is required');
//        value2=false
//    }
//    else{
//        setSuccess(password);
//        value2=true
//    }
//
//
//}
//
//if (Object.values(validity).every(value => value)) {
//
//    function openuserlogin() {
//    // You can replace 'https://example.com' with the URL of the page you want to open
//    window.location.href = 'http://127.0.0.1:5500/home.html';
//
//}
//    openuserlogin()
//
//
//}
//





//const form = document.getElementById('login-form');
//const username = document.getElementById("login-username")
//const password = document.getElementById("login-password")
//const submitButton = document.getElementById('login-submit');
//const errorDisplay = document.getElementById('login-error');
//
//const validity = {
//    username: false,
//    password: false,
//};
//
//form.addEventListener('submit', e => {
//    e.preventDefault();
//    validateInputs();
//});
//
////const setError = (element, message) => {
////    const inputControl = element.parentElement;
////    errorDisplay.innerText = message;
////    inputControl.classList.add('error');
////    inputControl.classList.remove('success');
////    validity[element.id] = false;
////}
//const setError = (element, message) => {
//    const inputControl = element.parentElement;
//    const errorDisplay = inputControl.querySelector('.error-message');
//    errorDisplay.innerText = message;
//    inputControl.classList.add('error');
//    inputControl.classList.remove('success');
//    validity[element.id] = false;
//}
//const setSuccess = element => {
//    const inputControl = element.parentElement;
//    errorDisplay.innerText = '';
//    inputControl.classList.add('success');
//    inputControl.classList.remove('error');
//    validity[element.id] = true;
//};
//
//const validateInputs = () => {
//    const usernameValue = username.value.trim();
//    const passwordValue = password.value.trim();
//    if(usernameValue === '') {
//        setError(username, 'Username is required');
//    } else {
//        setSuccess(username);
//    }
//
//    if(passwordValue === '') {
//        setError(password, 'Password is required');
//    }
//    else{
//        setSuccess(password);
//    }
//
//    if (Object.values(validity).every(value => value)) {
//        submitForm();
//    }
//}
//
//const submitForm = () => {
//    const formData = new FormData(form);
//    fetch('/login/', {
//        method: 'POST',
//        body: formData
//    })
//    .then(response => {
//        if (response.ok) {
//            // Redirect to the home page
//            window.location.href = '/';  // Redirect to the home page
//        } else {
//            // Handle failed login (e.g., display error message)
//            console.error('Login failed');
//            // You can display an error message to the user here
//        }
//    })
//    .catch(error => {
//        console.error('Error occurred during login:', error);
//        // Handle error (e.g., display error message)
//    });
//};





const form = document.getElementById('form');
const username = document.getElementById("username")
const password = document.getElementById("password")
const submitButton = document.getElementById('submit');
const usernameError = document.getElementById('username-error');
const passwordError = document.getElementById('password-error');

const validity = {
    username: false,
    password: false,
};

form.addEventListener('submit', e => {
    e.preventDefault();
    validateInputs();
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = element.id === 'username' ? usernameError : passwordError;

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success');
    validity[element.id] = false;
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = element.id === 'username' ? usernameError : passwordError;

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
    validity[element.id] = true;
};

const validateInputs = () => {
    const usernameValue = username.value.trim();
    const passwordValue = password.value.trim();
    if(usernameValue === '') {
        setError(username, 'Username is required');
    } else {
        setSuccess(username);
    }

    if(passwordValue === '') {
        setError(password, 'Password is required');
    }
    else{
        setSuccess(password);
    }

    if (Object.values(validity).every(value => value)) {
        submitForm();
    }
}

const submitForm = () => {
    const formData = new FormData(form);
    fetch('/login/', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            // Redirect to the home page
            window.location.href = '/';  // Redirect to the home page
        } else {
            // Handle failed login (e.g., display error message)
            console.error('Login failed');
            // You can display an error message to the user here
        }
    })
    .catch(error => {
        console.error('Error occurred during login:', error);
        // Handle error (e.g., display error message)
    });
};
