# JavaScript DOM manipulation

En JavaScript, on peut réagir aux événements d’un élément (comme un clic) en utilisant addEventListener. Il existe deux manières principales de définir la fonction qui sera exécutée : 

## exemple T1

**Fonction nommée (function)**

function maFonction() {
  // code à exécuter lors de l'événement
}

element.addEventListener('click', maFonction);
Crée une fonction séparée, réutilisable.
Syntaxe classique, compatible avec toutes les versions de JavaScript.

**Fonction fléchée (arrow function)**

element.addEventListener('click', () => {
  // code à exécuter lors de l'événement
});
Écrite directement dans addEventListener.
Plus compacte et moderne.
Pratique pour des fonctions courtes ou non réutilisées.

Résumé : Les deux méthodes exécutent le même code lors de l’événement. Le choix dépend surtout de la lisibilité et de la réutilisabilité.

[ Utilisateur clique ]
          │
          ▼
   +----------------+
   |  Element clic  |  ← ex: <div id="red_header">
   +----------------+
          │ addEventListener('click', fonction)
          ▼
   +----------------+
   |  Fonction JS   |  ← ex: changeColor() ou () => { ... }
   +----------------+
          │
          ▼
   +----------------+
   |  Element cible |  ← ex: <header>
   |  style modifié |
   +----------------+