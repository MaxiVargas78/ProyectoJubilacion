from tkinter import *

raiz=Tk()

raiz.title("PREVISION JUBILACION")
raiz.resizable(1,1)
#raiz.iconbitmap("afp.icon")
raiz.geometry("900x720")
raiz.config(bg="red")

def datos():
	x=550000
	result.config(text="Su pension estimada sera de "+str(x))

raiz.config(bg="white")
miframe=Frame()
miframe.pack()
miframe.pack(fill="both",expand="True")
miframe.config(bg="#56d6df")


raiz.mainloop()
