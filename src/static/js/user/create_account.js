function create_account(){

    let form = document.getElementById("formId");

    if (!form.checkValidity()) {

        Swal.fire({
            title: "Erro",
            text: "Por favor, preencha todos os campos necessários.",
            icon: "error"
        });

        return;
    }

    let data = getData();
    const url = new URL('/api/user/create/', window.location.origin);
    console.log(url);
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
            body: JSON.stringify(data)  
    })
    .then((response) => {
        console.log(response);
        if(response.ok){
            window.location.href = `${window.location.origin}/dash/user/login/`;
        }else{
            Swal.fire({
                title: "Erro",
                text: "Ocorreu um erro, por favor tente novamente.",
                icon: "error"
            });
        }
    })
    .catch((error) => {
        console.log(error);
    });

}

function getData(){

    let first_name = document.getElementById("user_first_name").value;
    let last_name = document.getElementById("user_last_name").value;
    let born_date = document.getElementById("user_born_date").value;
    let cpf = document.getElementById("user_cpf").value;
    let email = document.getElementById("user_email").value;
    let password = document.getElementById("user_password").value;

    return {first_name, last_name, born_date, cpf, email, password};

}

function back_login(){

    window.location.href = window.location.origin + "/dash/user/login/";

}