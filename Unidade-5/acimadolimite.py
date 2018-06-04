#coding: utf-8
#Crispiniano
#Unidade 5: Acima do Limite

limite = int(raw_input())
lista = []
sequencias = []
while True:
	seq = raw_input().split()
	if seq[0] == '-':
		break
	soma = 0
	for i in seq:
		soma += int(i)
	if soma > limite:
		lista.append(soma)
		sequencias.append(seq)
	if soma > 5 * limite:
		break 

string = ''
for e in range(len(sequencias)):
	for i in range(len(sequencias[e])):
		string += sequencias[e][i] + ' + '
		print string  
