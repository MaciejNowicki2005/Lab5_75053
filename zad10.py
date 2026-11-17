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

