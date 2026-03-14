# Défi prog 2025

Le fichier main gère l'affichage de pygame et des boutons.
Le fichier exploration_class gère le jeu en soit et les commandes qui rendent le jeu fonctionnel.
Le fichier gestion_scores sert a gérer l'écriture et la lecture du fichier json des scores. La commande à la fin du fichier permet d'afficher les scores.
Le fichier reset permet de remettre les scores à 0 et de réinitialiser le fichier zone de jeu.

Le fichier zone de jeu est le seul fichier qui doit être modifier par le joueur, il permait de donner au jeu les informations nécessaire au déroulement de la partie.

# Comment jouer

Dans zone_de_jeu vous indiquez votre numéro d'équipe et le niveau que vous désirez tanter, puis vous donner la liste des coups que vous désirez jouer pour ce niveau.

Les commandes possibles sont:

'avant' : Fait avancer le vaisseau d'une case vers l'avant.

'tdroite' : Fait tourner le vaisseau sur lui même vers la droite.

'tgauche' : Fait tourner le vaisseau sur lui même vers la gauche.



Les commandes sont écrite dans une liste de coups:

coups = ['tdroite' , 'avant' , 'avant' , etc]



Il est possible d'ajouter des boucles dans la liste de coups si vous insérez une liste commençant par un chiffre : 

[ [2, 'avant'] ] = [ 'avant' , 'avant' ]

le chiffre que vous indiquez représente le nombre de fois que les commandes inclue dans la boucle vont se répéter

Exemple: 

coups = ['tgauche' , [2, 'avant' , 'tdroite'] ]
      = ['tgauche' , 'avant' , 'tdroite' , 'avant' , 'tdroite']

Il est aussi possible de mettre des boucles dans des boucles:

Exemples:
coups = [ [2, [3, 'avant'], 'tgauche'] , 'tdroite'] 
      = [ 'avant', 'avant', 'avant', 'tgauche', 'avant', 'avant', 'avant', 'tgauche', 'tdroite']

#   COMMENT GAGNER !

Vous avez des points pour chaque sphère que vous réussissez à récupérer et des points bonus si vous les récupérer tous dans un même niveau.

Vous perdez des points pour chaque mot dans la liste de coups donc les boucles rapporte plus de points

Le nombre de déplacement du véhicule n'a pas d'importance seulement le nombre de mots dans la liste de coups donc le trajet le plus cours n'est pas toujours le plus payant. 

