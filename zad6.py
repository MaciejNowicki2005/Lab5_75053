# ZAD6
from math import sqrt
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


