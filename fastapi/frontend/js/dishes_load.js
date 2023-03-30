async function loadDis(url){
    const response = await fetch(url);
    const DISHES = await response.json();
    console.log(DISHES);

    let admin_dishes_btn = document.querySelector("#admin__dishes");

    admin_dishes_btn.addEventListener("click", function (e) {
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
            </tr>
        `;

        for (let id in DISHES){
            table.innerHTML += `
                <tr>
                    <td>` + DISHES[id]['id'] + `</td>
                    <td>` + DISHES[id]['name'] + `</td>
                </tr>
            `;
        }

            
    });
}
let url1 = 'http://127.0.0.1:8000/api/dishes';
const DISHES =loadDis(url1);