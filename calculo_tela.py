from tkinter import *

def bt_soma():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 + num2

def bt_subtracao():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 - num2

def bt_multiplicacao():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 * num2

def bt_divisao():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 / num2

                
i = Tk() 
i.title("Programa financeiro")
i.geometry("980x720+250+30")

# ADIÇÃO

lb = Label(i, text = "0")
lb.place(x = 230, y = 200)

bt = Button(i, width = "15", text = "SOMAR", bg = "white", command = bt_soma)
bt.place(x = 230, y = 220)

# SUBTRAÇÃO

bt = Button(i, width = "15", text = "SUBTRAIR", bg = "white", command = bt_subtracao)
bt.place(x = 230, y = 250)

# MULTIPLICAÇÃO

bt = Button(i, width = "15", text = "MULTIPLICAR", bg = "white", command = bt_multiplicacao)
bt.place(x = 230, y = 280)

# DIVISÃO

bt = Button(i, width = "15", text = "DIVIDIR", bg = "white", command = bt_divisao)
bt.place(x = 230, y = 310)


lb = Label(i, text = "Ruan Augusto Alves")
lb.place(x = 230, y = 400)

ed1 = Entry(i)
ed1.place(x = 230, y = 150)

ed2 = Entry(i)
ed2.place(x = 230, y = 180)

i["bg"] = "gray"

i.mainloop()