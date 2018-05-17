#coding: utf-8
#Crispiniano
#Unidade 4: Conta Inversa

palavra = raw_input()

inversa = ''
for i in range(len(palavra)-1,-1,-1):
	inversa += palavra[i]

cont = 0
for e in range(len(palavra)):
	if palavra[e] == inversa[e]:
		cont += 1

print 'A palavra {} contém {} caractere(s) coincidente(s) com a sua inversa.'.format(palavra,cont)
	
	
