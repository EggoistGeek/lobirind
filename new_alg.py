import random
raw_matrix = [[0 for i in range(5)] for j in range(5)]
matrix = {}
raw_matrix = list(enumerate(raw_matrix))
for i, j in raw_matrix:
    matrix.update({i: j})
print(matrix)
