# Passo 03 - Exercício 36
# Pontos por atividade física
horas = float(input("Quantas horas de atividade no mês? "))

if horas <= 10:
    pontos = horas * 2 # [cite: 124]
elif horas <= 20:
    pontos = horas * 5 # [cite: 125]
else:
    pontos = horas * 10

dinheiro = pontos * 0.05 # [cite: 126]
print(f"Você acumulou {pontos:.0f} pontos e ganhou R${dinheiro:.2f}")