from tkinter import *
import random
from time import sleep
import n_backend

blockSize = 3

def DisplayMaze(matrix, size):
	c.delete("all")
	for x in range(0, size):
		for y in range(0, size):
			color = "white" if matrix[x][y] == 0 else "black"
			c.create_rectangle(x * blockSize, y * blockSize, x * blockSize + blockSize, y * blockSize + blockSize, fill=color)
	c.update()

def LoadMaze():
	size = int(sizeBox.get())
	c.config(width=blockSize * size, height=blockSize * size)
	matrix = n_backend.GetFinalMatrice(size)
	DisplayMaze(matrix, size - 1)

root = Tk()
root.title("Лабиринт на Python")

c = Canvas(root, width=0, height=0, bg='white')
c.pack()

sizeLbl = Label(text="Введите размер лабиринта")
sizeLbl.pack()

sizeBox = Entry(textvariable="10")
sizeBox.pack()

btn = Button(text="Создать", command=LoadMaze)
btn.pack()


root.mainloop()