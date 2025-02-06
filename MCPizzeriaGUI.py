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

def zoekKlant():
 #haal de ingevoerde_klantnaam op uit het invoerveld

 # en gebruik dit om met SQL de klant in database te vinden
    gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
    print(gevonden_klanten) # om te testen
    invoerveldKlantnaam.delete(0, END) #invoerveld voor naam leeg maken
    invoerveldKlantNr.delete(0, END) #invoerveld voor klantNr leeg maken
 
    for rij in gevonden_klanten: #voor elke rij dat de query oplevert
 #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld
        invoerveldKlantNr.insert(END, rij[0]) 
 #toon klantAchternaam, de tweede kolom uit het resultaat in de invoerveld
        invoerveldKlantnaam.insert(END, rij[1])

def zoekPizza():
       gevonden_pizza = MCPizzeriaSQL.zoekPizzaInTabel(ingevoerde_pizzanaam.get())
       print(gevonden_pizza)
       listboxMenu.delete(0, END)
       listboxMenu.insert(0,"ID Gerecht Prijs")
       for regel in gevonden_pizza:
            listboxMenu.insert(END, regel)

def toonMenuInListbox():
       listboxMenu.delete(0, END) #maak de listbox leeg
       pizza_tabel = MCPizzeriaSQL.vraagOpGegevensPizzaTabel()
       listboxMenu.insert(0, "ID Gerecht Prijs")
       for regel in pizza_tabel:
              listboxMenu.insert(END, regel)

def haalGeselecteerdeRijOp(event):
 #bepaal op welke regel er geklikt is
 geselecteerdeRegelInLijst = listboxMenu.curselection()[0] 
 #haal tekst uit die regel
 geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst) 
 #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
 invoerveldGeselecteerdePizza.delete(0, END) 
 #zet tekst in veld
 invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst[1])

#voeg de bestelling van klant met gekozen pizza en aantal toe 
#in de winkelwagentabel
#en toon de bestelling in de listbox op het scherm
def voegToeAanWinkelWagen():
       klantNr = invoerveldKlantNr.get()
       gerechtID = invoerveldGeselecteerdePizza.get()
       aantal = aantalGekozen.get()
       MCPizzeriaSQL.voegToeAanWinkelWagen(klantNr, gerechtID, aantal )
       winkelwagen_tabel = MCPizzeriaSQL.vraagOpGegevensWinkelWagenTabel()
       listboxWinkelwagen.delete(0, END) #listbox eerst even leeg maken
       for regel in winkelwagen_tabel:
              listboxWinkelwagen.insert(END, regel)
### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")
knopSluit = Button(venster, text="Venster sluiten", width=50, command=venster.destroy)
knopSluit.grid(row=17, column=3)
labelIntro = Label (venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky='W')
klantnaam = Label (venster, text='Klantnaam')
klantnaam.grid(row= 1,column=0, sticky='W')
klantnummer = Label (venster, text='Klantnummer')
klantnummer.grid(row= 2,column=0, sticky='W')
ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")
invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")
knopZoekOpKlantnaam = Button(venster, text='Zoek klant', width=12, command=zoekKlant)
knopZoekOpKlantnaam.grid(row=1, column=2)
labelPizzanaam = Label (venster, text='Pizza naam')
labelPizzanaam.grid(row=3, column=0,sticky='W')
ingevoerde_pizzanaam = StringVar()
invoerveldpizzanaam = Entry (venster, textvariable=ingevoerde_pizzanaam)
invoerveldpizzanaam.grid (row=3, column=1,sticky='W')
knopZoekOpPizzaNaam = Button(venster, text='Zoek Pizza', width=12, command= zoekPizza)
knopZoekOpPizzaNaam.grid (row=3,column=2)
knopToonPizzas = Button(venster, text="Toon alle pizza's", width=12, command=toonMenuInListbox)
knopToonPizzas.grid (row=4,column=2,sticky=N)
labelMogelijkheden = Label (venster, text='Mogelijkheden')
labelMogelijkheden.grid(row=4, column=0)
listboxMenu = Listbox (venster, width=50)
listboxMenu.grid (row=4, column=1)
listboxMenu.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)
geselecteerdepizza = Label (venster, text='Gekozen pizza')
geselecteerdepizza.grid(row=5, column=0)
invoerveldGeselecteerdePizza = Entry (venster)
invoerveldGeselecteerdePizza.grid(row=5, column=1,sticky='W')
aantalGekozen = IntVar()
aantalGekozen.set(1)
AantalLabel = Label (venster, text='Aantal')
AantalLabel.grid (row=6,column=0)
optionMenuPizzaAantal = OptionMenu(venster, aantalGekozen, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
optionMenuPizzaAantal.grid(row=6, column=1,sticky=W)
voegtoeknop = Button (venster, width=15, text='Voeg toe',command=voegToeAanWinkelWagen)
voegtoeknop.grid (row=6,column=1,sticky=E)
Bestellingenlabel = Label(venster, text='Bestelling:')
Bestellingenlabel.grid (row=7,column=0,sticky=N)
listboxWinkelwagen = Listbox (venster, width=50)
listboxWinkelwagen.grid (row=7,column=1)
















#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()