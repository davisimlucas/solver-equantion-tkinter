import tkinter as tk
import solverLogic as solver
from tkinter import *
from solverLogic import *

root = Tk()
root.title('SOLVER EQUATION')   # método: dar título à interface 

root.geometry('600x400+400+150')    # método: dimensionar a geometria e seu posicionamento
root.resizable(True, True)      # método: fixar ou variar o dimencionamento da janela 

root.minsize(width = 600, height = 400)     # método: definir dimensão mínima
root.maxsize(width = 700, height = 700)     # método: definir dimensão máxima 

root.state('iconic')    # método: iniciar a abertura com a dimensão mínima. Para a dimensão máx ('zoomed')

root.iconbitmap('tkinterGraph\images\icon-math.ico')     # método: inserir ícone na janela (tipo de aquivo: .ico)

root.mainloop()     # método de looping: abrir interface
