function requestNewPassword(){

    let form = document.getElementById("formId");

    if (!form.checkValidity()) {

        Swal.fire({
            title: "Erro",
            text: "Por favor, preencha o campo E-mail.",
            icon: "error"
        });

        return;
    }

    const spinner = loader();

    let data = getData();
    const url = new URL('/api/user/forgot-password/', window.location.origin);

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
            body: JSON.stringify(data)  
    })
    .then((response) => {

        spinner.close();

        if(response.ok){
            Swal.fire({
                title: "Sucesso",
                text: "Um e-mail foi encaminhado com uma senha provisoria",
                icon: "success"
            });
        }else{
            Swal.fire({
                title: "Erro",
                text: "Não existe usuário com esse e-mail",
                icon: "error"
            });
        }
    })
    .catch((error) => {
        spinner.close();
        console.log(error);
    });

}

function getData(){

    let email = document.getElementById("user_email").value;

    return {email};

}