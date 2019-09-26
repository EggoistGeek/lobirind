
# Алгоритм был основан на методе змейки (https://habr.com/ru/post/318530/)
# Смысл в том, чтобы:
# 1. Заполнить всё поле 1 (Стены)
# 2. Выбрать точку старта и отправить змейку (aka Марио aka Miner)
#    Он будет ходить по лабиринту в рандомном направлении и "рыть туннель"
# 
# Нюансы:
# 1. Шахтёр не ломает стены к уже прорытым туннелям
# 2. Если шахтёр зашёл в тупик, он развернётся из пойдёт назад (За это отвечает minerHistory)
# 3. Если minerHistory будет пустой, то это значит, что лабиринт закончит (Выводится в консоль "Really no way")
# 4. Шахтёр будет пытаться избегать прямых туннелей (За это отвечают previousDir и previousDirRepeated)
#		Если шахтёр повторно выбирает одно и тоже направление некое кол-во раз, то он посторается сменить его


import random

# Метод для отображения матрици (был необходим во время отладки)
displayMaze = ""

# Направления куда может смотреть шахтёр (2 - тк мы строим стенки между туннелями. Если поставить 1, то всё поле будет состоять из 0)
dirs = [[0,2], [2,0], [0,-2], [-2,0]]


# Проверка на правльность значений. False если вне матрицы и True когда в ней
def isMatrixPos(x, y, size):
	if x < 0 or y < 0: return False
	elif x >= size or y >= size: return False
	else: return True


# Вызывается из maze.py и возращает готовый лабиринт
# Принмает size-размер лабиринта и action-передаётся DisplayMaze из maze.py
def GetFinalMaze(size, action):

	displayMaze = action
	
	# Собственно, сама матрица (Примичание: maze[x][y] - x это вертикаль, а y горизонталь)	
	maze = [[1 for i in range(size)] for j in range(size)]

	# Установка шахтёра в стартовую позицию (Любая точка, хоть 0,0)
	minerPos = [int(size / 2),int(size / 2)]
	maze[minerPos[0]][minerPos[1]] = 0

	minerHistory = [minerPos]

	previousDir = [0,0]
	previousDirRepeated = 0

	# Цикл шахётра. Тут происходит магия
	while True:
		
		# Копируем все возможные направления
		availiableDirs = dirs.copy()

		# Цикл (Также служит для обноружения тупиков)
		while len(availiableDirs) > 0:

			# Выбираем куда смотреть
			direct = availiableDirs[random.randint(0,len(availiableDirs) - 1)]

			# Смотрим куда в таком случае попадём
			newMinerPos = [minerPos[0] + direct[0], minerPos[1] + direct[1]]
			# breakWallPos - это позиция стены которую нужно будет сломать
			breakWallPos = [minerPos[0] + int(direct[0] / 2), minerPos[1] + int(direct[1] / 2)]

			# Проверяем, если то куда мы попадём находится в матрице И там ещё нет туннеля (.. == 1)
			if isMatrixPos(newMinerPos[0], newMinerPos[1], size) and maze[newMinerPos[0]][newMinerPos[1]] == 1:

				# Проверяем, не выбираем ли мы одно и тоже направление
				if direct == previousDir:
					if previousDirRepeated > 3:
						if len(availiableDirs) > 1:
							continue
					else:
						previousDirRepeated += 1
				else:
					previousDir = direct
					previousDirRepeated = 0

				# Если всё окей, то роем туннель
				minerPos = newMinerPos # Перемещаем шахтёра
				maze[minerPos[0]][minerPos[1]] = 0 # Копаем место для шахтёра
				maze[breakWallPos[0]][breakWallPos[1]] = 0 # Ломаем стену
				minerHistory.append(minerPos) # Записываем с историю (Не работает в режиме инкогнито :D )
			else:
				# Если нас чем то не удовлетворило направление, то удаляем его из списка просматриваемых и повторяем цикл
				availiableDirs.remove(direct)

		# Если получилось так, что ни одно направление не подошло, то это значит, что мы в тупике
		if len(availiableDirs) == 0:
			# Если история пуста
			if len(minerHistory) <= 1:
				# Значит, закончили делать лабиринт
				print("Really no way")
				break
			else:
				# Если в истории ещё что-то есть, то удаляем последнюю запись и возращаем шахтёра на ещё шаг назад
				minerHistory.remove(minerPos)
				minerPos = minerHistory[len(minerHistory) - 1]

	return maze
