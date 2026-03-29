Algoritmo "Exercicio12_Desconto"
// Disciplina  : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Calcula 5% de desconto sobre o preço de um produto
// Autor(a)    : Luiz Henrique Santos Aragao
// Data atual  : 24/03/2026

Var
 preco, desc, preco_final: real

Inicio

escrevaL("SISTEMA DE DESCONTO (5%)")
escrevaL("--------------------")

// Entrada de Dados
escreva("Digite o preço do produto: ")
leia(preco)

//Processamento
desc <- preco * 5 / 100
preco_final <- preco - desc

//Saida de Dados
escrevaL("--------------------")
escrevaL("Preco original: R$ ", preco:5:2)
escrevaL("Valor do Desconto: R$ ", desc:5:2)
escrevaL("Preco Promocional: R$ ", preco_final:5:2)

Fimalgoritmo