function deleteuser(){

    let data = getDataDelete();
    console.log(data);
    const url = new URL('/api/user/login/' + data + '/', window.location.origin);
    console.log(url);

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