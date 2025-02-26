import numpy as np

table = np.zeros((15, 15))
table[14][7] = 1
print(table[14])
table[10:14][:,7] = 2
print(table)

moves = ['avant', 'avant', 'tdroite', [2, 'avant', 'tdroite'], 'tgauche']
print(type(moves))
def longmoves(moves):
    strmoves = []
    for move in moves:
        if type(move) is str:
            strmoves += [move]
        elif type(move) is list:
            for i in range(move[0]):
                strmoves += move[1:]
    return strmoves
strmoves = longmoves(moves)
print(strmoves)