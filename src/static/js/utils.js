function getCookie(cname) {
    let name = cname + '=';
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) === 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function loader(){

    let spinner = Swal.fire({
        title: 'Carregando...',
        text: 'Estamos processando sua solicitação.',
        allowOutsideClick: false,
        didOpen: () => {
            Swal.showLoading();
        }
    });

    return spinner;
    
}

$(document).ready(function() {
    $('.dropdown-toggle').click(function() {
        $(this).next('.dropdown-menu').toggle(); // Alterna a visibilidade do menu
    });
});