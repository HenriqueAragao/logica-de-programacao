Algoritmo "Exercicio13_Aumento_Salarial"
// Disciplina  : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Calcula 15% de aumento sobre o salário de um funcionário
// Autor(a)    : Luiz Henrique Santos Aragao
// Data atual  : 24/03/2026

Var
 salario, aumento, novo_salario: real

Inicio

escrevaL("REAJUSTE SALARIAL (15%)")
escrevaL("--------------------")

escrevaL("Salario atual: R$ ")
leia(salario)

// Cálculo de aumento
aumento <- salario * 15 / 100
novo_salario <- salario + aumento

escrevaL("--------------------")
escrevaL("Aumento de: R$ ", aumento:5:2)
escrevaL("Novo salário: R$ ", novo_salario:5:2)

Fimalgoritmo