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


