#coding: utf-8
#Crispiniano
#Unidade 4: Dígitos Pares Coincidentes

n1 = raw_input()
n2 = raw_input()

print 'Dígitos coincidentes'
soma = 0
for i in range(len(n1)):
	if int(n1[i]) % 2 == 0:
		if int(n2[i]) % 2 == 0:
			if int(n1[i]) == int(n2[i]):
				print '{} na posição {}'.format(n1[i],i+1)
				soma += int(n1[i]) 

print 'Soma de dígitos coincidentes: {}'.format(soma)

			
				
			
