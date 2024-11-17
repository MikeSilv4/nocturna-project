function alteruser(){

    let data = getDataAlter();
    console.log(data);

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
            window.location.href = `${window.location.origin}/dash/user/login/`;
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

function getDataAlter(){

    let first_name = document.getElementById("user_firstname").value;
    let last_name = document.getElementById("user_lastname").value;
    let born_date = document.getElementById("user_borndate").value;
    let password = document.getElementById("user_password").value;

    return {first_name, last_name, born_date, password};
}

function deleteuser(){

    let data = getDataDelete();
    console.log(data);
    const url = new URL("/api/user/login/" + data["id"] + "/", window.location.origin);

fetch(url, {
    method: 'DELETE',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
    },
        body: JSON.stringify(data)
    })
    .then((response) => {
        if(response.ok){
            window.location.href = `${window.location.origin}/dash/user/login/`;
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

function getDataDelete(){

    let id = document.getElementById("user_id").value;

    return {id};
}

function backhome(){
    window.location.href = window.location.origin + "/dash/home/";
}