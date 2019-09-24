import random


def GetRandomValue():
	raw = random.randint(0, 1)
	result = 1 if raw == 0 else 0
	return result


def GetFirstHorizontal(size):
	horizontal = [0 for i in range(size)]
	for x in range(1, size):
		if(horizontal[x - 1] == 0):
			horizontal[x] = GetRandomValue()
	return horizontal

def GetEndHorizontal(base):
	#horizontal = [0 for i in range(len(base))]
	horizontal = base.copy()
	groupStartIndex = -1
	groupEndIndex = -1
	for x in range(0, len(base)):
		if(base[x] == 0):
			if(groupStartIndex == -1):
				groupStartIndex = x
				groupEndIndex = x
			else:
				groupEndIndex += 1
		else:
			if(groupStartIndex != groupEndIndex):
				randomGate = random.randint(groupStartIndex, groupEndIndex - 1)
				for ix in range(groupStartIndex, groupEndIndex):
					horizontal[ix] = 1
				horizontal[randomGate] = 0
				groupStartIndex = -1
				groupEndIndex = -1

	groupEndIndex = len(base)
	randomGate = random.randint(groupStartIndex, groupEndIndex - 1)
	for ix in range(groupStartIndex, groupEndIndex):
		horizontal[ix] = 1
	horizontal[randomGate] = 0
		
	return horizontal

def GetEndHorizontal2(base):
	horizontal = base.copy()

	freeSpaceStart = -1
	lastIndex = -1
	for x in range(0, len(base)):
		if(base[x] == 0):
			if(freeSpaceStart == -1):
				freeSpaceStart = x
				lastIndex = freeSpaceStart
		else:
			if(freeSpaceStart != x):
				gated = -1
				hasGate = False
				for ix in range(freeSpaceStart, x):
					horizontal[ix] = 1
					if(gated == -1):
						if(random.randint(0, 4) == 0):
							horizontal[ix] = 0
							hasGate = True
					elif(gated == 0):
						gated = -1
					else:
						gated += 1
				if(not hasGate):
					horizontal[random.randint(freeSpaceStart, x - 1)] = 0
				freeSpaceStart = -1

	for ix in range(lastIndex, len(base)):
		horizontal[ix] = 1
	horizontal[random.randint(lastIndex, len(base) - 1)] = 0

	return horizontal



def GetHorizontal(base):
	horizontal = [0 for i in range(len(base))]

	lastEntry = -1
	for x in range(0, len(base)):
		if(base[x] == 0):
			lastEntry = x
			continue
		if(lastEntry != -1):
			blockValue = GetRandomValue()
			horizontal[x] = blockValue
			if(blockValue == 1): lastEntry = -1
		else:
			horizontal[x] = 0


	return horizontal;

def GetMaze(size):
	# Шаг 1. Создать матрицу
	matrix = [[0 for i in range(size)] for j in range(size)]

	# Шаг 2 и 3. Создание первой горизонтали
	matrix[0] = GetFirstHorizontal(size)

	matrix[1] = GetEndHorizontal2(matrix[0].copy())

	#return matrix

	for iy in range(int(2 / 2), int(size / 2)):
		y = iy * 2
		matrix[y] = GetHorizontal(matrix[y - 1].copy())
		matrix[y + 1] = GetEndHorizontal2(matrix[y].copy())


	return matrix


def GetFinalMaze(size):
	return GetMaze(size)