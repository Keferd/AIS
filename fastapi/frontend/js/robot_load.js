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
            <th>ID</th>
            <th>CHTO</th>
        </tr>
    `;

    for (let id in ROBOT){
        table.innerHTML += `
            <tr>
                <td>` + ROBOT[id]['id'] + `</td>
                <td>` + ROBOT[id]['chto'] + `</td>
            </tr>
        `;
    }

        
});