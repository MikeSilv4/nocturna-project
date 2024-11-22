window.addEventListener('load', async function () {
    getItems();
});

var page = 1;
var total_items = null;

var filters = {
    limit : 20,
    offset : 0
}

function getItems(){

    const url = new URL('/api/item/items/', window.location.origin);
    
    url.searchParams.append('limit', filters.limit);
    url.searchParams.append('offset', filters.offset);
    console.log(url);
    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        } 
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {

        makeData(data.results);
        total_items = data.count;
        newPage();

        if(data.next){
            document.getElementById("next").disabled = false;
        }else{
            document.getElementById("next").disabled = true;
        }
        if(data.previous){
            document.getElementById("previous").disabled = false;
        }else{
            document.getElementById("previous").disabled = true;
        }
    })
    .catch((error) => {
        console.log(error);
    });

}

function makeData(data){

    let table = document.getElementById("table_content");
    table.innerHTML = "";

    data.forEach(element => {
        table.innerHTML += `
            <div class="col col-sm-3 col-md-3 mb-3">
                <div class="card">
                    <img src="${element.image}" class="card-img-top" alt="${element.name}">
                    <div class="card-body">
                        <h5 class="card-title">${element.name}</h5>
                        <p class="card-text">Preço: R$ ${element.value.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}</p>
                    </div>
                    <button class="product__buy--btn">Adicionar à sacola</button>
                </div>
            </div>
        `;
    });

}

function increaseFilter(){
    filters["offset"] = filters["offset"] + 20;
    page += 1;
    newPage();
    getItems();
}

function decreaseFilter(){
    filters["offset"] = filters["offset"] - 20;
    page -= 1;
    newPage();
    getItems();
}

function newPage(){
    document.getElementById("page").innerHTML = `${page}/${Math.floor(total_items/filters["limit"])}`;
}

function producViewModal(id){

}

document.getElementById("open_create_modal").addEventListener("click", function() {
    $("#create_item_modal").modal("show");
});
document.getElementById("close_create_item").addEventListener("click", function() {
    $("#create_item_modal").modal("hide");
});