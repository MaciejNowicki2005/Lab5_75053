
from math import sqrt

# ZAD1
def kwadrat(liczba):
    return liczba * liczba

kwadratowana = kwadrat(int(input("Podaj liczbę do kwadratowania: ")))
print("Kwadrat twojej liczby: ", kwadratowana)


# ZAD2
# Opcja 1
def odwracanie(doOdwracanie):
    odwocone = ""
    for i in range(len(doOdwracanie)-1, -1, -1):
        odwocone += doOdwracanie[i]
    return odwocone

lDoOdwrocenia = input("Podaj stringa do odwrócenia: ")
print(odwracanie(lDoOdwrocenia))

# Opcja 2
def odwracanie(odwracanie):
    return odwracanie[::-1]

lDoOdwrocenia = input("Podaj stringa do odwrócenia: ")
print(odwracanie(lDoOdwrocenia))


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

# ZAD4
def srednia(liczby):
    return sum(liczby) / len(liczby)

liczby = []
while True:
    try:
        liczby.append(int(input("Dodaj liczbe do średniej (jeśli chcesz skończyć wpisz cokolwiek): ")))
    except ValueError:
        break
if liczby == []:
    print("Brak liczb")
else:
    print(srednia(liczby))


# ZAD5
def BMI(wzrost, masa):
    bmi = round(masa / (wzrost * wzrost) * 10000, 2)
    print("BMI:", bmi)

    if bmi < 18.5:
        return "Niedowaga"
    elif 18.5 <= bmi < 25:
        return "Parametry ciała prawidłowe"
    elif 25 <= bmi < 30:
        return "Nadwaga"
    elif 30 <= bmi < 35:
        return "otylosc st.1"
    elif 35 <= bmi < 40:
        return "otylosc st.2"
    else:
        return "otylosc st.3"

wzrost = int(input("Podaj wzrost: "))
waga = int(input("Podaj wage: "))
print(BMI(wzrost, waga))


# ZAD6
def poleTrojkata(a, b, c):
    try:
        if (a + b <= c) or (b + c <= a) or (c + a <= b) or (a <= 0) or (b <= 0) or (c <= 0):
            raise ValueError("Błędnie podane boki trójkąta")
    except ValueError as blad:
        print(blad)
        return None

    opolObwod = (a + b + c) / 2
    poleTrojkata = sqrt(opolObwod * (opolObwod-a) * (opolObwod-b) * (opolObwod-c))
    return poleTrojkata

try:
    a = int(input("Podaj A: "))
    b = int(input("Podaj B: "))
    c = int(input("Podaj C: "))
    print(poleTrojkata(a, b, c))
except ValueError:
    print("Z takim bokiem to trójkąta nie policzymy :(")


# ZAD7

def potegowanie(a, n):
    if n == 0 and a == 0:
        print("Symbol nieoznaczony, umownie 1")
        return 1
    elif n == 0:
        return 1
    elif a == 0 and n < 0:
        print("Nie można dzielić przez zero")
        return 0
    elif a == 0:
        return 0
    elif n < 0:
        return 1 / potegowanie(a, -n)
    else:
        return a * potegowanie(a, n-1)

a = int(input("Podaj podstawę potęgi: "))
n = int(input("Podaj wykładnik potęgi: "))
print(f"Twoja potęga to: {potegowanie(a,n)}")

#ZAD8

def wyswietl(*liczby):
    for i in liczby:
        print(i)

def maksimum(*liczby):
    for i in liczby:
        print(i)
    if len(liczby) == 0:
        return "Brak liczb"
    else:
        return max(liczby)

liczby = []
while True:
    try:
        liczby.append(int(input("Dodaj liczbe (jeśli chcesz skończyć wpisz cokolwiek):")))
    except ValueError:
        break
print("Liczby w zbiorze:")
wyswietl(*liczby)
print("____________________________________________")
print("Maksimum:", maksimum(*liczby))

#ZAD9


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n<0:
        return None
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Podaj który element ciągu Fibbonaciego chcesz otrzymać:"))
print("Element ",n,":",fibonacci(n))

#ZAD10


def wspolne(lista1, lista2):
    return list(set(lista1) & set(lista2))

print("Podaj elementy dla listy1:")
lista1 = []
while True:
    try:
        lista1.append(int(input("Dodaj liczbe (jeśli chcesz skończyć wpisz cokolwiek):")))
    except ValueError:
        break
print("Podaj elementy dla listy2:")
lista2 = []
while True:
    try:
        lista2.append(int(input("Dodaj liczbe (jeśli chcesz skończyć wpisz cokolwiek):")))
    except ValueError:
        break
print("Elemnty wspólne obu list:")
print(wspolne(lista1, lista2))

