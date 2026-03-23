const header = document.querySelector('header');
const redHeaderDiv = document.getElementById('red_header');

function AddRedClass () {
  header.classList.add('red');
}
redHeaderDiv.addEventListener('click', AddRedClass);
