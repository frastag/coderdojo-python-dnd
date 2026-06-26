# 🐉 Incontro 2 – Il Combattimento Inizia!
## Operatori di confronto e if/else

---

## 📖 Capitolo 2 — Il Sentiero del Bosco

*Con la scheda dell'eroe pronta, partite verso il primo frammento della Pergamena, nascosto in una radura del bosco. Ma sul sentiero vi blocca un **Goblin Guardiano**, armato di una clava arrugginita. Per proseguire dovrete affrontarlo: il vostro attacco riuscirà a superare la sua difesa, o sarà lui a respingervi?*

🎯 **Oggi:** insegnate al programma a "decidere" cosa succede in base ai numeri, proprio come deve decidere il vostro eroe.

---

## ⚖️ Slide 1 — Operatori di confronto

Per confrontare due valori usiamo:
- `>` maggiore di
- `<` minore di
- `>=` maggiore o uguale
- `<=` minore o uguale
- `==` uguale a (attenzione: doppio uguale!)
- `!=` diverso da

Esempi:
```python
print(5 > 3)    # True
print(5 == 3)   # False
print(5 != 3)   # True
```

---

## 🤔 Slide 2 — True e False

Il risultato di un confronto è sempre **True** o **False**.
Questo tipo si chiama **booleano**.

```python
vita = 10
print(vita > 0)   # True
```

---

## 🔀 Slide 3 — `if`: prendere decisioni

```python
vita = 10

if vita > 0:
    print("Il personaggio è vivo!")
```

⚠️ Attenzione:
- i due punti `:` alla fine della riga
- il rientro (indentazione) della riga sotto

---

## ↔️ Slide 4 — `if` ... `else`

```python
vita = 0

if vita > 0:
    print("Il personaggio è vivo!")
else:
    print("Il personaggio è morto!")
```

---

## 🔁 Slide 5 — `elif`: più possibilità

```python
vita = 5

if vita > 15:
    print("In ottima forma!")
elif vita > 0:
    print("Ferito, ma vivo!")
else:
    print("Sconfitto!")
```

---

## ⚔️ Slide 6 — Esempio: attacco vs difesa

```python
attacco = 8
difesa_nemico = 5

if attacco > difesa_nemico:
    print("Colpo riuscito!")
else:
    print("Il nemico para il colpo!")
```

---

## 🎯 Slide 7 — La vostra missione

1. Aggiungi alla scheda personaggio una variabile `difesa_nemico`
2. Confronta `attacco` (tuo) con `difesa_nemico`
3. Stampa un messaggio diverso se il colpo va a segno o viene parato
4. Bonus: controlla anche se `vita <= 0` e stampa "Sei stato sconfitto!"

---

## 🎯 Slide 8 — Il modulo random

1. Per simulare scelte casuali usiamo il modulo `random`
2. Questo modulo può essere usato sia per simulare scelte casuali tra numeri (ad esempio il tiro di dati), ma anche scelte casuali tra stringhe all'interno di un array (ad esempio la scelta casuale della classe del nostro personaggio)

Esempio di modulo random per la selezione di un numero casuale

```python
import random

dado = random.randint(1, 20)
print("Hai tirato:", dado)

randint(1, 20)  # restituisce un numero intero a caso tra 1 e 20 (compresi).
```

Esempio di modulo random per la selezione casuale della classe di un personaggio

```python
import random

classi_disponibili = ["guerriero", "ladro", "mago"] # dichiarazione array con le classi disponibili
classe = random.choice(classi_disponibili) # restituisce una classe casuale tra quelle disponibili
```

---

## 📝 Riassunto dell'incontro

- `>`, `<`, `==`, `!=`, `>=`, `<=` → confrontano due valori e danno True/False
- `if` esegue codice solo se una condizione è vera
- `else` esegue codice quando la condizione è falsa
- `elif` permette di controllare più condizioni in sequenza
- Attenzione a `:` e all'indentazione!
- `import random` → per importare il modulo per le generazioni casuali di numeri o stringhe (a partire da un insieme di numeri o stringhe)
- `randint(1, 20)` restituisce un numero da 1 a 20 in maniera casuale
- `random.choice(classi_disponibili)` → restituisce uno dei valori inseriti nella variabile `classi_disponibili` in maniera casuale
