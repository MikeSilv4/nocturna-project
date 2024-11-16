function showData(){

    let first_name = document.getElementById("user_firstname").value;
    let last_name = document.getElementById("user_lastname").value;
    let born_date = document.getElementById("user_borndate").value;
    let cpf = document.getElementById("user_cpf").value;
    let email = document.getElementById("user_email").value;
    let username = document.getElementById("user_username").value;
    let password = document.getElementById("user_password").value;

    return {first_name, last_name, born_date, cpf, email, username, password};

}