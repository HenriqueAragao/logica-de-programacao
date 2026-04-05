# Passo 03 - Exercício 28
# Leia largura e comprimento de um terreno e mostre a classificação da área.
# Land area calculation and classification.
largura = float(input("Largura (m): ")) 
comp = float(input("Comprimento (m): ")) 
area = largura * comp

print(f"Área: {area:.1f}m²") 
if area < 100:
    print("Classificação: TERRENO POPULAR") 
elif 100 <= area <= 500:
    print("Classificação: TERRENO MASTER") 
else:
    print("Classificação: TERRENO VIP") 