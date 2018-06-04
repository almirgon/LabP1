#coding: utf-8
#Crispiniano
#Unidade 5: Monitor temperatura

cont = 0
soma = 0
while True:
	temp = float(raw_input())
	if temp < 10.0 or temp > 30.0:
		errada = temp
		print 'Temperatura inadequeda! {:.2f}.'.format(errada)
		break
	cont += 1
	soma += temp
		
print '{} medições lidas dentro do padrão.'.format(cont)
print 'Média = {:.2f}.'.format((soma)/cont)
