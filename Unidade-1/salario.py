#coding: utf-8
#@Crispiniano 
#Unidade 1: Salário

salario_bruto = float(raw_input())
horas_de_trabalho = int(raw_input())
ganhos_por_hora = salario_bruto / horas_de_trabalho
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (ir+inss+sindicato)
hora_liquida = salario_liquido/horas_de_trabalho

print "Salário Bruto = " + str(salario_bruto)
print "Hora Bruta = " + str(ganhos_por_hora)
print "Desconto IR = " + str(ir)
print "Desconto INSS = " + str(inss)
print "Desconto Sindicato = " + str(sindicato)
print "Salário Líquido = " + str(salario_liquido)
print "Hora Líquida = " + str(hora_liquida)
