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
