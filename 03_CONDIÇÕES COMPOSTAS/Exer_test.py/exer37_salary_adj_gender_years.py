# Passo 03 - Exercício 37
# Reajuste salarial complexo
salario = float(input("Salário atual: R$ "))
genero = input("Gênero [M/F]: ").strip().upper()
anos = int(input("Anos na empresa: "))

if genero == 'F':
    if anos < 15: novo = salario * 1.05 # [cite: 131, 132]
    elif anos <= 20: novo = salario * 1.12
    else: novo = salario * 1.23
else: # Homem
    if anos < 20: novo = salario * 1.03 # [cite: 133]
    elif anos <= 30: novo = salario * 1.13
    else: novo = salario * 1.25

print(f"Seu novo salário será de R${novo:.2f}")