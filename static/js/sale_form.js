function check_input() {
    let input_material_value = document.getElementsByName('material')[0].value;
    let input_sample_gold = document.getElementsByName('sample_gold')[0];
    let input_sample_gold_label = input_sample_gold.previousElementSibling;
    let input_sample_silver = document.getElementsByName('sample_silver')[0];
    let input_sample_silver_label = input_sample_silver.previousElementSibling;
    let input_sample_platinum = document.getElementsByName('sample_platinum')[0];
    let input_sample_platinum_label = input_sample_platinum.previousElementSibling;
    if (input_material_value == 'silver' || input_material_value == 'platinum') {
        input_sample_gold.value = 'none';
        input_sample_gold_label.style.display = 'none';
        input_sample_gold.style.display = 'none';
    } else {
        input_sample_gold.style.display = 'block';
        input_sample_gold_label.style.display = 'block';
    }
    if (input_material_value == 'gold' || input_material_value == 'platinum') {
        input_sample_silver.value = 'none';
        input_sample_silver_label.style.display = 'none';
        input_sample_silver.style.display = 'none';
    } else {
        input_sample_silver.style.display = 'block';
        input_sample_silver_label.style.display = 'block';
    }
    if (input_material_value == 'silver' || input_material_value == 'gold') {
        input_sample_platinum.value = 'none';
        input_sample_platinum_label.style.display = 'none';
        input_sample_platinum.style.display = 'none';
    } else {
        input_sample_platinum.style.display = 'block';
        input_sample_platinum_label.style.display = 'block';
    }
}

check_input();


let input_material = document.getElementsByName('material')[0];
input_material.addEventListener('change', function (e) {
    check_input();
})