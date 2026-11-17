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


