poäng=0
max_poäng=0

def fråga(fråga, alt1, alt2, alt3, svar):
    global poäng
    global max_poäng
    print(f"{fråga}")
    print(f"{alt1}")
    print(f"{alt2}")
    print(f"{alt3}")
    if input("Ditt val: ") == str(svar):
        print(f"Rätt!\n")
        poäng+=1
        max_poäng+=1
    else:
        if svar == "1":
            print(f"Fel, rätt svar var {alt1}\n")
        elif svar == "2":
            print(f"Fel, rätt svar var {alt2}\n")
        elif svar == "3":
            print(f"Fel, rätt svar var {alt3}\n")
        max_poäng+=1 

fråga("Vilken huvudstad har Norge?", "Oslo", "Bergen", "Trondeim", "1")
fråga("Vilket år började andra världskriget?", "1914", "1939", "1945", "2")
print(f"Du fick {poäng} av {max_poäng} rätt")  