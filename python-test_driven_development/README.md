Python - Développement piloté par les tests


## Workflow TDD

1. **Écrire les tests en premier**  
   - Créer un fichier `.txt` dans `tests/`  
   - Définir tous les cas valides et invalides avec **doctest**

2. **Écrire le module Python**  
   - Ajouter un **docstring** au module  
   - Ajouter un **docstring** à chaque fonction décrivant :
     - Description  
     - Paramètres et types  
     - Type de retour  
     - Exceptions levées  
     - Exemples doctest  

3. **Exécuter les tests**  
```bash
python3 -m doctest ./tests/*
python3 -m doctest -v ./tests/*


# Lancer tous les doctests
python3 -m doctest ./tests/*

# Lancer doctest avec détails
python3 -m doctest -v ./tests/*

# Vérifier les docstrings
python3 -c 'print(__import__("nom_module").__doc__)'
python3 -c 'print(__import__("nom_module").ma_fonction.__doc__)'

# Vérifier le style
pycodestyle nom_module.py

# Exécuter le fichier main
./