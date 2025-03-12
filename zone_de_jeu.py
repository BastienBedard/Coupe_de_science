"""
Fichier de jeux

Indiquer votre numéro d'équipe et le niveu que vous voulez jouer
puis écriver les différentes commandes que vous voulez donner au vaisseau.
"""
from main import play

EQUIPE = 0
NIVEAU = 0
coups = ['avant']
play(equipe = EQUIPE, niveau = NIVEAU, moves = coups)
















#0=300
#1=300
#2=700
#3=450
#4=700

# coups = [[4, 'avant']]
# coups = ['avant', [4, [3, 'avant'], 'tdroite']]#1
# coups = ['avant','tdroite','avant',[4,[4,'avant'],'tgauche']]#2
# coups = [[3, 'tgauche', 'avant', [2, 'tdroite'], 'avant', 'tgauche', [2,'avant']]]#3
# coups = ['tdroite', [7, 'avant'], [2,'tdroite', [2,'avant']], [4, 'avant'], [2,'tdroite', [4,'avant']], [2, 'avant']] #4

# coups = [[2, 'avant'], 'tdroite', [7, 'avant'], [2,'tdroite', [2,'avant']], [4, 'avant'], [2,'tgauche', [2,'avant']], [4, 'avant']]#4
# coups = ['avant', 'tdroite', [3,'avant'], 'tgauche', [2, 'avant']]#1
