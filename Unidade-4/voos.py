#coding: utf-8
#Crispiniano
#Unidade 4: Autorização voos

tempo = float(raw_input())
n = int(raw_input())
cont = 0

for i in range(n):
	voos = float(raw_input()) 
	if voos <= tempo and tempo >= 0:
		tempo -= voos
		cont += 1

print '{} voo(s) autorizados.'.format(cont) 
