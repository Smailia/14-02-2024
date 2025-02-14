inventario = {

0 : {"nome": "Il PC di ...", "quantità": 1, "prezzo": 3999},
1 : {"nome": "Nintendo Switch 2", "quantità": 10, "prezzo": 449},
2 : {"nome": "GTA VI", "quantità": 3, "prezzo": 100}
} 

while true:
   scelta = input("Premi: 1. Aggiungere un prodotto nome, quantità e prezzo 2. Modificare la quantità di un prodotto esistente 3. Modificare il prezzo di un prodotto esistente 4. Eliminare un prodotto dall’inventario 5. Visualizzare l’intero inventario in modo leggibile")
if scelta == 1:
        x = str(input("Aggiungi nome: "))
        y = str(input("Aggiungi quantità"))
        z = str(input("Aggiungi prezzo"))