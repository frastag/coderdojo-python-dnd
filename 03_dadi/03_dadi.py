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

bonus_speciale = random.choice([True, False]) # per estrarre casualmente una scelta tra True e False posso usare random.choice con, come argomento, la lista con i due valori booleani

print("Benvenuto", nome, "la classe del tuo personaggio è", classe, "e hai", vita, "punti vita,", forza,
      "punti forza,", magia, "punti magia.")

if bonus_speciale:
    print("Hai anche ottenuto un buono speciale, che ti può essere utile in combattimento!")

dado = random.randint(1, 20)

vita_nemico = 30
difesa_nemico = random.randint(1, 20)

print("Incontri un goblin e lo vuoi attaccare, sferri un attacco di", dado, "e il nemico si difende con", difesa_nemico)

colpo_a_segno = True

if dado == 20 and bonus_speciale:
    print("Hai effettuato un colpo epico e il tuo nemico è morto!")
    vita_nemico = 0
elif dado > 1 and bonus_speciale and dado > difesa_nemico:
    print("Ottimo colpo!")
    vita_nemico = vita_nemico - dado - 1
elif dado > 1 and not bonus_speciale and dado > difesa_nemico: # potrei non inserire il not bonus_speciale, perchè è implicito, lo metto per chiarezza solo in questa condizione
    print("Ottimo colpo!")
    vita_nemico = vita_nemico - dado
else:
    print("Il tuo colpo non è andato a segno")
    colpo_a_segno = False

if colpo_a_segno:
    print("Il nemico ha ora", vita_nemico,"punti vita")

