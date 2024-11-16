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
<<<<<<< HEAD
            window.location.href = `${window.location.origin}/dash/home/`;
=======
            window.location.href = `${window.location.origin}/dash/user/login/`;
>>>>>>> c17bebeb6da7246c8bd307ced5cb32b98661a676
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
    let last_name = document.getElementById("user_lastname").value;
    let born_date = document.getElementById("user_borndate").value;
    let cpf = document.getElementById("user_cpf").value;
    let email = document.getElementById("user_email").value;
    let password = document.getElementById("user_password").value;

    return {first_name, last_name, born_date, cpf, email, username, password};
}