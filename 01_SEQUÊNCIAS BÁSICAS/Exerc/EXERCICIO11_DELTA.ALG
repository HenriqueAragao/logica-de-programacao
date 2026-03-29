Algoritmo "Exercicio11_Delta"
// Disciplina  : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Calcula o valor de Delta (B² - 4AC)
// Autor(a)    : Luiz Henrique Santos Aragao
// Data atual  : 24/03/2026

Var
 a, b, c, delta: real

Inicio
// Entrada de Dados
escreva("Informe o valor A: ")
leia(a)
escreva("Informe o valor B: ")
leia(b)
escreva("Informe o valor C: ")
leia(c)

//Processamento
//Delta = B ao quadrado menos 4 vezes A vezes C
delta <- (b ^ 2) - (4 * a * c)

//Saida de Dados
escrevaL("--------------------")
escrevaL("O valor de Delta é: ", delta:5:2)

Fimalgoritmo