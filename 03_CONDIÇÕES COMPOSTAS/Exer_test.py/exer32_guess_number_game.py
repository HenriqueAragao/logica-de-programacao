# Passo 03 - Exercício 32
# Desafio: Sorteio de número entre 1 e 5
import random

computador = random.randint(1, 5)
print("Vou pensar em um número entre 1 e 5. Tente adivinhar!")
jogador = int(input("Em que número eu pensei? "))

if jogador == computador:
    print(f"PARABÉNS! Você acertou, eu pensei no {computador}.")
else:
    print(f"GANHEI! Eu pensei no número {computador} e não no {jogador}!")