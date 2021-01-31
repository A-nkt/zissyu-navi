var textbox_element = document.getElementById('footer-year');

var new_element = document.createElement('p');
let d = new Date();
let year = d.getFullYear();
new_element.textContent = '実習ナビ ©' + year;

textbox_element.appendChild(new_element);
