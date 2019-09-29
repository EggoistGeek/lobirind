from tkinter import *
from tkinter import ttk
import random
import zaebal
import platform
import log

# Размер каждого блока (стена и проход) в пикселях
blockSize = 8
mazeSize = 31

# Отрисовка матрицы на канвасе
def DisplayMaze(matrix, size):
	c.delete("all")
	for x in range(0, size):
		for y in range(0, size):
			color = "black" if matrix[x][y] == 0 else "white" if matrix[x][y] == 1 else "red" if matrix[x][y] == 2 else "green"
			c.create_rectangle(y * blockSize, x * blockSize, y * blockSize + blockSize, x * blockSize + blockSize, fill=color)
	c.update()

# Получаем матрицу из бэкенда
maze = [[0 for i in range(10)] for j in range(10)]

def LoadMaze4():
	#size = int(sizeBox.get())
	btn.configure(state='disabled')
	comboExample.configure(state='disabled')
	nameBox.configure(state='disabled')

	mazeSize = 31 if comboExample.current() == 0 else 41 if comboExample.current() == 1 else 61 if comboExample.current() == 2 else 71
	size = mazeSize
	c.config(width=blockSize * size, height=blockSize * size)
	global maze
	maze = zaebal.GetFinalMaze(size, DisplayMaze)
	nahuyPos = [random.randint(0, len(maze) - 1), random.randint(0, len(maze) - 1)]
	maze[nahuyPos[0]][nahuyPos[1]] = 3
	maze[playerPos[0]][playerPos[1]] = 2
	DisplayMaze(maze, size)


def SetScoreToJSON(name, score):
	log.save(score, name)


playerPos = [1,1]
nahuyPos = [random.randint(0, len(maze)), random.randint(0, len(maze))]
score = 0
def PlayerController(event):
	global playerPos
	global score

	Xoff = 1 if event.keysym == "Down" else -1 if event.keysym == "Up" else 0
	Yoff = 1 if event.keysym == "Right" else -1 if event.keysym == "Left" else 0

	newPos = [playerPos[0] + Xoff, playerPos[1] + Yoff]

	if maze[newPos[0]][newPos[1]] == 3:
		print("Finished")
		score += 1 + int(comboExample.current())**2 if comboExample.current() != 3 else 999999
		scorelbl.configure(text = "Очки: " + str(score))
		SetScoreToJSON(nameBox.get(), score)
		LoadMaze4()
		return

	if CanISosat(maze, newPos[0], newPos[1]):
		maze[playerPos[0]][playerPos[1]] = 0
		playerPos = newPos
		maze[playerPos[0]][playerPos[1]] = 2
		DisplayMaze(maze, len(maze))

	


def CanISosat(maze, x, y):
	if x < 0 or y < 0 or x >= len(maze) or y >= len(maze): return False
	elif maze[x][y] == 0: return True
	elif maze[x][y] == 1: return False
	else: return True


root = Tk()
root.title("Лабиринт на Python")
if platform.system() != "Linux":
	root.iconbitmap('telega.ico')
root.minsize(400,140)
root.bind('<Left>', PlayerController)
root.bind('<Right>', PlayerController)
root.bind('<Up>', PlayerController)
root.bind('<Down>', PlayerController)
root.resizable(height = False, width = False)

scorelbl = Label(text="Очки: 0")
scorelbl.pack()

c = Canvas(root, width=0, height=0, bg='white')
c.pack()

sizeLbl = Label(text="Имя:")
sizeLbl.pack()

nameBox = Entry(textvariable="43")
nameBox.pack()

sizeLbl = Label(text="Сложность: ")
sizeLbl.pack()


comboExample = ttk.Combobox(root, values=["Дотер", "; в питоне","Нормал","Сложна"])
comboExample.current(1)
comboExample.pack()

#sizeBox = Entry(textvariable="43")
#sizeBox.pack()

btn = Button(text="Создать", command=LoadMaze4)
btn.pack()


root.mainloop()
