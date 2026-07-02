# 🐉 Lezione 3 – I Dadi del Destino!
## Operatori booleani e numeri casuali
 
---

## 📖 Capitolo 3 — La Foresta dei Sussurri

*Sconfitto il Goblin, recuperate il primo frammento e proseguite nella **Foresta dei Sussurri**, un luogo magico e imprevedibile dove la fortuna conta quanto la forza. Qui ogni colpo viene deciso dal lancio dei dadi: un tiro fortunato può diventare leggendario, uno sfortunato può fallire miseramente.*

🎯 **Oggi:** i dadi entrano ufficialmente nel gioco, insieme alle condizioni "e"/"o" che gestiscono i casi speciali.
 
---

## 🎲 Slide 1 — Il modulo `random`

Per simulare i dadi usiamo il modulo `random`.

```python
import random
 
dado = random.randint(1, 20)
print("Hai tirato:", dado)
```

`randint(1, 20)` restituisce un numero intero a caso tra 1 e 20 (compresi).
 
---

## ✅❌ Slide 2 — Operatori booleani: `and`, `or`, `not`

- `and` → vero solo se **entrambe** le condizioni sono vere
- `or` → vero se **almeno una** condizione è vera
- `not` → inverte il valore (True diventa False e viceversa)
  Esempio dalla vita reale:
  "Esco a giocare SE è sabato AND non piove"
  "Mangio il gelato SE ho finito i compiti OR è il mio compleanno"

---

## 🧮 Slide 3 — Esempi pratici

```python
piove = True
sabato = True
 
print(sabato and not piove)   # False (perché piove)
print(sabato or piove)        # True
```

💡 Far provare alla classe diverse combinazioni di True/False a voce alta.
 
---

## 🐉 Slide 4 — Colpo critico con `and`

```python
import random
 
dado = random.randint(1, 20)
ha_arma_magica = True
 
if dado == 20 and ha_arma_magica:
    print("COLPO CRITICO LEGGENDARIO!")
elif dado == 20:
    print("Colpo critico!")
else:
    print("Tiro normale:", dado)
```
 
---

## 💥 Slide 5 — Fallimento con `or`

```python
dado = random.randint(1, 20)
stordito = False
 
if dado == 1 or stordito:
    print("Il colpo fallisce miseramente!")
else:
    print("Il colpo parte!")
```
 
---

## 🎯 Slide 6 — La vostra missione

1. Importa `random` e tira un d20 per il tuo attacco
2. Se il dado è 20 → "Colpo critico!"
3. Se il dado è 1 → "Fallimento totale!"
4. Altrimenti → confronta come nella Lezione 2 (`attacco` vs `difesa_nemico`)
5. Bonus: usa `and`/`or` per aggiungere una condizione speciale (es. arma magica, scudo rotto...)
 
---

## 📝 Riassunto dell'incontro

- `random.randint(a, b)` restituisce un numero intero a caso tra a e b
- `and` → tutte le condizioni devono essere vere
- `or` → basta una condizione vera
- `not` → inverte True/False
- Oggi: i dadi entrano nel gioco!
 