import random

SIZE = 21
# делаем матрицу
raw_matrix = [[0 for i in range(SIZE+1)] for j in range(SIZE+1)]
raw_matrix[0][0] = 1
# делаем координаты
x = random.randint(1, SIZE-1)
y = random.randint(1, SIZE-1)
# начальная точка
raw_matrix[y][x] = 1
b = 0
good = [1, 2, 3, 4]
choise = []
choise.extend(good)
for j in range(100000):
    b = 0
    while b != 4:
        a = random.choice(choise)  # 1 - север, 2 - юг, 3 - восток, 4 - запад
        if a == 1:
            if y-2 < 0 or y-2 > SIZE-1 or raw_matrix[y-2][x] == 1:  # проверка на наличие прохода и выходы за пределы листа
                b += 1
                print('not')
                choise.remove(1)
                continue


            else:
                choise = []
                choise.extend(good)
                raw_matrix[y-1][x] = 1
                y -= 2
                raw_matrix[y][x] = 1
                b = 0
                print(j)
                for i in raw_matrix:
                    print(i)
                print("  ")

        if a == 2:
            if y+2 < 0 or y+2 > SIZE-1 or raw_matrix[y+2][x] == 1:  # проверка на наличие прохода и выходы за пределы листа
                b += 1
                print('not')
                choise.remove(2)
                continue
            else:
                raw_matrix[y+1][x] = 1
                choise = []
                choise.extend(good)
                y += 2
                raw_matrix[y][x] = 1
                b = 0
                print(j)
                for i in raw_matrix:
                    print(i)
                print("  ")

        if a == 3:
            if x-2 < 0 or x-2 > SIZE-1 or raw_matrix[y][x-2] == 1:  # проверка на наличие прохода и выходы за пределы листа
                b += 1
                print('not')
                choise.remove(3)
                continue
            else:
                choise = []
                choise.extend(good)
                raw_matrix[y][x-1] = 1
                x -= 2
                raw_matrix[y][x] = 1
                b = 0
                print(j)
                for i in raw_matrix:
                    print(i)
                print("  ")

        if a == 4:
            if x+2 < 0 or x+2 > SIZE-1 or raw_matrix[y][x+2] == 1:  # проверка на наличие прохода и выходы за пределы листа
                print('not')
                b += 1
                choise.remove(4)
                continue
            else:
                choise = []
                choise.extend(good)
                raw_matrix[y][x+1] = 1
                x += 2
                raw_matrix[y][x] = 1
                b = 0
                print(j)
                for i in raw_matrix:
                    print(i)
                print("  ")

    x = random.randint(0, SIZE-1)
    y = random.randint(0, SIZE-1)

raw_matrix[y][x] = 3333333
for i in raw_matrix:
    print(i)


# if __name__ == '__main__':
#     for i in raw_matrix:
#         print(i)

