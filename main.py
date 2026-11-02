def fråga(fråga, alt1, alt2, alt3, svar):
    print(f"{fråga}")
    print(f"{alt1}")
    print(f"{alt2}")
    print(f"{alt3}")
    if input("Ditt val: ") == str(svar):
        print("Rätt!")
    else:
        print("Fel")
    
fråga("Vilken huvudstad har Sverige?", "Oslo", "Stockholm", "Köpenhamn", "2")