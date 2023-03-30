async function loadIng(url){
    const response = await fetch(url);
    const INGREDIENTS = await response.json();
    console.log(INGREDIENTS);
    let admin_ingredients_btn = document.querySelector("#admin__ingredients");

admin_ingredients_btn.addEventListener("click", function (e) {
    document.querySelector("#admin__main").innerHTML = `
        <div class="admin__placeholder">
            <img src="img/loading.png" alt="loading..." class="loading-img">
            <style>
            .loading-img {
            width: 50px;
            height: 50px;
            animation: move 0.5s infinite linear;
            }
            
            @keyframes move {
            0% {
            transform: rotate(0deg);
            }
            50% {
            transform: rotate(180deg);
            border-radius: 50%;
            }
            100% {
            transform: rotate(360deg);
            }
            }
            </style>
        </div>
    `

    document.getElementById("admin__main").innerHTML = `
        <div class="admin__tablefield">
            <table class="admin__table" id="admin__table">
            </table>
        </div>
    `;

    let table = document.getElementById("admin__table");
    
    table.innerHTML += `
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Count</th>
        </tr>
    `;

    for (let id in INGREDIENTS){
        table.innerHTML += `
            <tr>
                <td>` + INGREDIENTS[id]['id'] + `</td>
                <td>` + INGREDIENTS[id]['name'] + `</td>
                <td>` + INGREDIENTS[id]['count'] + `</td>
            </tr>
        `;
    }

        
});
}
let url = 'http://127.0.0.1:8000/api/ingredients';
const INGREDIENTS =loadIng(url);

// fetch(url, {
//     method: 'GET',
//     headers: {
//         'Accept': 'application/json',
//     },
// })
//    .then(response => response.json())
//    .then(response => console.log(JSON.stringify(response)));

// let formdata = JSON.stringify({ id: id, name: name, count: count});
// let response =  fetch(url,
// {
//     method: "GET",
//     body: formdata,
//     headers: {
//         'Content-Type': 'application/json'
//     }
// })
// let INGREDIENTS = response;

