import os
import sys
import tkinter as tk
from tkinter import *

my_project =  os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(my_project)

from controllers.solverController import *

root = Tk()
root.title('SOLVER EQUATION')   
root['bg'] = '#08298A'    

width = 338
height = 320
widthScreem = root.winfo_screenwidth()
heightScreem = root.winfo_screenheight()
posx = widthScreem / 2 - width / 2
posy = heightScreem / 2 - height / 2
root.geometry('%dx%d+%d+%d' % (width, height, posx, posy))    
root.resizable(TRUE, TRUE)      
root.state('iconic')   
root.iconbitmap('assets/icon-math.ico')    

equationString = StringVar()

def showResult():
    resultString = solverEquation(equationString.get())
    resultLabel['text'] = f'X = {resultString:.2f}' 

inicialLabel = Label(
    root,
    text= 'Solver Equation',
    font= ('Calibri', 16, 'bold'),    
    foreground= '#D8D8D8',    
    anchor= CENTER,  
    background= '#08298A',    
    width= 30,  
    height= 2,  
    borderwidth= 3,   
    relief= 'flat') 

exempleLabel = Label(
    root, 
    text= 'Enter a equation\nExemple: X = A op B\nop: "+" or "-" or "*" or "/"',
    font= ('Calibri', 12),
    foreground= 'black',
    justify= CENTER,
    width= 30,
    background= '#D8D8D8',
    borderwidth= 2,
    relief= 'solid',
)

entryEquation = Entry(
    root,
    textvariable= equationString,
    font= ('Calibri', 14, 'bold'),
    fg= 'black',
    justify= CENTER,
    width= 23,
    background= '#D8D8D8',
    borderwidth= 2,
    relief= 'solid')

executeButton= Button(
    root,
    text= 'Solver Execute\nClick here!',
    command= lambda: showResult(),
    background= '#D8D8D8',
    font= ('Calibri', 14, 'bold'),
    foreground= 'black',
    width= 15,
    height= 2,
    borderwidth= 2,
    relief= 'solid'
)

resultLabel = Label(
    root,
    background= '#D8D8D8',
    font= ('Calibri', 14, 'bold'),
    foreground= 'black',
    anchor= CENTER,
    width= 15,
    borderwidth= 2,
    relief= 'flat'
)

inicialLabel.grid(row= 0, column= 0)
exempleLabel.grid(row= 1, pady= 5, column=0)
entryEquation.grid(row= 2, pady=10, column=0)
executeButton.grid(row=3, pady= 10, column= 0)
resultLabel.grid(row= 4, pady= 10, column=0)

root.mainloop()