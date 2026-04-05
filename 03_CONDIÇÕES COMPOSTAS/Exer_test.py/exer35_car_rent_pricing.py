# Passo 03 - Exercício 35
# Aluguel de carros Popular vs Luxo
tipo = input("Tipo de carro (popular ou luxo): ").strip().lower()
dias = int(input("Quantos dias de aluguel? "))
km = float(input("Quantos Km percorridos? "))

if tipo == "popular":
    custo_dia = dias * 90
    if km <= 100:
        custo_km = km * 0.20
    else:
        custo_km = km * 0.10
else: # luxo
    custo_dia = dias * 150
    if km <= 200:
        custo_km = km * 0.30
    else:
        custo_km = km * 0.25

total = custo_dia + custo_km
print(f"O valor total do aluguel ficou em R${total:.2f}")