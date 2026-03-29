Algoritmo "Exercicio06_Vizinhos"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Lê um número inteiro e exibe o seu antecessor e seu sucessor.
// Autor(a)    : Luiz Henrique Santos Aragao
// Data atual  : 22/03/2026
Var

num, ant, suc: inteiro

Inicio

// Entrada de Dados
escreva("Digite um numero: ")
leia(num)

//Processamento
ant <- num - 1
suc <- num + 1

//Saida de Dados
escrevaL("O antecessor de ", num, " é ", ant)
escrevaL("O sucessor de ", num, " é ", suc)

Fimalgoritmo