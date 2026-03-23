document.addEventListener('DOMContentLoaded', function () {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const helloElem = document.getElementById('hello');

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      helloElem.textContent = data.hello;
    });
});
