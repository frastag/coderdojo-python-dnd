import random

nome = input("come si chiama il tuo eroe?")
print("le classi sono: Mago, Guerriero e Ladro")
classe = input ("qual è la tua classe?")

if classe =="Mago":
    punti_vita = 35
    forza = 20
    magia = 30
elif classe== "Guerriero":
    punti_vita = 45
    forza = 40
    magia = 20
elif classe == "Ladro":
    punti_vita = 40
    forza = 25
    magia = 10
else:
    classi = ["Guerriero", "Mago", "Ladro"]
    scelta = random.choice(classi)
    classe = scelta
    if classe =="Mago":
        punti_vita = 35
        forza = 20
        magia = 30
    elif classe== "Guerriero":
        punti_vita = 45
        forza = 40
        magia = 20
    elif classe == "Ladro":
        punti_vita = 40
        forza = 25
        magia = 10
input("")
difesa_nemico_1 = 18
vita_nemico_1 = 15
attacco_nemico_1 = 20
difesa_nemico_2 = 20
vita_nemico_2 = 25
attacco_nemico_2 = 27
attacco = 8
print("benvenuto,", nome, "!", "la tua classe è:", classe, ",", "i tuoi punti vita sono", punti_vita, ",", "la tua forza è", forza, ",", "la tua magia è", magia, ".")
print("buona fortuna!")
print("ora ascolterai e diverrai parte di una storia di maghi e mostri, tu sarai il protagonista e dovrai recuperare la pergamena del Mago. Attraverserai foreste, montagne e laghi incantati e dovrai combattere contro i nemici che ti si pareranno davanti. la storia inizia ora.")
if punti_vita >10:
    print("hai moltissima vita!")
elif punti_vita > 0:
    print("ooof, sei vivo!")
elif punti_vita ==0:
    print("oh, no! sei morto!")
input("")
print("il Mago ti da un potenziamento. Ti dice anche che puoi utilizzarlo per l'Attacco Epico")
possiede_il_potenziamento = True
print("Lasci il palazzo del Mago e ti avventuri sul sentiero. Purtroppo, dopo un po', incontri uno degli scagnozzi di Orcher. Non hai scampo: devi combattere")
input("")
dado1 = random.randint(1, 20)
print("hai tirato il dado, è uscito", dado1)
if dado1 == 1:
    print("il tuo attacco fallisce!")
elif dado1 == 20 and possiede_il_potenziamento:
    print("hai lanciato il tuo Attacco Epico, e hai consumato il tuo potenziamento")
    vita_nemico_1 = 0
elif dado1 == 20:
    print("hai lanciato l'Attacco Super")
    vita_nemico_1 = 0
elif dado1 <7 and forza <8:
    print("per il rotto della cuffia hai lanciato un attacco che potrebbe salvarti")
    vita_nemico_1 = vita_nemico_1 - dado1 - forza
elif dado1 == 7:
    print("hai ottenuto un altro potenziamento, che puoi utilizzare per l'Attacco Epico")
else:
    print("hai lanciato il tuo attacco")
    vita_nemico_1 = vita_nemico_1 - attacco
input("")
dado2 = random.randint(1, 20)
print("hai tirato il dado, è uscito", dado2)
if dado2 == 1:
    print("il tuo attacco fallisce!")
elif dado2 == 20 and possiede_il_potenziamento:
    print("hai lanciato il tuo Attacco Epico, e hai consumato il tuo potenziamento")
    vita_nemico_1 = 0
elif dado2 == 20:
    print("hai lanciato l'Attacco Super")
    vita_nemico_1 = 0
elif dado2 <7 and forza <8:
    print("per il rotto della cuffia hai lanciato un attacco che potrebbe salvarti")
    vita_nemico_1 = vita_nemico_1 - dado2 - forza
elif dado2 == 7:
    print("hai ottenuto un altro potenziamento, che puoi utilizzare per l'Attacco Epico")
else:
    print("hai lanciato il tuo attacco")
    vita_nemico_1 = vita_nemico_1 - attacco
input("")
dado3 = random.randint(1, 20)
print("hai tirato il dado, è uscito", dado3)
if dado3 == 1:
    print("il tuo attacco fallisce!")
elif dado3 == 20 and possiede_il_potenziamento:
    print("hai lanciato il tuo Attacco Epico, e hai consumato il tuo potenziamento")
    vita_nemico_1 = 0
elif dado3 == 20:
    print("hai lanciato l'Attacco Super")
    vita_nemico_1 = 0
elif dado3 <7 and forza <8:
    print("per il rotto della cuffia hai lanciato un attacco che potrebbe salvarti")
    vita_nemico_1 = vita_nemico_1 - dado3 - forza
elif dado3 == 7:
    print("hai ottenuto un altro potenziamento, che puoi utilizzare per l'Attacco Epico")
else:
    print("hai lanciato il tuo attacco")
    vita_nemico_1 = vita_nemico_1 - attacco
input("")
if vita_nemico_1 <=0:
    print("hai sconfitto il nemico e ora continui il sentiero fino alla grotta dove trovi il primo pezzo della pergamena")
else:
    punti_vita = punti_vita - attacco_nemico_1
