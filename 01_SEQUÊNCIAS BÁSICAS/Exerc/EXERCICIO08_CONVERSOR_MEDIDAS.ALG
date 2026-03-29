Algoritmo "Exercicio08_Conversor_Medidas"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Converte metros para Km, Hm, Dam, dm, cm e mm
// Autor(a)    : Luiz Henrique Santos Aragao
// Data atual  : 23/03/2026

Var

m, km, hm, dam, dm, cm, mm: real

Inicio
// Entrada de Dados
escreva("Digite uma distância em metros: ")
leia(m)

//Processamento
km <- m / 1000
hm <- m / 100
dam <- m / 10
dm <- m * 10
cm <- m * 100
mm <- m * 1000

//Saida de Dados
escrevaL("A distancia de ", m, "m corresponde a:")
escrevaL(km:10:5, "km")
escrevaL(hm:10:5, "hm")
escrevaL(dam:10:5, "dam")
escrevaL(dm:10:1, "dm")
escrevaL(cm:10:1, "cm")
escrevaL(mm:10:1, "mm")

Fimalgoritmo