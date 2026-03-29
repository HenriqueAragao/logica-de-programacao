Algoritmo "Exercicio15_Salario_Trabalhado"
// Disciplina  : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Calcula o salário baseado em dias trabalhados (R$25/hora)
// Autor(a)    : Luiz Henrique Santos Aragao
// Data atual  : 24/03/2026

Var
 dias: inteiro
 salario: real

Inicio

//Entrada de Dados
escrevaL("CALCULO DE FOLHA DE PAGAMENTO")
escrevaL("--------------------")

escrevaL("Informe o numero de dias trabalhados: ")
leia(dias)

// Cálculo: Dias * (8 horas * R$25.00)
salario <- dias * 200

escrevaL("--------------------")
escrevaL("O funcionario trabalhou ", dias, " dias.")
escrevaL("Salario total a receber: R$ ", salario:5:2)

Fimalgoritmo