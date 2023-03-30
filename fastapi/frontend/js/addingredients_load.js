let admin_addingredients_btn = document.querySelector("#admin__addingredients");

admin_addingredients_btn.addEventListener("click", function (e) {
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
            <div class="admin__form">
                <h1 class="admin__h1">Добавление ингредиента</h1>
                <input class="admin__input" type="text" id="admin__input_ingredient" placeholder="Название ингредиента">
                <input class="admin__submit" type="submit" id="admin__submit_ingredient">
            </div>
        </div>
    `;

    let ingredient_button = document.getElementById('admin__submit_ingredient');

    ingredient_button.addEventListener('click',function(){
        const jsonObject = {};
        let ing_field = document.getElementById('admin__input_ingredient');        
            jsonObject['name']=ing_field.value;
            jsonObject['count']=0;
            if(ing_field.value.length > 0){
                
                console.log(jsonObject);
                const requestOptions = {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({'name':ing_field.value,'count':0})
                };
                fetch('http://127.0.0.1:8000/api/ingredient', requestOptions)
                    .then(response => response.json())
                    .then(data => console.log(data))
                    .catch(error => console.error(error));
                ing_field.value='';
            }
            else{
                //ing_field.placeholder='Ошибкаааа!';
            }
            
           
    });
});