# Passo 03 - Exercício 30
# Triangle type determination (Equilateral, Isosceles, Scalene).
a = float(input("Lado A: ")) 
b = float(input("Lado B: ")) 
c = float(input("Lado C: ")) 

if a < b + c and b < a + c and c < a + b: 
    print("Pode formar um triângulo: ", end="")
    if a == b == c:
        print("EQUILÁTERO") 
    elif a == b or a == c or b == c:
        print("ISÓSCELES")
    else:
        print("ESCALENO")
else:
    print("Não é possível formar um triângulo.")