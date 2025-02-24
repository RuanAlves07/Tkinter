from tkinter import *

# Criando uma função para clique no botão 

def bt_click():
    #O label que usa propriedade TEXT receberá a mensagem "Trocou o texto"
    lb["text"] = "Trocou o texto"

    #Esse print abaixo exibe o texto na tela do console 

    print("O botão foi clicado!")

def bt_clickar():
    #Esse print exibe o texto digitado na caixa de texto e exibe na label da tela 
    print(ed.get()) 
    lb["text"]=ed.get()

# i (instanciar) recebe o objeto Tk

i = Tk()

#Gerar titulo na janela

i.title("Programa financeiro")
i.geometry("980x720+250+30")
i["bg"] = "green"

# i.wm_iconbitmap("icone.ico") - TEMPORARIO

lb =  Label(i, text = "Nome do usuário")
lb.place(x = 100, y = 100)

bt = Button(i,width = '20', text = 'OK', command = bt_click)
bt.place(x = 230, y = 100)

# O código abaixo cria um botão e posiciona abaixo do botão OK.

bt = Button(i,width = '20', text = 'Capturar', command = bt_clickar)
bt.place(x = 230, y = 190)

# Criar a caixa de texto 

ed = Entry(i)
ed.place(x = 230, y = 150)

i.mainloop()