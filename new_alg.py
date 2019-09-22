import random

SIZE = 20
# делаем матрицу
raw_matrix = [[0 for i in range(SIZE)] for j in range(SIZE)]
raw_matrix[0][0] = 1
# делаем координаты
x = random.randint(1, SIZE-1)
y = random.randint(1, SIZE-1)
# начальная точка
raw_matrix[y][x] = 1
# while True:
a = random.randint(1, 4)  # 1 - север, 2 - юг, 3 - восток, 4 - запад
if a == 1:
    if raw_matrix[y-2][x] == 1 or y-2 < 0 or y-2 > SIZE:  # проверка на наличие прохода и выходы за пределы листа
        pass
    else:
        raw_matrix[y-1][x] = 1
        y -= 2
        raw_matrix[y][x] = 1
    for i in raw_matrix:
        print(i)
        print("  ")

if a == 2:
    if raw_matrix[y+2][x] == 1 or y+2 < 0 or y+2 > SIZE:  # проверка на наличие прохода и выходы за пределы листа
        pass
    else:
        raw_matrix[y+1][x] = 1
        y += 2
        raw_matrix[y][x] = 1
    for i in raw_matrix:
        print(i)
        print("  ")

if a == 3:
    if raw_matrix[y][x-2] == 1 or x-2 < 0 or x-2 > SIZE:  # проверка на наличие прохода и выходы за пределы листа
        pass
    else:
        raw_matrix[y][x-1] = 1
        x -= 2
        raw_matrix[y][x] = 1
    for i in raw_matrix:
        print(i)
        print("  ")

if a == 4:
    if raw_matrix[y][x+2] == 1 or x+2 < 0 or x+2 > SIZE:  # проверка на наличие прохода и выходы за пределы листа
        pass
    else:
        raw_matrix[y][x+1] = 1
        x += 2
        raw_matrix[y][x] = 1
    for i in raw_matrix:
        print(i)
        print("  ")



# if __name__ == '__main__':
#     for i in raw_matrix:
#         print(i)

