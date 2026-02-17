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


import requests

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
#!/usr/bin/python3
"""
Module pour l'exercice RESTful API Holberton
"""

import requests
import csv

def fetch_and_print_posts():
    """
    Récupère tous les posts de JSONPlaceholder et affiche leurs titres.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Récupère tous les posts et les sauvegarde dans posts.csv
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })
