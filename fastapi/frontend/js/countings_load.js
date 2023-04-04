async function loadCount(url){
    const response = await fetch(url);
    const COUNTINGS = await response.json();
    console.log(COUNTINGS);

    const response2 = await fetch('http://127.0.0.1:8000/api/ingredients');
    const INGREDIENTS = await response2.json();
    console.log(INGREDIENTS);

    let admin_ingredients_btn = document.getElementById("admin__countings");

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
            <th>Название</th>
            <th>Значение</th>
        </tr>
    `;

    for (let id in COUNTINGS){
        table.innerHTML += `
            <tr>
                <td>` + COUNTINGS[id]['ingredient_id'] + `</td>
                <td>` + INGREDIENTS[COUNTINGS[id]['ingredient_id']]['name'] + `</td>
                <td>` + COUNTINGS[id]['delivery_count'] + `</td>
            </tr>
        `;
    }

        
});
}
let url67 = 'http://127.0.0.1:8000/api/countings';
const COUNTINGS =loadCount(url67);

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

