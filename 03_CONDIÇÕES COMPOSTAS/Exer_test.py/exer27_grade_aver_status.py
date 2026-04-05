# Passo 03 - Exercício 27
# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando a situação.
# Student grade average and status.
nota1 = float(input("Primeira nota: ")) 
nota2 = float(input("Segunda nota: ")) 
media = (nota1 + nota2) / 2

if media >= 7.0:
    print(f"Média {media:.1f}: APROVADO")
elif 5.0 <= media <= 6.9:
    print(f"Média {media:.1f}: RECUPERAÇÃO")
else:
    print(f"Média {media:.1f}: REPROVADO")