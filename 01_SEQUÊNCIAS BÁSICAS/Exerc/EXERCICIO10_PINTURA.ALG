Algoritmo "Exercicio10_Pintura"
// Disciplina  : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Calcula a área de uma parede e a quantidade de tinta necessária
// Autor(a)    : Luiz Henrique Santos Aragao
// Data atual  : 24/03/2026

Var
larg, alt, area, tinta: real

Inicio
// Entrada de Dados
escrevaL("--- SISTEMA DE CÁLCULO DE PINTURA ---")
escreva("Largura da parede (em metros): ")
leia(larg)
escreva("Altura da parede (em metros): ")
leia(alt)

//Processamento
area <- larg * alt
tinta <- area / 2

//Saida de Dados
escrevaL("----------------------------------------")
escrevaL("Área total a ser pintada: ", area:5:2, " metros quadrados.")
escrevaL("Quantidade de tinta necessária: ", tinta:5:2, " litros. ")
escrevaL("----------------------------------------")

Fimalgoritmo