# Défi prog 2025

Le fichier main gère l'affichage de pygame et des boutons.
Le fichier exploration_class gère le jeu en soit et les commandes qui rendent le jeu fonctionnel.
Le fichier gestion_scores sert a gérer l'écriture et la lecture du fichier json des scores.

Le fichier zone de jeu est le seul fichier qui doit être modifier par le joueur, il permait de donner au jeu les informations nécessaire au déroulement de la partie.

# Comment jouer

Dans zone_de_jeu vous indiquez votre numéro d'équipe et le niveau que vous désirez tanter, puis vous donner la liste des coups que vous désirez jouer pour ce niveau.

Les commandes possibles sont:

'avant' : Fait avancer le vaisseau d'une case vers l'avant.

'tdroite' : Fait tourner le vaisseau sur lui même vers la droite.

'tgauche' : Fait tourner le vaisseau sur lui même vers la gauche.



Les commandes sont écrite dans une liste de coups:

coups = ['commande1', 'commande2', 'commande3', etc]   ou les commandes sont soit 'avant', 'tdroite' ou 'tgauche'



Il est possible de faire des boucles de commandes:

Dans la liste de coups si vous inséré une liste de la forme : [#, 'commande1', 'commande2', 'commande3', etc] 
le nombre que vous indiquer à la place du # représente le nombre de fois que les commandes inclue dans la boucle vont se repéter 

Exemple:
coups = ['commande1', [2, 'avant', 'tdroite'], 'commande2'] = ['commande1', 'avant', 'tdroite', 'avant', 'tdroite', 'commande2'] 


Il est aussi possible de mettre des boucles dans des boucles:

Exemples:
coups = ['commande1', [2, [3, 'avant'], 'tgauche']] 
      = ['commande1', 'avant', 'avant', 'avant', 'tgauche', 'avant', 'avant', 'avant', 'tgauche']

#   COMMENT GAGNER !

Les points sont calculé selon la nombre de commandes que vous avez donner pour réussir chaque niveau (Le moins possible donc essayer les boucles)

Vous avez des points pour chaque minerai que vous réussissez à récupérer et des points bonus si vous les récupérer tous dans un même niveau.
