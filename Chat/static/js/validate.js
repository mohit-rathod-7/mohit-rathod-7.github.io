function validateEmail(){
    var email = $('#email').val();
    var emailError = $('#error_email');

    if (email.length == 0){
        emailError.html('Email is required');
        $("#email").css("border", "1px solid red");
        return false;
    }

    if (!email.match(/^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/)){
        emailError.html('Email is invalid');
        $("#email").css("border", "1px solid red");
        return false;
    }

    emailError.html('');
    $("#email").css("border", "unset");
    return true;
}


function validatePassword(){
    var password = $('#password').val();
    var passwordError = $('#error_password');
    
    if (password.length == 0){
        passwordError.html('Password is required');
        $("#password").css("border", "1px solid red");
        return false;
    }

    passwordError.html('');
    $("#password").css("border", "unset");
    return true;
}


function validatePasswords(){
    var password_1 = $('#password_1').val();
    var password_2 = $('#password_2').val();
    var passwordError = $('#error_password');
    
    if (password_1.length == 0 || password_2.length == 0){
        passwordError.html('Password is required');
        $("#password_1").css("border", "1px solid red");
        $("#password_2").css("border", "1px solid red");
        return false;
    }

    if (password_1 != password_2){
        passwordError.html("Passwords don't match");
        $("#password_1").css("border", "1px solid red");
        $("#password_2").css("border", "1px solid red");
        return false;
    } 

    passwordError.html('');
    $("#password_1").css("border", "unset");
    $("#password_2").css("border", "unset");
    return true;
}