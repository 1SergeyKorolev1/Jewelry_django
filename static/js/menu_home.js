// Получаем элемент с id "menu_home"
var menuHome = document.getElementById('menu_home');

// Находим все дочерние элементы (блоки) внутри этого элемента
var blocks = menuHome.children;

// Перебираем дочерние элементы и добавляем класс "menu home"
for (var i = 0; i < blocks.length; i++) {
    blocks[i].classList.add('menu_home');
}