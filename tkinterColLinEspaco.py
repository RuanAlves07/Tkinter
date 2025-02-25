from tkinter import *

i = Tk()
i.geometry("980x720+250+30")
i.title ("Programa Financeiro")

"""lb3 = Label(i, text = "")
lb3.grid(row = 0, column = 0)

lb4 = Label(i, text = "")
lb4.grid(row = 0, column = 0)

lb1 = Label(i, text = "Login:", bg = "#D3D3D3" )
lb1.grid(row = 1, column = 1)

lb5 = Label(i, text = "")
lb5.grid(row = 2, column = 0)

lb2 = Label(i, text = "Senha:", bg = "#D3D3D3" )
lb2.grid(row = 3, column = 1)

ed1 = Entry(i)
ed1.grid(row = 1, column = 2)

ed2 = Entry(i)
ed2.grid(row = 3, column = 2)

lb6 = Label(i, text = "")
lb6.grid(row = 4, column = 0)



bt1 = Button(i, text = "Login") 
bt1.grid(row = 5, column = 1)"""

lb3 = Label(i, text = "", width = 5, height = 3)
lb3.grid(row = 0, column = 0)

lb4 = Label(i, text = "")
lb4.grid(row = 0, column = 0)

lb1 = Label(i, text = "Login:", bg = "#D3D3D3" )
lb1.grid(row = 1, column = 1)

lb5 = Label(i, text = "")
lb5.grid(row = 2, column = 0)

lb2 = Label(i, text = "Senha:", bg = "#D3D3D3" )
lb2.grid(row = 3, column = 1)

ed1 = Entry(i)
ed1.grid(row = 1, column = 2)

ed2 = Entry(i)
ed2.grid(row = 3, column = 2)

lb6 = Label(i, text = "")
lb6.grid(row = 4, column = 0)



bt1 = Button(i, text = "Login") 
bt1.grid(row = 5, column = 1)

i.mainloop()