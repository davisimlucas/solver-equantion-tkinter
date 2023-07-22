import os
import sys
import tkinter as tk
from tkinter import *

my_project =  os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(my_project)

from solverLogic.solverEquation import*

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

leftValue = StringVar()
ValueEquals = '='
ValueA = StringVar()
ValueB = StringVar()
ValueOp = StringVar()

resultText = StringVar()

expression = f"{leftValue} {ValueEquals} {ValueA} {ValueOp} {ValueB}"

# criação de um Label de introdução
inicialLabel = Label(
    root,
    text= 'Solver Equation\nEnter a equation', #texto 
    font= ('Calibri', 16, 'bold'),    # estilo, tamanho e característica da fonte
    fg= 'white',    # cor da fonte
    anchor= CENTER,  # alinhamento do texto (de acordo com uma bússola)
    background= 'blue',     # cor back graund
    width= 15,  # comprimento do Label
    height= 2,  # altura do Label
    borderwidth= 3,  # tamanho da borda 
    relief= 'solid')    # estilo da borda

# criação dos entry 
leftEntry = Entry(
    root,
    textvariable= leftValue,
    font= ('Calibri', 14, 'bold'),
    fg= 'black',
    justify= CENTER,
    width= 10,
    background= 'grey',
    borderwidth= 3,
    relief= 'solid')

entryA = Entry(
    root,
    textvariable= ValueA,
    font= ('Calibri', 14, 'bold'),
    fg= 'black',
    justify= CENTER,
    width= 10,
    background= 'grey',
    borderwidth= 2,
    relief= 'solid')

entryOp = Entry(
    root,
    textvariable= ValueOp,
    font= ('Calibri', 14, 'bold'),
    fg= 'black',
    justify= CENTER,
    width= 5,
    background= 'grey',
    borderwidth= 2,
    relief= 'solid')

entryB = Entry(
    root,
    textvariable= ValueB,
    font= ('Calibri', 14, 'bold'),
    fg= 'black',
    justify= CENTER,
    width= 10,
    background= 'grey',
    borderwidth= 2,
    relief= 'solid')
# criação do label do "=" ---> espaço para colocar um texto fixo
equalsLabel = Label(
    root, 
    text= ValueEquals, 
    font= ('Calibri', 14, 'bold'),  
    foreground= 'black', 
    anchor= CENTER, 
    width=5,
    height=2,
    background= 'grey', 
    borderwidth= 3,
    relief= 'flat'
)
# criação do botão de executar 
executeButton= Button(
    root,
    text= 'Solver Execute\nClick here!',
    command= solverEquation(equation=expressionList),
    background= 'blue',
    font= ('Calibri', 14, 'bold'),
    foreground= 'white',
    width= 15,
    height= 2,
    borderwidth= 2,
    relief= 'solid'
)

incognitoLabel = Label(
    root,
    text= 'X =',
    background= 'grey',
    font= ('Calibri', 14, 'bold'),
    foreground= 'black',
    anchor= CENTER,
    width=5,
    borderwidth= 2,
    relief= 'solid'
)

resultLabel = Label(
    root, 
    textvariable= result,
    background= 'blue',
    font= ('Calibri', 14, 'bold'),
    foreground= 'white',
    anchor= CENTER,
    width= 10,
    borderwidth= 2,
    relief= 'solid'
)

inicialLabel.grid(row= 0, column= 0)
leftEntry.grid(row= 1, pady=10, column=0, columnspan= 2)
equalsLabel.grid(row= 1, column=1)
entryA.grid(row= 1, pady=10, column=2)
entryOp.grid(row=1, pady=10, column= 3)
entryB.grid(row= 1, pady=10, column= 4)
executeButton.grid(row=2, column= 0)
incognitoLabel.grid(row= 3, pady= 10, column= 0)
resultLabel.grid(row= 3, pady= 10, column=1)

root.mainloop()     # método de looping: abrir interface