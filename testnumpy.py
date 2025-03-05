from main import play


equipe = 2
niveau = 4
# moves = [[2,'avant'], 'tdroite', 'avant', 'Avant', 'avant', 'tgauche', 'Avant']
# moves = ['tdroite', 'avant', 'tgauche', 'avant', [4, [4,'avant'], 'tdroite']]
# moves = [[3, [2,'avant'], 'tgauche', 'avant', [2, 'tdroite'], 'avant', 'tgauche']]

moves = ['avant', 'avant', 'tdroite', [1, [4, 'avant', 'tdroite']]]

play(equipe = equipe, niveau = niveau, moves = moves)
