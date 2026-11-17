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


