# Passo 02 - Exercício 18
# Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade e diga se ela pode ou não votar.
# Voting eligibility check based on birth year

birth_year = int(input("Enter birth year: "))
age = 2026 - birth_year

if age >= 16:
    print(f"Age: {age}. You can vote!")
else:
    print(f"Age: {age}. You cannot vote yet.")