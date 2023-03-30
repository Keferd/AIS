async function loadOrd(url){
    const response =await  fetch(url);
    const ORDERS = await response.json();
    console.log(ORDERS);

    let admin_orders_btn = document.querySelector("#admin__orders");

    admin_orders_btn.addEventListener("click", function (e) {
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
                <th>Date</th>
            </tr>
        `;

        for (let id in ORDERS){
            table.innerHTML += `
                <tr>
                    <td>` + ORDERS[id]['id'] + `</td>
                    <td>` + ORDERS[id]['date'] + `</td>
                </tr>
            `;
        }

            
    });
}

let urls = 'http://127.0.0.1:8000/api/orders';
const ORDRS = loadOrd(urls);
