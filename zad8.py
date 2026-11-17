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
