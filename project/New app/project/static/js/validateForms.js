function validateLoginForm(){
    if (!validateEmail() || !validatePasswords()){
        return false;
    }
}

function validateSignupForm(){
    if (!validateEmail() || !validatePasswords()){
        return false;
    }
}

function validateCredential(){
    if (!validateMobileNumber()){
        return false;
    }
}
