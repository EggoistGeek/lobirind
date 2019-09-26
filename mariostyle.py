import random
import time

directions = [[0,1], [0,-1], [-1,0], [1,0]]


def CanJump(x, y, dir, snakeMatrix):
	if x < 0 or y < 0: return False
	elif x + dir[0] >= int(len(snakeMatrix)) or y + dir[1] >= int(len(snakeMatrix)): return False
	elif snakeMatrix[x + dir[0]][y + dir[1]] == 0: return False
	else: return True


def GetFreeSpace(snakeMatrix):
	freePlaces = []
	for x in range(len(snakeMatrix)):
		for y in range(len(snakeMatrix)):
			if snakeMatrix[x][y] == 1: freePlaces.append([x,y])
	if len(freePlaces) == 0:
		#print("GetFreeSpace: No places")
		return "Sosi"
	toReturn = freePlaces[random.randint(0, len(freePlaces) - 1)]
	#print("Free spaces count ", len(freePlaces), " Returned ", toReturn)
	return toReturn


def GetFinalMaze(size, mazeScript):
	halfSize = int(size / 2)
	snakeMatrix = [[1 for i in range(halfSize)] for j in range(halfSize)]
	maze = [[1 for i in range(size)] for j in range(size)]

	# Шаг 1. Выбираем изначальную позицию
	snakeX = random.randint(0, halfSize)
	snakeY = random.randint(0, halfSize)

	antiLoop = 10000
	cycles = 0
	while antiLoop > 0:
		antiLoop -= 1
		dbg = ">"
		# Зацикливание шага 2
		availableDirs = directions.copy()
		while len(availableDirs) > 0:

			# Шаг 2. Выбираем рандомное направление
			dir = availableDirs[random.randint(0,len(availableDirs) - 1)]

			# Шаг 3. Прыжок
			if CanJump(snakeX, snakeY, dir, snakeMatrix):
				maze[snakeX * 2][snakeY * 2] = 0
				maze[snakeX * 2 + dir[0]][snakeY * 2 + dir[1]] = 0
				snakeX += dir[0]
				snakeY += dir[1]
				snakeMatrix[snakeX][snakeY] = 0
				dbg += "1, "
				break
			else:
				availableDirs.remove(dir)
				dbg += "0, "
				continue

		cycles += 1
		dbg += "2, "

		# Если змейка зашла в тупик
		if len(availableDirs) == 0:
			position = GetFreeSpace(snakeMatrix)
			if position == "Sosi":
				print("Blyat, net mest. Cycles=",cycles)
				dbg += "3, "
				return maze
			else:
				snakeX = position[0]
				snakeY = position[1]
				dbg += "4(" + str(position) + "),"

		print(dbg)
		mazeToDisplay = snakeMatrix.copy()
		#mazeToDisplay[snakeX][snakeY] = 2
		mazeScript(mazeToDisplay, len(mazeToDisplay))
		time.sleep(0.2)

	print("No more time")
	return maze
