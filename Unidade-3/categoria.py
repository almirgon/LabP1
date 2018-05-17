#coding: utf-8
#Crispiniano
#Unidade 3: Categorias

nome = raw_input()
idade = int(raw_input())

if idade < 5:
	print '{}, {} anos, Não pode competir.'.format(nome,idade)
if 5 <= idade <= 7:
	print '{}, {} anos, Infantil A.'.format(nome,idade)
if 8 <= idade <= 10:
	print '{}, {} anos, Infantil B.'.format(nome,idade)
if 11 <= idade <= 13:
	print '{}, {} anos, Juvenil A.'.format(nome,idade)
if 14 <= idade <= 17:
	print '{}, {} anos, Juvenil B.'.format(nome,idade)
if idade > 17:
	print '{}, {} anos, Senior.'.format(nome,idade)


