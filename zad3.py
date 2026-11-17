# ZAD3
def witaj(jezyk="polski", imie="Użytkowniku"):
    if jezyk == "angielski":
        return f"Hello, {imie}"
    elif jezyk == "niemiecki":
        return f"Guten Morgen, {imie}"
    elif jezyk == "polski":
        return f"Cześć, {imie}"
    else:
        return f"Witaj, {imie}"
imie=""
imie = input("Podaj imię: ")
if imie == "": imie = "Użytkowniku"
jezyk = input("Podaj język (angielski/niemiecki/polski (domyślny)): ")
#podane dane od użytkownika
print(witaj(jezyk, imie))
#dane defaultowe
print(witaj())
#a niech będzie Queen Elizabeth z Anglii
print(witaj( "angielski","Elizabeth"))

