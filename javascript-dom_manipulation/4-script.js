const addItemDiv = document.getElementById('add_item');
const myList = document.querySelector('ul.my_list');

function addItem () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  myList.appendChild(newItem);
}

addItemDiv.addEventListener('click', addItem);
