#coding: utf-8
#Crispiniano
#Unidade 2: Salário Bruto e Líquido

nome = raw_input()
horas = float(raw_input())
minimo = float(raw_input())
extra = float(raw_input())

hora_extra = horas * extra
bruto = 4 * minimo + hora_extra
inss = bruto * 0.12
renda = bruto * 0.20 
liquido = bruto - (inss + renda)

print 'O Salário Bruto de {} é de R$ {:.2f}'.format(nome,bruto)
print 'O Salário Líquido de {} é de R$ {:.2f}'.format(nome,liquido)
