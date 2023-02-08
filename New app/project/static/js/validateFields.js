function validateUsername(){
    var username = $('#username').val();
    var usernameError = $('#error_username');

    if (username.length == 0){
        usernameError.html('Username is required');
        $("#username").addClass("error");
        return false;
    }

    usernameError.html('');
    $("#username").removeClass("error");
    return true;
}


function validateEmail(){
    var email = $('#email').val();
    var emailError = $('#error_email');

    if (email.length == 0){
        emailError.html('Email is required');
        $("#email").addClass("error");
        return false;
    }

    if (!email.match(/^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/)){
        emailError.html('Email is invalid');
        $("#email").addClass("error");
        return false;
    }

    emailError.html('');
    $("#email").removeClass("error");
    return true;
}


function validatePassword(){
    var password = $('#password').val();
    var passwordError = $('#error_password');
    
    if (password.length == 0){
        passwordError.html('Password is required');
        $("#password").addClass("error");
        return false;
    }

    passwordError.html('');
    $("#password").removeClass("error");
    return true;
}


function validatePasswords(){
    var password = $('#password').val();
    var confirm_password = $('#confirm_password').val();
    var passwordError = $('#error_password');
    
    if (password.length == 0 || confirm_password.length == 0){
        passwordError.html('Password is required');
        $("#password").addClass("error");
        $("#confirm_password").addClass("error");
        return false;
    }

    if (password != confirm_password){
        passwordError.html("Passwords don't match");
        $("#password").addClass("error");
        $("#confirm_password").addClass("error");
        return false;
    }

    passwordError.html('');
    $("#password").removeClass("error");
    $("#confirm_password").removeClass("error");
    return true;
}


function validateMobileNumber(){
    var mobile_number = $('#mobile_number').val();
    var mobile_numberError = $('#error_mobile_number');

    if (mobile_number.length == 0){
        mobile_numberError.html('Mobile number is required');
        $("#mobile_number").addClass("error");
        return false;
    }
    
    if (mobile_number.length != 10){
        mobile_numberError.html('Mobile number should be ten digits');
        $("#mobile_number").addClass("error");
        return false;
    }

    if (!mobile_number.match(/^[6-9]\d{9}$/)){
        mobile_numberError.html('This mobile number is invalid');
        $("#mobile_number").addClass("error");
        return false;
    }

    mobile_numberError.html('');
    $("#mobile_number").removeClass("error");
    return true;
}

