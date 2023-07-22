import os
import sys
import tkinter as tk
from tkinter import *

my_project =  os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(my_project)

from solverLogic.solverEquation import*

root = Tk()
root.title('SOLVER EQUATION')   
root['bg'] = 'grey'    

width = 600
height = 400
widthScreem = root.winfo_screenwidth()
heightScreem = root.winfo_screenheight()
posx = widthScreem / 2 - width / 2
posy = heightScreem / 2 - height / 2
root.geometry('%dx%d+%d+%d' % (width, height, posx, posy))    
root.resizable(False, False)      
root.minsize(width = 600, height = 400)     
root.maxsize(width = 700, height = 700)   
root.state('iconic')   
root.iconbitmap('tkinterGraph\images\icon-math.ico')    

equationString = StringVar()

def showResult():
    resultString = solverEquation(equationString.get())
    resultLabel['text'] = f'X = {resultString}' 

inicialLabel = Label(
    root,
    text= 'Solver Equation\nEnter a equation',
    font= ('Calibri', 16, 'bold'),    
    fg= 'white',    
    anchor= CENTER,  
    background= 'blue',    
    width= 15,  
    height= 2,  
    borderwidth= 3,   
    relief= 'solid') 

entryEquation = Entry(
    root,
    textvariable= equationString,
    font= ('Calibri', 14, 'bold'),
    fg= 'black',
    justify= CENTER,
    width= 10,
    background= 'grey',
    borderwidth= 2,
    relief= 'solid')

executeButton= Button(
    root,
    text= 'Solver Execute\nClick here!',
    command= lambda: showResult(),
    background= 'blue',
    font= ('Calibri', 14, 'bold'),
    foreground= 'white',
    width= 15,
    height= 2,
    borderwidth= 2,
    relief= 'solid'
)

resultLabel = Label(
    root,
    background= 'blue',
    font= ('Calibri', 14, 'bold'),
    foreground= 'white',
    anchor= CENTER,
    width= 10,
    borderwidth= 2,
    relief= 'solid'
)

inicialLabel.grid(row= 0, column= 0)
entryEquation.grid(row= 1, pady=10, column=0)
executeButton.grid(row=2, pady= 10, column= 0)
resultLabel.grid(row= 3, pady= 10, column=0)

root.mainloop()