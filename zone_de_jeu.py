"""
Fichier de jeux

Indiquer votre numéro d'équipe et le niveu que vous voulez jouer
puis écriver les différentes commandes que vous voulez donner au vaisseau.
"""
from main import play

EQUIPE = 19
NIVEAU = 3
coups = [3, 'avant', 'avant', 'tgauche', 'avant', 'tdroite', 'tdroite', 'avant', 'tgauche']

play(equipe = EQUIPE, niveau = NIVEAU, moves = coups)
















# moves = [[2,'avant'], 'tdroite', [2'avant'], 'tgauche', 'Avant']#2
# coups = ['avant','tdroite','avant',[4,[4,'avant'],'tgauche']]#3
# moves = [[3, [2,'avant'], 'tgauche', 'avant', [2, 'tdroite'], 'avant', 'tgauche']]

# moves = ['avant', 'avant', 'tdroite', [1, [4, 'avant', 'tdroite']]]
