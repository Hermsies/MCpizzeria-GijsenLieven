# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
# 
#
# Vul hier jullie namen in:
# Gijs
# Lieven
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL


### ---------  Functie definities  -----------------


### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")
knopSluit = Button(venster, text="Venster sluiten", width=50, command=venster.destroy)
knopSluit.grid(row=17, column=4)
labelIntro = Label (venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky='W')
klantnaam = Label (venster, text='Klantnaam')
klantnaam.grid(row= 1,column=0, sticky='W')
ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")







#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
