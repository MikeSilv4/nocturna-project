window.onload = function(){
    accountdata();
}

function accountdata{
    const user = JSON.parse(sessionStorage.getItem("user"));
    console.log(user);
}

function backhome(){
    window.location.href = "../../home/";
}