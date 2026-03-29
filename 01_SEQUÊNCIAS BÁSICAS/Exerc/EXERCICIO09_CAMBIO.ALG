Algoritmo "Exercicio09_Cambio"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Converte Real para Dólar (Cotação 5.23)
// Autor(a)    : Luiz Henrique Santos Aragao
// Data atual  : 24/03/2026

Var
reais, dolares: real

Inicio
// Entrada de Dados
escreva("Quanto dinheiro voce tem na carteira? R$ ")
leia(reais)

//Processamento
dolares <- reais / 5.23

//Saida de Dados
escreva("Com R$ ", reais:5:2, " você pode comprar US$ ", dolares:5:2)

Fimalgoritmo