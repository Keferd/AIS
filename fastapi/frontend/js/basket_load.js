const BASKET = [{
    id: 1,
    name: 'Капуста с картошкой'
},   
{
    id: 2,
    name: 'Картошка с курицей'
},   
{
    id: 3,
    name: 'Курица с капустой'
}
];

document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#menu__field").innerHTML = `
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

    document.getElementById("menu__field").innerHTML = `
        <h1 class="menu__h1">
            Корзина
        </h1>
    `;

    let field = document.getElementById("menu__field");
    
    for (let id in BASKET){
        field.innerHTML += `
            <div class="menu__product" id="` + BASKET[id]['id'] + `">
                <img class="menu__item-img" src="img/` + BASKET[id]['id'] + `.jpg" alt="img.jpg">
                <div class="menu__details">
                    <div class="manu__name">
                        ` + BASKET[id]['name'] + `
                    </div>
                    <div class="manu__ctrl-panel">
                        <div class="manu__btn">+</div>
                        <div class="menu__value">0</div>
                        <div class="manu__btn">-</div>
                    </div>
                </div>
            </div>
        `;
    }

        
});