from tkinter import *

i = Tk()

i.geometry("980x720+250+30")

i.title ("Programa Financeiro")

lb1 = Label(i, text = "Label 1", bg = "pink")
lb1.place(x = 230, y = 200)

lb2 = Label(i, text = "Label 2", bg = "yellow")
lb2.place(x = 230, y = 200)

lb3 = Label(i, text = "Label 3", bg = "green")
lb3.place(x = 230, y = 200)

lb4 = Label(i, text = "Label 4", bg = "red")
lb4.place(x = 230, y = 200)

"""lb2.pack()
lb3.pack()
lb1.pack()
lb4.pack()"""



"""lb1.pack(side = "top") # O código ao lado é responsável por posicionar o label no topo da interface
lb2.pack(side = "left") # O código ao lado é responsável por posicionar o label na esquerda da interface
lb3.pack(side = "right") #  O código ao lado é responsável por posicionar o label no direita da interface
lb4.pack(side = "bottom") # O código ao lado é responsável por posicionar o label abaixo da interface"""


lb1.pack(side = "left") 
lb2.pack(side = "left") 
lb3.pack() 
lb4.pack()



i.mainloop()