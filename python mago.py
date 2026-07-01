import random

classi = ["Guerriero", "Mago", "Ladro", "Criceto"]
sceltaclasse = random.choice(classi)
#Statistiche.
nome = input("Come si chiama il tuo eroe? ")
#Indicare meglio la lista delle classi e mostrare anche le stat di ogni classe, SPECIALMENTE il criceto perché fa cagare.
classe = input("E qual'è la tua classe?                 Classi: Guerriero, Mago, Ladro e Criceto ")
if classe=="Guerriero":
    pv = 200
    forza = 60
    psi = 0
elif classe=="Mago":
    pv = 100
    forza = 30
    psi = 60
elif classe=="Ladro":
    pv = 130
    forza = 45
    psi = 30
elif classe=="Criceto":
    pv = 20
    forza = 5
    psi = 0
#Scelta classe casuale.
else :
    classe_rand = random.randint(1,4)
    print("La tua classe è stata scelta casualmente. La tua classe è:", sceltaclasse)
    classe=sceltaclasse
if classe=="Guerriero":
    pv = 200
    forza = 60
    psi = 0
elif classe=="Mago":
    pv = 100
    forza = 30
    psi = 60
elif classe=="Ladro":
    pv = 130
    forza = 45
    psi = 30
elif classe=="Criceto":
    pv = 10
    forza = 5
    psi = 0
#Intro.
print("Benvenuto,", nome, "!", "i tuoi punti vita sono", pv, ",", "la tua forza è", forza, ",", "la tua magia è", psi, ".")
print("Buona fortuna!")

azione = input("Un goblin ti ferma, tu cosa fai? ")
if azione=="Attacca":
    dadoAtt=random.randint(1,20)
    print("Il risultato è:", dadoAtt)
    if dadoAtt==1:
        print("Il colpo fallisce miseramente..")
    elif dadoAtt==20:
            print("COLPO CRITICO!")
    else:
        print("Il colpo è di successo!")
elif azione=="Magia" and psi>1:
    dadoPsi=random.randint(1,6)
    print("Il risultato è:",dadoPsi)
    if dadoPsi==1:
        print("La magia fallisce miseramente...")
    elif dadoPsi==6:
        print("SEGNAPOSTO TEMPORANEO MESSAGGIO MAGIA 6")
    else:
        print("La magia è di successo!")
#Questo è il goblin.
ps_nemico1= 18