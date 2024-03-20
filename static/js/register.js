const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');
const phone_number = document.getElementById('password2');

const validity = {
    username: false,
    email: false,
    password: false,
    password2: false,
};

form.addEventListener('submit', e => {
    e.preventDefault();

    validateInputs();

    if (Object.values(validity).every(value => value)) {
        alert('Form submitted successfully!');

        function openuserlogin() {
            // You can replace 'https://example.com' with the URL of the page you want to open
            window.location.href = 'http://127.0.0.1:5500/login.html';

        }
        openuserlogin()

    }
});
const passwordInput = document.getElementById('password');
        const strengthResult = document.getElementById('strengthResult');

        passwordInput.addEventListener('input', function () {
            const password = this.value;
            const passwordStrength = checkPasswordStrength(password);
            strengthResult.innerText = `Password Strength: ${passwordStrength}`;
        });

        function checkPasswordStrength(password) {
            const minLength = 8;
    const hasUppercase = /[A-Z]/.test(password);
    const hasLowercase = /[a-z]/.test(password);
    const hasNumber = /\d/.test(password);
    const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);

    // Calculate the strength score based on criteria
    let strengthScore = 0;
    strengthScore += password.length >= minLength ? 1 : 0;
    strengthScore += hasUppercase ? 1 : 0;
    strengthScore += hasLowercase ? 1 : 0;
    strengthScore += hasNumber ? 1 : 0;
    strengthScore += hasSpecialChar ? 1 : 0;

    // Translate the score into a strength level
    if (strengthScore === 0) {
        return 'Very Weak';
    } else if (strengthScore === 1) {
        return 'Weak';
    } else if (strengthScore === 2) {
        return 'Moderate';
    } else if (strengthScore === 3) {
        return 'Strong';
    } else {
        return 'Very Strong';
    }


        }
const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')

    validity[element.id] = false;
}
const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');

    validity[element.id] = true;
};

const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@]+(\.[^<>()[\]\\.,;:\s@]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

const validateInputs = () => {
    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const password2Value = password2.value.trim();
    const phone_numberValue = phone_number.value.trim();
    if(usernameValue === '') {
        setError(username, 'Username is required');
    } else {
        setSuccess(username);
    }
    if(emailValue === '') {
        setError(email, 'Email is required');
    } else if (!isValidEmail(emailValue)) {
        setError(email, 'Provide a valid email address');
    } else {
        setSuccess(email);
    }

    if(passwordValue === '') {
        setError(password, 'Password is required');
     } else if (passwordValue.length <= 8 ) {
        setError(password, 'password is weak, try again')
    }
    else{
        setSuccess(password);
    }
    if(password2Value === '') {
        setError(password2, 'Please confirm your password');
    } else if (password2Value !== passwordValue) {
        setError(password2, "Passwords doesn't match");
    } else {
        setSuccess(password2);
    }

}


