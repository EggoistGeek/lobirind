from tkinter import *
import random
import n_backend
import velikiyrandom

# Размер каждого блока (стена и проход) в пикселях
blockSize = 10

# Отрисовка матрицы на канвасе
def DisplayMaze(matrix, size):
	c.delete("all")
	for x in range(0, size):
		for y in range(0, size):
			color = "black" if matrix[x][y] == 0 else "white" if matrix[x][y] == 1 else "red"
			c.create_rectangle(y * blockSize, x * blockSize, y * blockSize + blockSize, x * blockSize + blockSize, fill=color)
	c.update()

# Получаем матрицу из бэкенда
def LoadMaze():
	size = int(sizeBox.get())
	c.config(width=blockSize * size, height=blockSize * size)
	matrix = n_backend.GetFinalMatrice(size)
	DisplayMaze(matrix, size)

def LoadMaze2():
	size = int(sizeBox.get())
	c.config(width=blockSize * size, height=blockSize * size)
	DisplayMaze(velikiyrandom.GetFinalMaze(size), size)


root = Tk()
root.title("Лабиринт на Python")
root.iconbitmap('telega.ico')
root.minsize(400,140)

c = Canvas(root, width=0, height=0, bg='white')
c.pack()

sizeLbl = Label(text="Введите размер лабиринта")
sizeLbl.pack()

sizeBox = Entry(textvariable="10")
sizeBox.pack()

btn = Button(text="Создать", command=LoadMaze2)
btn.pack()


root.mainloop()