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

