
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

