import numpy as np

name1 = [3, 1, 0, 1, 0, 1, 1]
name2 = [1, 4, 1, 1, 0, 0, 1]
name3 = [0, 0, 1, 1, 0, 1, 1]
name4 = [1, 0, 0, 1, 1, 1, 1]
np.matrix = [name1, name2, name3, name4]
name5 = ["a", "b", "c", "d", "e", "f", "g", "h"]

R = 6
C = 4
lista = []
szukana = 1
r1 = 1 - 1
c1 = 1 - 1
r2 = 4 - 1
c2 = 5 - 1
lista.append([r1,c1])
print(lista)
print(np.matrix[1][1])

if np.matrix[0][1] == szukana:
    lista.append([0, 1])

print(lista)

