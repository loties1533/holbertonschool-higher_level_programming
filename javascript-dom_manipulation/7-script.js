const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listMoviesUl = document.getElementById('list_movies');

fetch(url)
  .then(response => response.json())
  .then(data => {
    data.results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      listMoviesUl.appendChild(listItem);
    });
  });
