function delete_account(){

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
    const url = new URL('/api/user/login/' + data["id"] + "/", window.location.origin);
    console.log(url);
    fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
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

    let id = document.getElementById("user_id").value;

    return {id};

}

function back_home(){

    window.location.href = window.location.origin + "/dash/home/";

}