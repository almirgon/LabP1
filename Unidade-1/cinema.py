#coding: utf-8
#@Crispiniano 
#Unidade 1: Calcula despesas do cinema

dia =  raw_input("Dia da semana? ")
orcamento =  float(raw_input("Orcamento? R$ "))
adultos =  int(raw_input("Numero de adultos? "))
criancas =  int(raw_input("Numero de criancas? "))
pizza = float(raw_input("Preco da pizza? R$ "))
refrigerante = float(raw_input("Preco do refrigerante? R$ "))
estacionamento = float(raw_input("Preco do estacionamento? R$ "))
cinema = float(raw_input("Preco do ingresso do cinema? R$ "))

gastos_alimentacao = pizza + refrigerante
taxa = (adultos + criancas) * 2.00
gastos_cinema = ((cinema * adultos) + (cinema/2.00) * criancas) + taxa
gastos_total = gastos_cinema + gastos_alimentacao + estacionamento

print "========== Despesas de " + dia + " =========="
print "Despesas com alimentacao: R$ " + str(gastos_alimentacao)
print "Despesas com cinema: R$ " + str(gastos_cinema)
print "Despesas por pessoa: R$ " + str(gastos_total / (criancas + adultos))
print "Saldo disponivel: " + str(orcamento - gastos_total)
