Algoritmo "Exercicio03_Nome_Salario"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Lê o nome e o salário de um funcionário e exibe os dados formatados
// Autor(a)    : Luiz Henrique Santos Aragao
// Data atual  : 22/03/2026
Var
// Declarando as variáveis (as "caixas" de memória)
nome: caractere
salario: real

Inicio
// Entrada de Dados
escreva("Nome do Funcionario:")
leia(nome)

escreva("Salario: ")
leia(salario)

// Saida de Dados com formatação
// O ":5:2" diz ao VisuAlg: use 5 espaços e 2 casas decimais
escreva("O funcionario ", nome, " tem um salario de R$", salario:5:2, " em junho.")

Fimalgoritmo