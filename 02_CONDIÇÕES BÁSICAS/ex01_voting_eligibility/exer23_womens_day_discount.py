# Passo 02 - Exercício 23
# Leia nome, sexo e valor de compras. Aplique 5% de desconto para homens e 13% para mulheres.
# Women's Day special discount calculator

name = input("Customer name: ")
gender = input("Gender [M/F]: ").upper()
purchase_value = float(input("Total purchase value: R$"))

if gender == "F":
    discount = purchase_value * 0.13
    final_price = purchase_value - discount
    print(f"Happy Women's Day! 13% discount applied. Final price: R${final_price:.2f}")
else:
    discount = purchase_value * 0.05
    final_price = purchase_value - discount
    print(f"Standard 5% discount applied. Final price: R${final_price:.2f}")