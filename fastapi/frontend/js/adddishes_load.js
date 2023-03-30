let admin_adddishes_btn = document.querySelector("#admin__adddishes");

admin_adddishes_btn.addEventListener("click", function (e) {
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
                <h1 class="admin__h1">Добавление блюда</h1>
                <input class="admin__input" type="text" id="admin__input_dishname" placeholder="Название блюда">
                <input class="admin__input" type="text" id="admin__input_dishing" placeholder="Ингредиенты">
                <input class="admin__submit" type="submit" id="admin__submit_dish">
            </div>
        </div>
    `;

    let ingredient_button = document.getElementById('admin__submit_dish');

    ingredient_button.addEventListener('click',function(){
        const jsonObject = {};
        let dish_name_field = document.getElementById('admin__input_dishname');   
        let dish_ings = document.getElementById('admin__input_dishing');     
            // jsonObject['name']=ing_field.value;
            // jsonObject['count']=0;
           // let jacon=JSON.parse(dish_ings);
            console.log(dish_name_field.value);
            var arrayOfStrings = dish_ings.value.split(',');
            
            console.log(arrayOfStrings);
            for (let i = 0; i < arrayOfStrings.length; i++) {
                var ing_count=arrayOfStrings[i].split(';');
                jsonObject[ing_count[0]]=ing_count[1];
            }
            console.log(jsonObject);

            if(dish_name_field.value.length > 0&&dish_ings.value.length>0){
                
                console.log(jsonObject);
                const requestOptions = {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({'name':dish_name_field.value,'ingredients':jsonObject})
                };
                fetch('http://127.0.0.1:8000/api/dish', requestOptions)
                    .then(response => response.json())
                    .then(data => console.log(data))
                    .catch(error => console.error(error));
                dish_name_field.value='';
                dish_ings.value='';
            }
            else{
                //ing_field.placeholder='Ошибкаааа!';
            }
            
           
    });

    
});