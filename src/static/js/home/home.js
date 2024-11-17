function goview(){
    window.location.href = window.location.origin + "/dash/user/view/";
}

function logout(){

    let data = getData();
    console.log(data);
    const url = new URL('/api/user/login/logout_user', window.location.origin);

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
                window.location.href = `${window.location.origin}/dash/user/login`;
            }
            else{
                Swal.fire({
                    title: "Erro",
                    text: "E-mail/Senha invalida",
                    icon: "error"
                });
            }
        })
        .catch((error) => {
            console.log('nok');
        });

}

function getData(){

    let username = document.getElementById("user_email").value;
    let password = document.getElementById("user_password").value;

    return {username, password};

}