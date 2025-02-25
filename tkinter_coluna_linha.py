from tkinter import *

i = Tk()
i.geometry("980x720+250+30")
i.title ("Programa Financeiro")

#componente .grid serve também para posicionar utilizando indicativo de linha(row) e coluna (column)

i["bg"] = "#CFB997"

#lb1 = Label(i, text = "Login:", bg = "#D3D3D3" ) #lb1 = tudo referente ao "login", sendo as duas linhas de código sobre o texto
#lb1.place(x= 1530, y = 30 )


#lb2 = Label(i, text = "Senha:", bg = "#D3D3D3") #lb2 = tudo referente a "senha", sendo as duas linhas de código sobre o texto
#lb2.place(x = 1530, y = 90, )

#ed1 = Entry(i, width = "50") # barra do login
#ed1.place(x = 1400, y = 60)

#ed2 = Entry(i, width = "50") # barra da senha
#ed2.place(x = 1400, y = 120)

#bt1 = Button(i, text = "Login", width = "50") #botão do login
#bt1.place(x = 800, y = 550)

# O código abaixo faz correção das posições das labels

lb1 = Label(i, text = "Login:", bg = "#D3D3D3" )
lb1.grid(row = 1, column = 1)

lb2 = Label(i, text = "Senha:", bg = "#D3D3D3" )
lb2.grid(row = 2, column = 1)

ed1 = Entry(i)
ed1.grid(row = 1, column = 2)

ed2 = Entry(i)
ed2.grid(row = 2, column = 2)

bt1 = Button(i, text = "Login") 
bt1.grid(row = 3, column = 1)

i.mainloop()