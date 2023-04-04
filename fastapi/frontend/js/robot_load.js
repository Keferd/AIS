async function loadRo(url){
    const response = await fetch(url);
    const ROBOT = await response.json();
    console.log(ROBOT);

    const response2 = await fetch('http://127.0.0.1:8000/api/ingredients');
    const INGREDIENTS = await response2.json();
    console.log(INGREDIENTS);

let admin_robot_btn = document.querySelector("#admin__robot");

admin_robot_btn.addEventListener("click", function (e) {
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
            <th>Привезти</th>
            <th>Сколько</th>
        </tr>
    `;

    for (let id in ROBOT){
        table.innerHTML += `
            <tr>
                <td> Привези: ` + INGREDIENTS[ROBOT[id]['id_ingredient']]['name'] + `</td>
                <td>` + ROBOT[id]['count'] + `</td>
            </tr>
        `;
    }

        
});
}
let url3 = 'http://127.0.0.1:8000/api/storages';
const ROBOTS =loadRo(url3);