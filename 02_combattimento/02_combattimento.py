import random

classi_disponibili = ["guerriero", "ladro", "mago"]
vita = 20

nome = input("Inserisci il nome del tuo personaggio\n")
classe = input("Inserisci la classe del tuo personaggio: Mago, Guerriero, Ladro\n")

# miglioramento rispetto alla versione scorsa: controlliamo se la classe inserita dall'utente è
# corretta, usando una lista di classi disponibili e controllando se quanto inserito dall'utente
# non è al suo interno e rendendo il tutto case insensitive
if not classe.lower() in classi_disponibili: # uso lower per non tenere in considerazione se le lettere sono maiuscole o minuscole
    # se la classe non è tra quelle valide, viene selezionata in maniera random
    classe = random.choice(classi_disponibili)

# in base alla classe cambiano i punti forza e magia. Vita sono sempre uguaali
if classe.lower() == "guerriero":
    forza = 10
    magia = 0
elif classe.lower() == "ladro":
    forza = 5
    magia = 5
else:
    forza = 0
    magia = 10

print("Benvenuto", nome, "la classe del tuo personaggio è", classe, "e hai", vita, "punti vita,", forza,
      "punti forza,", magia, "punti magia.")

# Esempio di attacco e difesa nemico
attacco = 10
difesa_nemico = 3

if attacco > difesa_nemico:
    print("Attacco perfetto!")
elif attacco <= difesa_nemico:
    print("Il memico ha parato il tuo attacco!")
