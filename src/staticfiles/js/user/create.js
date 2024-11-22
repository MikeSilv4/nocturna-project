function register(){

    let form = document.getElementById("formId");

    if (!form.checkValidity()) {

        if (!emailField.validity.valid) {
            Swal.fire({
                title: "Erro",
                text: "Por favor, insira um e-mail válido.",
                icon: "error"
            });
        }
        else{
            Swal.fire({
                title: "Erro",
                text: "Por favor, revise as informações.",
                icon: "error"
            });
        }

        return;
    }

    if(document.getElementById("user_password_1").value != document.getElementById("user_password_2").value){
        Swal.fire({
            title: "Erro",
            text: "Senhas divergentes",
            icon: "error"
        }); 
        return;
    }

    let data = getData();
    console.log(data);
    const url = new URL('/api/user/', window.location.origin);

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
            body: JSON.stringify(data)  
    })
    .then((response) => {
        if(response.ok){
            window.location.href = `${window.location.origin}/dash/home/`;
        }else{
            return response.json();
        }
    })
    .then((data) => {
        if (data) {
            Swal.fire({
                title: "Erro",
                text: data.details,
                icon: "error"
            });
        }
    })
    .catch((error) => {
        console.log(error);
    });

}

function getData(){

    let email = document.getElementById("user_email").value;
    let first_name = document.getElementById("user_first_name").value;
    let last_name = document.getElementById("user_last_name").value;
    let password = document.getElementById("user_password_1").value;
    let cpf = document.getElementById("user_cpf").value;
    cpf = cpf.replace(/[.-]/g, '');
    let born_date = document.getElementById("user_born_date").value;

    return {email, first_name, last_name, password, cpf, born_date};

}

document.getElementById('user_cpf').addEventListener('input', function(e) {
    var cpf = e.target.value.replace(/\D/g, '');
    cpf = cpf.replace(/(\d{3})(\d)/, '$1.$2');
    cpf = cpf.replace(/(\d{3})(\d)/, '$1.$2');
    cpf = cpf.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
    e.target.value = cpf;
  });