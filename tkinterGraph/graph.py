import tkinter as tk
from tkinter import *

root = Tk()
root.title('SOLVER EQUATION')   # método: dar título à interface 
root['bg'] = 'gray'     # 'bg': back graund -> altera a cor de fundo 

# posicionamento e geometria
width = 600
height = 400
# centralizar a janela
widthScreem = root.winfo_screenwidth()
heightScreem = root.winfo_screenheight()
posx = widthScreem / 2 - width / 2
posy = heightScreem / 2 - height / 2
root.geometry('%dx%d+%d+%d' % (width, height, posx, posy))    # método: dimensionar a geometria e seu posicionamento
root.resizable(False, False)      # método: fixar ou variar o dimencionamento da janela 
root.minsize(width = 600, height = 400)     # método: definir dimensão mínima
root.maxsize(width = 700, height = 700)     # método: definir dimensão máxima 
root.state('iconic')    # método: iniciar a abertura com a dimensão mínima. Para a dimensão máx ('zoomed')
root.iconbitmap('tkinterGraph\images\icon-math.ico')     # método: inserir ícone na janela (tipo de aquivo: .ico)

# criação de um button
inicialLabel = Label(
    root,
    text= 'Solver Equation.\nEnter a equation.', #texto 
    font= 'Calibri 16 bold',    # estilo, tamanho e característica da fonte
    fg= 'white',    # cor da fonte
    anchor= CENTER,  # alinhamento do texto (de acordo com uma bússola)
    bg= 'blue',     # cor back graund
    width= 60,  # comprimento do Label
    height= 2,  # altura do Label
    bd= 3,  # tamanho da borda 
    relief= 'solid' # estilo da borda
).pack()

# criação do label ---> espaço para colocar um texto
label1 = Label(
    root, 
    text = '=', 
    font = 'Calibri 14 bold',  
    fg = 'black', 
    anchor= CENTER, 
    bg = 'grey', 
    bd= 3,
    relief= 'flat'
).pack()    


root.mainloop()     # método de looping: abrir interface
