# Comando abaixo importa tudo da biblioteca que é necessária 
# Para a criação de telas. (ASTERISCO significa tudo)

from tkinter import *

# I (instanciar) recebe o objeto Tk

i = Tk()

# Gerar titulo da janela

i.title ("Programa Financeiro")

# Propriedade que altera o tamanho da janela (980x720) e distancia da direita e topo da tela (250x30)

i.geometry("980x720+250x30")

# Propriedade graficas, cor de fundo da tela (BG) ou (background)
# Não pode passar o i com ponto! Deve ser i[]

i["bg"] = "yellow"

#Cria Icone na janela, você deve ter a imagem no mesmo local do código.

# i.wm_iconbitmap("icone.ico") TEMPORARIO

# Cria um label e posiciona (place). ele em relação a tela. 

lb = Label(i, text = "Nome do usuário: ")
lb.place(x = 100, y = 100)

# Cria um botão e posiciona (place) ele em relação a label.

bt = Button(i, width = "20", text = "OK")
bt.place(x = 230, y = 100)

#Gera a janela gráfica

i.mainloop()