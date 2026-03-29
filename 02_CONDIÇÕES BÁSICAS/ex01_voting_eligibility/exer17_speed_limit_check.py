# Passo 02 - Exercício 17
# Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, 
# exiba uma mensagem dizendo que o usuário foi multado e o valor da multa (R$5 por Km acima).
# Traffic fine system and speed limit check

speed = float(input("Enter the car speed (Km/h): "))

if speed > 80:
    print("ALERTA: You were ticketed!")
    excess = speed - 80
    fine = excess * 5
    print(f"Fine amount: R${fine:.2f}")
else:
    print("Safe: Speed within limit. Have a safe trip!")