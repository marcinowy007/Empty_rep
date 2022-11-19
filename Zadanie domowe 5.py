

def szyfruj(tekst):
    try:
        str(tekst)
    except:
        print("Podany argument nie może zostać potraktowany jako tekst.")
    print("Za pomocą jakiego szyfru chcesz szyfrować podany tekst?")
    inp = input("GADERYPOLUKI (G), POLITYKARENU (P), własny szyfr użytkownika (U) \nTu wpisz odpowiednią literę: ").lower()
    if inp == "u":
        szyfr_user = input("Podaj szyfr: ").lower()
        #sprawdzenie szyfru
        if len(szyfr_user)%2 != 0:
            print("Podany szyfr zawiera niepoprwaną liczbę liter.")
            return
        elif len(set(szyfr_user)) != len(szyfr_user):
            print("Podany szyfr zawiera powtarzające się litery.")
            return
        szyfr = {}
        for i in range(0, len(szyfr_user), 2):
            szyfr[szyfr_user[i]] = szyfr_user[i+1]
            szyfr[szyfr_user[i+1]] = szyfr_user[i]

    elif inp == "g":
        szyfr1 = {"g": "a", "d": "e", "r": "y", "p": "o", "l": "u", "k": "i"}
        szyfr2 = {v: k for k, v in szyfr1.items()}
        szyfr = szyfr1 | szyfr2
    elif inp == "p":
        szyfr1 = {"p": "o", "l": "i", "t": "y", "k": "a", "r": "e", "n": "u"}
        szyfr2 = {v: k for k, v in szyfr1.items()}
        szyfr = szyfr1 | szyfr2
    else:
        print("Nie podano prawidłowej litery")
        return
    wynik = ""
    tekst = tekst.lower()
    for znak in tekst:
        try:
            wynik += szyfr[znak]
        except:
            wynik += znak
    print(wynik)
    return wynik

szyfruj("Ala ma kota")