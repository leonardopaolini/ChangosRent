document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('loginForm');
    form.addEventListener('submit', function(event) {
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
            validateUsername();
            validatePassword();
        }
    });

    function validateUsername() {
        const usernameInput = document.getElementById('username');
        const usernameError = document.getElementById('usernameError');
        if (!usernameInput.validity.valid) {
            if (usernameInput.validity.valueMissing) {
                usernameError.textContent = 'Por favor ingrese su usuario';
            }
        } else {
            usernameError.textContent = '';
        }
    }

    function validatePassword() {
        const passwordInput = document.getElementById('password');
        const passwordError = document.getElementById('passwordError');
        if (!passwordInput.validity.valid) {
            if (passwordInput.validity.valueMissing) {
                passwordError.textContent = 'Por favor ingrese su contraseña';
            }
        } else {
            passwordError.textContent = '';
        }
    }
    document.getElementById('username').addEventListener('input', validateUsername);
    document.getElementById('password').addEventListener('input', validatePassword);
});