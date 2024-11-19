function go_view_account(){

    window.location.href = window.location.origin + "/dash/user/view-account/";

}

function logout_account(){

    const url = new URL('/api/user/login/logout_user/', window.location.origin);
    console.log(url);
    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
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