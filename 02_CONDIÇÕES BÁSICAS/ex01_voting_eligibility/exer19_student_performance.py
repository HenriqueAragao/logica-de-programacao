# Passo 02 - Exercício 19
# Leia o nome e as duas notas de um aluno, calcule a média e mostre se ele teve um bom aproveitamento (média >= 7.0).
# Student academic performance and average calculation

name = input("Student name: ")
n1 = float(input("Grade 1: "))
n2 = float(input("Grade 2: "))
average = (n1 + n2) / 2

print(f"Average: {average:.1f}")
if average >= 7.0:
    print(f"Great job, {name}! You had a good performance.")
else:
    print(f"Keep studying, {name}. You can do better!")