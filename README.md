# xss-attack
Code utilisé pour démontrer l'attaque XSS (cross-site scripting) sur le site : altoromutual.com.
Ce travail est réalisé pour une présentation dans le cadre du cours d'introduction à la sécurité informatique.

## Scénario
- La victime essaie de se connecter au site de sa mutuelle. Un script a été injecté dans cette page.
- Lorsqu'elle tente de se connecter, son nom d'utilisateur et son mot de passe sont envoyés vers le serveur du hacker.
- Un message d'erreur apparaît et la (vraie) page de connexion charge.
- La victime peut désormais se connecter normalement sans savoir que ses données de connexion ont été volées.

## Comment reproduire l'attaque ?
1. Lancer le serveur python dans l'invite de commande : python listening-server.py.
2. Sur le site : altoromutual.com, copier le script dans la barre de recherche, et appuyer sur Enter.
3. Entrer un nom d'utilisateur et un mot de passe, puis appuyer sur Login.

Remarque :
- si index.html se trouve à l'emplacement : /usr/documents/index.html,
- le répertoire courant lorqu'on lance le serveur doit être : /usr/documents/
