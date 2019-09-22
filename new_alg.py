import random
raw_matrix = [[0 for i in range(5)] for j in range(5)]
raw_matrix[0][0] = 1
raw_matrix[random.randint(1, 4)][random.randint(1, 4)] = 1
for i in raw_matrix:
    print(i)
