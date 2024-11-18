function login(){

    let form = document.getElementById("formId");

    if (!form.checkValidity()) {

        Swal.fire({
            title: "Erro",
            text: "Por favor, preencha os campos de E-mail e senha.",
            icon: "error"
        });

        return;
    }

    let data = getData();
    const url = new URL('/api/user/login/', window.location.origin);
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
            window.location.href = `${window.location.origin}/dash/home/`;
        }else{
            Swal.fire({
                title: "Erro",
                text: "Login/Senha invalida",
                icon: "error"
            });
        }
    })
    .catch((error) => {
        console.log(error);
    });

}

function getData(){

    let username = document.getElementById("user_email").value;
    let password = document.getElementById("user_password").value;

    return {username, password};

}