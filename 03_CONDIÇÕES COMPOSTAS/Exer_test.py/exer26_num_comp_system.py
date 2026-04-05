# Passo 03 - Exercício 26
# Escreva um algoritmo que leia dois números inteiros e compare-os.
# Numerical comparison system.

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 > n2:
    print("O primeiro valor é o maior")
elif n2 > n1:
    print("O segundo valor é o maior")
else:
    print("Não existe valor maior, os dois são iguais")