from tkinter import *

def bt_soma():
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        #Se valores não forem numericos, imprime a mensagem abaixo
        lb["text"] = num1 + num2
        lb["bg"] = "#00FA9A"
    else:
        lb["text"] = "Valores são invalidos!"
        lb["bg"] = "red"
 
def bt_subtracao():
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        #Se valores não forem numericos, imprime a mensagem abaixo
        lb["text"] = num1 - num2
        lb["bg"] = "#00FA9A"
    else:
        lb["text"] = "Valores são invalidos!"
        lb["bg"] = "red"

def bt_multiplicacao():
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        #Se valores não forem numericos, imprime a mensagem abaixo
        lb["text"] = num1 * num2
        lb["bg"] = "#00FA9A"
    else:
        lb["text"] = "Valores são invalidos!"
        lb["bg"] = "red"

def bt_divisao():
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        #Se valores não forem numericos, imprime a mensagem abaixo
        lb["text"] = num1 / num2
        lb["bg"] = "#00FA9A"
    else:
        lb["text"] = "Valores são invalidos!"
        lb["bg"] = "red"
                
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


lb2 = Label(i, text = "Ruan Augusto Alves👌👌👌")
lb2.place(x = 230, y = 400)

ed1 = Entry(i)
ed1.place(x = 230, y = 150)

ed2 = Entry(i)
ed2.place(x = 230, y = 180)

i["bg"] = "light gray"

i.mainloop()