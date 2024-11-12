function login(){

    let data = getData();
    
    const url = new URL('/api/login/', window.location.origin);
  
fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify(data)  
    })
    .then((response) => {
        console.log('ok');
    })
    .catch((error) => {
        console.log('nok');
    });

}

function getData(){

    let username = document.getElementById("user_email");
    let password = document.getElementById("user_password");

    return {username, password};

}