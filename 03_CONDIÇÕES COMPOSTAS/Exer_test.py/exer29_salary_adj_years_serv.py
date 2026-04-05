# Passo 03 - Exercício 29
# Reajuste salarial baseado no tempo de empresa.
# Salary adjustment based on years of service.
nome = input("Nome do funcionário: ") 
salario = float(input("Salário atual: R$")) 
anos = int(input("Anos na empresa: ")) 

if anos < 3:
    novo_salario = salario * 1.03
elif 3 <= anos < 10:
    novo_salario = salario * 1.125
else:
    novo_salario = salario * 1.20

print(f"Novo salário de {nome}: R${novo_salario:.2f}")