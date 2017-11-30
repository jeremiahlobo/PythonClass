import tkinter 
from tkinter import messagebox
from tkinter import LEFT
from tkinter import RIGHT
from tkinter import Entry


mainWindow = tkinter.Tk()
mainWindow.geometry("250x250")

def callback():
	text = e.get()
	messagebox.showerror("Error", text)

b = tkinter.Button(mainWindow, text="get", width=10, command=callback)
b.pack(side="right")
e = Entry(mainWindow)
e.pack(side="left")



mainWindow.mainloop()

