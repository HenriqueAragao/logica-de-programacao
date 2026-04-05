# Passo 03 - Exercício 31
# Desafio: Jogo de JoKenPo (Pedra-Papel-Tesoura)
import random

print("=== JOKENPO ===")
print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
jogador = int(input("Qual é a sua jogada? "))

print(f"O computador escolheu: {itens[computador]}")
print(f"Jogador escolheu: {itens[jogador]}")

if computador == 0: # Pedra
    if jogador == 0: print("EMPATE!")
    elif jogador == 1: print("JOGADOR VENCE!")
    elif jogador == 2: print("COMPUTADOR VENCE!")
elif computador == 1: # Papel
    if jogador == 0: print("COMPUTADOR VENCE!")
    elif jogador == 1: print("EMPATE!")
    elif jogador == 2: print("JOGADOR VENCE!")
elif computador == 2: # Tesoura
    if jogador == 0: print("JOGADOR VENCE!")
    elif jogador == 1: print("COMPUTADOR VENCE!")
    elif jogador == 2: print("EMPATE!")