const updateHeaderDiv = document.getElementById('update_header');
const header = document.querySelector('header');

function updateHeader () {
  header.textContent = 'New Header!!!';
}

updateHeaderDiv.addEventListener('click', updateHeader);
