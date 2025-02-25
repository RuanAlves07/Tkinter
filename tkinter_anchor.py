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

# Código abaixo posiciona cada label em lugares diferentes
# Após testar, comente a linha do LB1 até o LB4

lb1.pack(side = LEFT)
lb2.pack(side = "left")
lb3.pack(anchor = "w") # Sempre que não utilizo a opção side, ele sempre será topo
#lb4.pack(anchor = "w") # Sempre que não utilizo a opção side, ele sempre será topo

#lb4.pack(side=BOTTOM, anchor = "sw")

lb4.pack(anchor = "e")

i.mainloop()