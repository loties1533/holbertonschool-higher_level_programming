| GET     | Récupère des données | `GET /posts` ou `GET /posts/1` |
| POST    | Envoie des données pour créer une ressource | `POST /posts` avec un body JSON pour créer un nouveau post 
| PUT     | Met à jour complètement une ressource existante | `PUT /posts/1` avec un body JSON pour remplacer le post 
| PATCH   | Met à jour partiellement une ressource | `PATCH /posts/1` avec un body JSON partiel 
| DELETE  | Supprime une ressource | `DELETE /posts/1` 


curl -X POST https://jsonplaceholder.typicode.com/posts \
-H "Content-Type: application/json" \
-d '{"title":"Presentation","body":"contenue de ma presentation","userId":1}'

200	OK - La requête a réussi	GET /posts/1 retourne le post demandé
201	Created - Une ressource a été créée	POST /posts retourne le post créé
400	Bad Request - Requête mal formée	POST /posts avec JSON invalide
404	Not Found - Ressource inexistante	GET /posts/999999 pour un post qui n’existe pas
500	Internal Server Error - Erreur serveur	Généralement une erreur serveur, simulée rarement par JSONPlaceholder

exemple : curl -i https://jsonplaceholder.typicode.com/posts/999999  --> renvoi : HTTP/1.1 404 Not Found

`curl` est un outil en ligne de commande pour **envoyer des requêtes HTTP**.

Avec `curl`, tu peux :

- Demander une page (`GET`)
- Envoyer des données (`POST`)
- Tester tes API rapidement sans front-end
