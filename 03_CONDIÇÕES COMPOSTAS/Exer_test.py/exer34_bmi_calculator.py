# Passo 03 - Exercício 34
# Índice de Massa Corpórea (IMC)
peso = float(input("Qual é seu peso? (kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / (altura ** 2)

print(f"O seu IMC é de {imc:.1f}")

if imc < 18.5:
    print("Você está ABAIXO DO PESO.")
elif 18.5 <= imc < 25:
    print("Você está no PESO IDEAL.")
elif 25 <= imc < 30:
    print("Você está em SOBREPESO.")
elif 30 <= imc < 40:
    print("Você está em OBESIDADE.")
else:
    print("Você está em OBESIDADE MÓRBIDA, cuidado!")