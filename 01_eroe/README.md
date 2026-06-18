# 🐉 Lezione 1 – Creiamo il Nostro Eroe!
## Variabili e tipi di dato in Python

---

## 📖 Capitolo 1 — Il Richiamo

*Il vecchio mago **Alarion**, guardiano di Pietraverde, vi convoca nella sua torre. La grande Pergamena che proteggeva il villaggio si è spezzata in 5 frammenti, dispersi nei dintorni, e le creature della foresta iniziano ad avvicinarsi alle mura. Alarion vi chiede di diventare eroi e di scrivere il vostro nome nel Libro degli Eroi, insieme alla vostra classe e alle vostre caratteristiche.*

🎯 **Oggi:** create la vostra scheda personaggio, il primo passo della vostra avventura.

---

## 📦 Slide 1 — Cos'è una variabile?

Immagina una **scatola con un'etichetta**.

- L'etichetta è il **nome** della variabile
- Dentro la scatola c'è il **valore**
- Puoi **cambiare** il contenuto quando vuoi

**Esempio dal mondo reale:**
Una scatola etichettata "età" oggi contiene 10. Il prossimo compleanno, ci scrivi 11. La scatola è sempre la stessa, ma il contenuto cambia.

---

## 🔤🔢 Slide 2 — I tipi di dato

Oggi useremo due tipi principali:

- **Testo (stringa)** → si scrive tra virgolette: `"Mago"`, `"Excalibur"`
- **Numero (intero)** → si scrive senza virgolette: `25`, `100`

💡 Domanda per la classe: "Aria" è una stringa o un numero? E 7?

---

## ✍️ Slide 3 — Creare una variabile

```python
nome_variabile = valore
```

Esempi:
```python
nome = "Aria"
vita = 20
classe = "Mago"
```

⚠️ Regole per i nomi delle variabili:
- niente spazi (usa `_` invece, es. `punti_vita`)
- niente accenti o simboli strani
- non può iniziare con un numero

---

## 🗣️ Slide 4 — Far parlare il computer: `print()`

```python
print("Ciao avventuriero!")

nome = "Aria"
print(nome)

vita = 20
print("Punti vita:", vita)
```

---

## ❓ Slide 5 — Chiedere qualcosa al giocatore: `input()`

```python
nome = input("Come si chiama il tuo eroe? ")
print("Benvenuto,", nome, "!")
```

Quello che scrive il giocatore viene salvato nella variabile!

---

## 🛡️ Slide 6 — Oggi creiamo: la Scheda del Personaggio!

Ogni eroe avrà:
- **Nome**
- **Classe** (Guerriero / Mago / Ladro)
- **Punti Vita**
- **Forza**
- **Magia**

---

## 🧙 Slide 7 — Esempio: la scheda di un eroe

```python
nome = "Aria"
classe = "Mago"
vita = 20
forza = 5
magia = 15

print("=== SCHEDA PERSONAGGIO ===")
print("Nome:", nome)
print("Classe:", classe)
print("Vita:", vita)
print("Forza:", forza)
print("Magia:", magia)
```

---

## 🎯 Slide 8 — La vostra missione

1. Crea le variabili della tua scheda personaggio
2. Usa `input()` per scegliere nome e classe
3. Stampa la scheda con `print()`
4. Bonus: aggiungi una variabile extra (arma, animale magico, oro...)

---

## 📝 Riassunto dell'incontro

- Variabile = scatola con etichetta che contiene un valore
- Stringhe = testo tra virgolette, Numeri = senza virgolette
- `print()` mostra cose a schermo
- `input()` chiede cose al giocatore
- Oggi: prima versione della Scheda Personaggio!
