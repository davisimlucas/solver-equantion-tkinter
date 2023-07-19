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
inicialButton = Button(root, text = 'Início')
inicialButton.pack()

root.mainloop()     # método de looping: abrir interface
