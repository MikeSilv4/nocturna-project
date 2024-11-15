function createuser(){

    let data = getData();
    console.log(data);
    const url = new URL('/api/user/create/', window.location.origin);
  
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
            window.location.href = `${window.location.origin}/dash/user/`;
        }else{
            Swal.fire({
                title: "Erro",
                icon: "error"
            });
        }
    })
    .catch((error) => {
        console.log('nok');
    });

}

function getData(){

    let first_name = document.getElementById("user_firstname").value;
    let last_name = document.getElementById("user_lastemail").value;
    let born_date = document.getElementById("user_borndate").value;
    let cpf = document.getElementById("user_cps").value;
    let email = document.getElementById("user_email").value;
    let username = document.getElementById("user_name").value;
    let password = document.getElementById("user_password").value;

    return {first_name, last_name, born_date, cpf, email, username, password};
}