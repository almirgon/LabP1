#coding: utf-8
#Crispiniano
#Unidade 4: Identifica Iguais

entrada1 = raw_input().split()
entrada2 = raw_input().split()

if len(entrada1) > len(entrada2):
	entrada1,entrada2 = entrada2,entrada1
for i in range(len(entrada1)):
		if int(entrada1[i]) == int(entrada2[i]):
			print '{}: {}'.format(i+1,entrada1[i])
