Algoritmo "Exercicio05_Media"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Lê as duas notas de um aluno e exibe a sua média na disciplina
// Autor(a)    : Luiz Henrique Santos Aragao
// Data atual  : 22/03/2026

Var
nota1, nota2, media: real

Inicio

// Entrada de Dados
escreva("Nota 1: ")
leia(nota1)

escreva("Nota 2: ")
leia(nota2)

//O calcula da média é a soma das duas notas divididas por 2
media <- (nota1 + nota2) / 2

//Saida de Dados
escreva("A média entre ", nota1, " e ", nota2, " é igual a ", media)

Fimalgoritmo