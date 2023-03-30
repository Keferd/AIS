async function loadSto(url){
    const response = await fetch(url);
    const STORAGE = await response.json();
    console.log(STORAGE);

    let admin_storage_btn = document.querySelector("#admin__storage");

    admin_storage_btn.addEventListener("click", function (e) {
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
                <th>ID of Ingredient</th>
                <th>Date</th>
                <th>Count</th>
            </tr>
        `;

        for (let id in STORAGE){
            table.innerHTML += `
                <tr>
                    <td>` + STORAGE[id]['id'] + `</td>
                    <td>` + STORAGE[id]['id_ingredient'] + `</td>
                    <td>` + STORAGE[id]['date'] + `</td>
                    <td>` + STORAGE[id]['count'] + `</td>
                </tr>
            `;
        }

            
    });
}
let url2 = 'http://127.0.0.1:8000/api/storages';
const STORAGE =loadSto(url2);