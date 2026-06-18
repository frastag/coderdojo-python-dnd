def main():
    nome = input("Inserisci il nome del tuo personaggio\n")
    classe = input("Inserisci la classe del tuo personaggio: Mago, Guerriero, Ladro\n")
    if classe != "Guerriero" and classe != "Ladro" and classe != "Mago":
        classe = "Mago"  # se la classe inserita non è tra quelle disponibili, viene assegnata una classe di default
    vita = 20
    forza = 5
    magia = 15
    animale = "Topo"
    print("Benvenuto", nome, "la classe del tuo personaggio è", classe, "e hai", vita, "punti vita,", forza,
          "punti forza,", magia, "punti magia e come animale hai", animale)


if __name__ == "__main__":
    main()
