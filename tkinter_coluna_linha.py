from tkinter import *

i = Tk()
i.geometry("980x720+250+30")
i.title ("Programa Financeiro")

lb1 = Label(i, text = "Login", bg = "white" ) 

#componente .grid serve também para posicionar utilizando indicativo de linha(row) e coluna (column)

lb1.place(x= 640, y = 30 )
lb2 = Label(i, text = "Senha", bg = "white")
lb2.place(x = 640, y = 80)

ed1 = Entry(i)
ed1.place(x = 620, y = 60)

ed2 = Entry(i)
ed2.place(x = 600, y = 100)

bt1 = Button(i, text = "Login")
bt1.place(x = 450, y = 450)

i.mainloop()