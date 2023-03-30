const xhr = new XMLHttpRequest();
const url = 'http://127.0.0.1:8000/api/dishes'; // URL сервера, откуда получаем данные

xhr.open('GET', url); // настройка запроса
xhr.responseType = 'json'; // указываем, что ожидаем ответ в формате JSON

xhr.onload = function() {
  if (xhr.status === 200) { // если ответ успешный
    const data = xhr.response; // данные, полученные с сервера
    const MENU = JSON.parse(JSON.stringify(data)); // преобразование данных в объект JavaScript
    console.log(MENU);  // данные, полученные с сервера
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
            Меню
        </h1>
    `;

    let field = document.getElementById("menu__field");
    
    for (let id in MENU){
        field.innerHTML += `
            <div class="menu__product" id="` + MENU[id]['id'] + `">
                <img class="menu__item-img" src="img/` + MENU[id]['id'] + `.jpg" alt="img.jpg">
                <div class="menu__details">
                    <div class="manu__name">
                        ` + MENU[id]['name'] + `
                    </div>
                    <div class="manu__ctrl-panel">
                        <div class="manu__btn">+</div>
                        <div class="menu__value">0</div>
                        <div class="manu__btn__dec">-</div>                      
                        
                    </div>
                </div>
            </div>
        `;
    }
     // выводим данные в консоль
  } else {
    console.error('Ошибка при получении данных:', xhr.statusText); // если ответ неудачный, выводим сообщение об ошибке
  }
};
xhr.send(); 


document.addEventListener("DOMContentLoaded", () => {
    

        
});// отправ этом примере мы создаем объект XMLHttpRequest, настраиваем его для GET запроса на указанный сервер, указываем, что ожидаем ответ в формате JSON, и отправляем запрос на сервер. При получении ответа выполняется функция onload, в которой мы проверяем успешность ответа и получаем данные с помощью свойства response объекта XMLHttpRequest. Если ответ неудачный, выводим сообщение об ошибке.





