import random
SIZE = 21
raw_matrix = [[0 for i in range(SIZE+1)] for j in range(SIZE+1)]
def point_two():
    x = random.randint(1, SIZE)
    y = random.randint(1, SIZE)
    return x, y


