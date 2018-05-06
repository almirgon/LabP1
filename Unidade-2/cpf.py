#coding: utf-8
#Crispiniano
#Unidade 2: Novo cpf 

parte1 = raw_input()
parte2 = raw_input()
parte3 = raw_input()

soma = 0
for i in range(len(parte3)):
	soma += int(parte3[i])

print '{}.{}.{}-{:02.0f}'.format(parte1,parte2,parte3,soma)
