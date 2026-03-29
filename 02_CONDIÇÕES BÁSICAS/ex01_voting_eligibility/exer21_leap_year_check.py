# Passo 02 - Exercício 21
# Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO.
# Check if a year is a leap year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is a LEAP YEAR.")
else:
    print(f"The year {year} is NOT a leap year.")