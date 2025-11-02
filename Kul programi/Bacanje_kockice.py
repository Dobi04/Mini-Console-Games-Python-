import random
import time

kockice = {
    1: ("┌─────────┐",
        "|         |",
        "|    ●    |",
        "|         |",
        "└─────────┘"),
    2: ("┌─────────┐",
        "|  ●      |",
        "|         |",
        "|      ●  |",
        "└─────────┘"),
    3: ("┌─────────┐",
        "|  ●      |",
        "|    ●    |",
        "|      ●  |",
        "└─────────┘"),
    4: ("┌─────────┐",
        "|  ●   ●  |",
        "|         |",
        "|  ●   ●  |",
        "└─────────┘"),
    5: ("┌─────────┐",
        "|  ●   ●  |",
        "|    ●    |",
        "|  ●   ●  |",
        "└─────────┘"),
    6: ("┌─────────┐",
        "|  ●   ●  |",
        "|  ●   ●  |",
        "|  ●   ●  |",
        "└─────────┘"),
}

frames = {
    1: (  # Kockica okrenuta ivicom ka nama
        "     ______  ",
        "   /      /| ",
        "  /______//| ",
        "  |      | | ",
        "  |  ●   | /  ",
        "  |______|/   "),
    2: (  # Kockica pada na lice
        "     ______  ",
        "   /      /| ",
        "  /  ●   //| ",
        "  |      | | ",
        "  |   ●  | /  ",
        "  |______|/   "),
    3: (  # Kockica okrenuta sa 3 strane vidljive
        "     ______  ",
        "   /  ●   /| ",
        "  /______//| ",
        "  |      |●| ",
        "  |   ●  | /  ",
        "  |______|/   "),
    4: (  # Kockica rotira dalje
        "     ______  ",
        "   /      /| ",
        "  /   ●  //| ",
        "  |      | | ",
        "  | ●  ● | /  ",
        "  |______|/   "),
    5: (  # Skoro završena rotacija
        "     ______  ",
        "   /  ●   /| ",
        "  /______//| ",
        "  |  ●   |●| ",
        "  |      | /  ",
        "  |______|/   ")
}

suma = 0

while True:
    vrednost = input("Bacite kocku (pritisnite bilokoju dirku, 'i' za izadji): ").upper()
    if vrednost == "I":
        break
    else:
        nasumicna_vrednost = random.randint(1,6)

    for broj in range(0,100):
        for i in range(1,5):
            for red in frames.get(i):
                print(red)

        
    for red in kockice.get(nasumicna_vrednost):
        print(red)
    suma += nasumicna_vrednost
    print(f"Ukupna dosadasnja suma kockica koje ste bacili iznosi: {suma}")
        

print(f"Ukupna suma kockica koje ste bacili iznosi: {suma}")
