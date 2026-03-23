const header = document.querySelector('header');
const redheaderDiv = document.getElementById('red_header');

function changeHeaderColor () {
  header.style.color = '#FF0000';
}

redheaderDiv.addEventListener('click', changeHeaderColor);
