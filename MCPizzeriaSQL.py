# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in:
# Gijs
# Lieven
#


### --------- Bibliotheken en globale variabelen -----------------

import sqlite3
with sqlite3.connect("MCPizzeria.db") as db:
    cursor = db.cursor()
    #cursor is object waarmee je data uit de database kan halen


### ---------  Functie definities  -----------------
def maakTabellenAan () :
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbi_pizzas(
        gerechtID INTEGER PRIMARY KEY AUTOINCREMENT,
        gerechtNaam TEXT NOT NULL,
        gerechtPrijs REAL NOT NULL);""")
    print("Tabel 'tbi_pizzas' aangemaakt")

### --------- Hoofdprogramma  ---------------
maakTabellenAan()
