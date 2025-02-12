import numpy as np

table = np.zeros((15, 15))
table[14][7] = 1
print(table[14])
table[10:14][:,7] = 2
print(table)