let input_weight = document.getElementsByName('weight')[0];
let input_description = document.getElementsByName('description')[0];
let input_image_one = document.getElementsByName('image_one')[0];
let input_image_two = document.getElementsByName('image_two')[0];
let description_label = input_description.previousElementSibling;
let image_one_label = input_image_one.previousElementSibling;
let image_two_label = input_image_two.previousElementSibling;

function check_input() {
    if (input_weight.value){
        input_description.style.display = 'block';
        description_label.style.display = 'block';
    } else {
        input_description.style.display = 'none';
        description_label.style.display = 'none';
        input_image_one.style.display = 'none';
        input_image_two.style.display = 'none';
        image_one_label.style.display = 'none';
        image_two_label.style.display = 'none';
    }
}

function check_input_two() {
    if (input_description.value) {
        input_image_one.style.display = 'block';
        image_one_label.style.display = 'block';
    }
}

function check_input_any() {
    if (input_image_one.value) {
        input_image_two.style.display = 'block';
        image_two_label.style.display = 'block';
    }
}

check_input();

input_weight.addEventListener('change', function (e) {
    check_input();
})
input_description.addEventListener('change', function (e) {
    check_input_two();
})
input_image_one.addEventListener('change', function (e) {
    check_input_any();
})