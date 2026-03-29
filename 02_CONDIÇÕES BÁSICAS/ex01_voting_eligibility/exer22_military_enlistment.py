# Passo 02 - Exercício 22
# Leia o ano de nascimento e informe se já passou, se é tempo ou quanto falta para o alistamento militar.
# Military enlistment status based on age

birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year

if age < 18:
    years_left = 18 - age
    print(f"You are {age} years old. Missing {years_left} years for enlistment.")
elif age == 18:
    print(f"You are {age} years old. It's time to enlist!")
else:
    years_past = age - 18
    print(f"You are {age} years old. It's been {years_past} years since your enlistment period.")