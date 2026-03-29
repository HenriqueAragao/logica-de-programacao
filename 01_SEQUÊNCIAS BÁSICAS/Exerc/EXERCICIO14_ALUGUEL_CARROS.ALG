Algoritmo "Exercicio14_Aluguel_Carros"
// Disciplina  : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Calcula o pre�o total do aluguel de um carro
// Autor(a)    : Luiz Henrique Santos Aragao
// Data atual  : 24/03/2026

Var
 dias: inteiro
 km, preco_total: real

Inicio

escrevaL("LOCADORA DE VEICULOS")
escrevaL("--------------------")

escrevaL("Dias alugados: ")
leia(dias)
escrevaL("Km percorridos: ")
leia(km)

// C�lculo: R$90 por dia + R$0.20 por Km
preco_total <-(dias * 90) + (km * 0.20)

escrevaL("--------------------")
escrevaL("Total a pagar: R$ ", preco_total:5:2)

Fimalgoritmo