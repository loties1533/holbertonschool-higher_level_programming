#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    """
    récupère tous les posts depuis 'JSONPlaceholder' et affiche leur titres

    - posts = liste de dictionnaires chaque dict représentant un post + clés
        - 'id' = identifiant du post
        - 'title' = titre du post
        - 'body' = contenu du post
    """
    Response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {Response.status_code}")
    if Response.status_code == 200:
        posts = Response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Récupe tous les posts depuis 'JSONPlaceholder'
    et les enregistre dans 'posts.csv'

    posts.csv = un fichier CSV créé automatiquement avec les colonne 'id'
    'title'et 'body'
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()

        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            colonne_csv = ['id', 'title', 'body']
            monfichiercsv = csv.DictWriter(f, fieldnames=colonne_csv)

            monfichiercsv.writeheader()

            for post in posts:
                monfichiercsv.writerow({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })
