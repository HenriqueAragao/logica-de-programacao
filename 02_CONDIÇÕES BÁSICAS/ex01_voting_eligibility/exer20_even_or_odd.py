# Passo 02 - Exercício 20
# Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.
# Check if an integer number is even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"The number {number} is EVEN.")
else:
    print(f"The number {number} is ODD.")