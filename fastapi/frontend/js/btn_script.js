const parent = document.querySelector('#menu__field');

// Добавляем обработчик события на родительский элемент
parent.addEventListener('load', function(event) {
  // Проверяем, что событие произошло на элементе, который нас интересует
  if (event.target.matches('manu__btn')) {
    const elements = document.querySelectorAll('.manu__btn');

// Добавляем обработчик клика для каждого элемента
    elements.forEach(function(element) {
    element.addEventListener('click', function() {
        const valueElement = document.querySelector('#menu__value');
        // Изменяем значение только у элемента, на который был клик
        valueElement.innerHTML = '1';
    });
    });
    // Делаем что-то с дочерним элементом, например, выводим его текстовое содержимое в консоль
    // const valueElement = document.querySelector('#menu__value');
    // const value = 1;
    // value++; // увеличиваем значение
    // valueElement.textContent = value;
  }
});

