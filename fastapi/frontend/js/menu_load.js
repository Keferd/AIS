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
        let value=localStorage.getItem(MENU[id]['id']);
        let huk=0;
        if(value!=null){
            huk=value;
        }
        field.insertAdjacentHTML('beforeend',`
            <div class="menu__product" id="` + MENU[id]['id'] + `">
                <img class="menu__item-img" src="img/` + MENU[id]['id'] + `.jpg" alt="img.jpg">
                <div class="menu__details">
                    <div class="manu__name">
                        ` + MENU[id]['name'] + `
                    </div>
                    <script src="js/btn_script.js"></script>
                    <div class="manu__ctrl-panel">
                        <div class="manu__btn" >+</div>
                        <div class="menu__value">`+huk+`</div>
                        <div class="manu__btn__dec">-</div>                     
                        
                    </div>
                </div>
            </div>
        `);
        
    }
    for (let id in MENU){
        let menu__item = document.getElementById(MENU[id]['id']);
        let button_inc = menu__item.querySelector('.manu__btn');
        let button_dec = menu__item.querySelector('.manu__btn__dec');
        // = menu__item.querySelector('.menu__value');
        //let value=parseInt(value_field.textContent);
        button_inc.addEventListener('click',function() {
            console.log('Нажата новая кнопка '+MENU[id]['id']);
            let value_field=button_inc.parentElement.querySelector('.menu__value')
            let value = parseInt(value_field.textContent);
            value_field.innerHTML=(value+1);
            localStorage.setItem(MENU[id]['id'],value+1);
        });
        button_dec.addEventListener('click',function() {
            console.log('Нажата новая кнопка '+MENU[id]['id']);
            let value_field=button_dec.parentElement.querySelector('.menu__value')
            let value = parseInt(value_field.textContent);
            if(value>0){
                value_field.innerHTML=(value-1);
                localStorage.setItem(MENU[id]['id'],value-1);
            }
        });
    }
    // document.querySelector('manu__btn').addEventListener('click', function() {
    //     alert('Нажата новая кнопка');
    // });
     // выводим данные в консоль
  } else {
    console.error('Ошибка при получении данных:', xhr.statusText); // если ответ неудачный, выводим сообщение об ошибке
  }
};
xhr.send(); 


document.addEventListener("DOMContentLoaded", () => {
    

        
});// отправ этом примере мы создаем объект XMLHttpRequest, настраиваем его для GET запроса на указанный сервер, указываем, что ожидаем ответ в формате JSON, и отправляем запрос на сервер. При получении ответа выполняется функция onload, в которой мы проверяем успешность ответа и получаем данные с помощью свойства response объекта XMLHttpRequest. Если ответ неудачный, выводим сообщение об ошибке.

let order_button = document.getElementById('order-btn');
order_button.addEventListener('click',function() {
    //console.log(localStorage);
    const jsonObject = {};
    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        const value = localStorage.getItem(key);
        if(value>0&&value<30&&Number.isInteger(parseInt(key))){
            jsonObject[key]=value;
            localStorage.setItem(key,0);
        }
        //console.log(`Ключ: ${key}, Значение: ${value}`);
    }
    //if(jsonObject.length==0){
        console.log(jsonObject);
        
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ dishes: jsonObject})
        };
        fetch('http://127.0.0.1:8000/api/order', requestOptions)
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error(error));
   // }
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
            let value=localStorage.getItem(MENU[id]['id']);
            let huk=0;
            if(value!=null){
                huk=value;
            }
            field.insertAdjacentHTML('beforeend',`
                <div class="menu__product" id="` + MENU[id]['id'] + `">
                    <img class="menu__item-img" src="img/` + MENU[id]['id'] + `.jpg" alt="img.jpg">
                    <div class="menu__details">
                        <div class="manu__name">
                            ` + MENU[id]['name'] + `
                        </div>
                        <script src="js/btn_script.js"></script>
                        <div class="manu__ctrl-panel">
                            <div class="manu__btn" >+</div>
                            <div class="menu__value">`+huk+`</div>
                            <div class="manu__btn__dec">-</div>                     
                            
                        </div>
                    </div>
                </div>
            `);
            
        }
        for (let id in MENU){
            let menu__item = document.getElementById(MENU[id]['id']);
            let button_inc = menu__item.querySelector('.manu__btn');
            let button_dec = menu__item.querySelector('.manu__btn__dec');
            // = menu__item.querySelector('.menu__value');
            //let value=parseInt(value_field.textContent);
            button_inc.addEventListener('click',function() {
                console.log('Нажата новая кнопка '+MENU[id]['id']);
                let value_field=button_inc.parentElement.querySelector('.menu__value')
                let value = parseInt(value_field.textContent);
                value_field.innerHTML=(value+1);
                localStorage.setItem(MENU[id]['id'],value+1);
            });
            button_dec.addEventListener('click',function() {
                console.log('Нажата новая кнопка '+MENU[id]['id']);
                let value_field=button_dec.parentElement.querySelector('.menu__value')
                let value = parseInt(value_field.textContent);
                if(value>0){
                    value_field.innerHTML=(value-1);
                    localStorage.setItem(MENU[id]['id'],value-1);
                }
            });
        }
        // document.querySelector('manu__btn').addEventListener('click', function() {
        //     alert('Нажата новая кнопка');
        // });
            // выводим данные в консоль
        } else {
        console.error('Ошибка при получении данных:', xhr.statusText); // если ответ неудачный, выводим сообщение об ошибке
        }
    };
    xhr.send(); 
    // localStorage.clear();

    //location.reload();
});



