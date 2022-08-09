function validateSignupForm(){
    if (!validateEmail() || !validatePasswords()){
        return false;
    }
}