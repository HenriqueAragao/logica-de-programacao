Algoritmo "Exercicio16_Vida_Fumante"
// Disciplina  : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Calcula a redução de vida em dias devido ao fumo
// Autor(a)    : Luiz Henrique Santos Aragao
// Data atual  : 24/03/2026

Var
 cigarros_dia, anos_fumando: inteiro
 total_cigarros, minutos_perdidos, dias_perdidos: real

Inicio

//Entrada de Dados
escrevaL("CALCULO DE REDUÇÂO DE VIDA")
escrevaL("--------------------")

escreva("Quantos cigarros você fuma por dia? ")
leia(cigarros_dia)
escreva("Fuma há quantos anos")
leia(anos_fumando)

// Cálculo do total de cigarros na vida (considerando anos de 365 dias)
total_cigarros <- cigarros_dia * anos_fumando * 365

//Cada cigarro tira 10 minutos de vida
minutos_perdidos <- total_cigarros * 10

//Convertendo minutos para dias (1 dia = 24h * 60min = 1440 min)
dias_perdidos <- minutos_perdidos / 1440

escrevaL("--------------------")
escrevaL("Você ja fumou aproximadamente ", total_cigarros, " cigarros. ")
escrevaL("Estimativa de vida perdida: ", dias_perdidos:5:1, " dias.")

Fimalgoritmo