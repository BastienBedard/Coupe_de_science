# Défi prog 2025

Le fichier main gère l'affichage de pygame et des boutons.
Le fichier exploration_class gère le jeu en soit et les commandes qui rendent le jeu fonctionnel.
Le fichier scores sert a gérer l'écriture et la lecture du fichier json des scores.

Le fichier zone de jeu est le seul fichier qui doit être modifier par le joueur, il permait de donner au jeu les informations nécessaire au déroulement de la partie.

# How to play

Dans zone_de_jeu vous inquez votre numéro d'équipe et le niveau que vous désirer tanter, puis vous donner la list des coups que vous désirez jouer pour ce niveau.

Les coups possibles sont:

'avant' : Fait avancer le vaisseau d'une case vers l'avant.
'tdroite' : Fait tourner le vaisseau sur lui même vers la droite.
'tgauche' : Fait tourner le vaisseau sur lui même vers la gauche.

Il est possible de faire des boucles:
