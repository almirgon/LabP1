#coding: utf-8
#Crispiniano
#Unidade 4: Colheita

registros = int(raw_input())
mes1 = mes2 = mes3 = mes4 = mes5 = mes6 = mes7 = mes8 = mes9 = mes10 = mes11 = mes12 = 0

for i in range(registros):
	colheita = raw_input().split(',')
	if colheita[0] == '1':
		mes1 += int(colheita[1])
	elif colheita[0] == '2':
		mes2 += int(colheita[1])
	elif colheita[0] == '3':
		mes3 += int(colheita[1])
	elif colheita[0] == '4':
		mes4 += int(colheita[1])
	elif colheita[0] == '5':
		mes5 += int(colheita[1])
	elif colheita[0] == '6':
		mes6 += int(colheita[1])
	elif colheita[0] == '7':
		mes7 += int(colheita[1])
	elif colheita[0] == '8':
		mes8 += int(colheita[1])
	elif colheita[0] == '9':
		mes9 += int(colheita[1])
	elif colheita[0] == '10':
		mes10 += int(colheita[1])
	elif colheita[0] == '11':
		mes11 += int(colheita[1])
	elif colheita[0] == '12':
		mes12 += int(colheita[1])
		
media = float(mes1+mes2+mes3+mes4+mes5+mes6+mes7+mes8+mes9+mes10+mes11+mes12)/registros

if mes1 >= media:
	print 'O mês 1 teve boa colheita.'
if mes2 >= media:
	print 'O mês 2 teve boa colheita.'
if mes3 >= media:
	print 'O mês 3 teve boa colheita.'
if mes4 >= media:
	print 'O mês 4 teve boa colheita.'
if mes5 >= media:
	print 'O mês 5 teve boa colheita.'
if mes6 >= media:
	print 'O mês 6 teve boa colheita.'
if mes7 >= media:
	print 'O mês 7 teve boa colheita.'
if mes8 >= media:
	print 'O mês 8 teve boa colheita.'
if mes9 >= media:
	print 'O mês 9 teve boa colheita.'
if mes10 >= media:
	print 'O mês 10 teve boa colheita.'
if mes11 >= media:
	print 'O mês 11 teve boa colheita.'
if mes12 >= media:
	print 'O mês 12 teve boa colheita.'
