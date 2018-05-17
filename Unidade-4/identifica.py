#coding: utf-8
#Crispiniano
#Unidade 4: Identifica Iguais

entrada1 = raw_input().split()
entrada2 = raw_input().split()

for i in range(len(entrada1)):
		if entrada1[i] == entrada2[i]:
			print '{}: {}'.format(i+1,entrada1[i])
