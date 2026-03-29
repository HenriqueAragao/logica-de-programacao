# Passo 02 - Exercício 24
# Calcule o preço da passagem: R$0.50/Km para até 200Km e R$0.45/Km para viagens mais longas.
# Travel ticket price based on trip distance

distance = float(input("Enter travel distance (Km): "))

if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45

print(f"For a {distance}Km trip, the ticket price is: R${price:.2f}")