# Passo 02 - Exercício 25
# [DESAFIO] Leia o comprimento de três retas e diga se elas podem formar um triângulo.
# Triangle inequality theorem check

s1 = float(input("First segment: "))
s2 = float(input("Second segment: "))
s3 = float(input("Third segment: "))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("Yes, these segments CAN form a triangle.")
else:
    print("No, these segments CANNOT form a triangle.")