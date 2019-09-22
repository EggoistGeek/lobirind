from random import choice

DATA_TO_RANDOM = [1, 1, 1, 0]

#константа с размером списка
SIZE = 200

#функция инициализации(будет вызываться каждый раз когда функция нахождения путей не найдет путь)
def init():
    example_matrice = [[choice(DATA_TO_RANDOM) for i in range(SIZE)] for j in range(SIZE)]
    example_matrice[0][0] = 1
    example_matrice[SIZE - 1][SIZE - 1] = 1
    return example_matrice

#функция нахождения путей
def is_way(row_matrice):
    modern_matrice = init()
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if row_matrice[i][j] != 0:
                modern_matrice[i][j] = i + j
            else:
                modern_matrice[i][j] = 0
    x = 0
    y = 0
    while True:

        node = modern_matrice[x][y]
        if x < SIZE - 1:
            if modern_matrice[x + 1][y] == node + 1:
                x += 1
                continue
        if y < SIZE - 1:
            if modern_matrice[x][y + 1] == node + 1:
                y += 1
                continue
        elif x == SIZE - 1 and y == SIZE - 1:
            return True
        if x != 0 or y != 0:
            modern_matrice[x][y] = 0
            x = 0
            y = 0
            continue
        return False

#функция сортировки
def sort(matrice):
    while True:
        if is_way(matrice):
            break
        matrice = init()
    return matrice

def GetFinalMatrice(size):
	SIZE = size
	matrice = init()
	some_matrice = sort(matrice)
	print(SIZE)
	return some_matrice
