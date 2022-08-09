function validateLoginForm(){
    if (!validateEmail() || !validatePassword()){
        return false;
    }
}