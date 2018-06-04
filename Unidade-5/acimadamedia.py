#coding: utf-8
#Crispiniano
#Unidade 5: Acima da média (Criminalidade)

media_mensal = float(raw_input())

lista = []
soma = 0.0
while True:
	sequencia = raw_input().split()
	if sequencia[0] == 'fim':
		break
	for num in sequencia:
		soma += int(num)
	media = soma / len(sequencia)
	if media < (media_mensal / 2):
		break
	if media > media_mensal:
		string = ''
		for i in range(len(sequencia)):
			if i == len(sequencia)-1:
				string += str(sequencia[i])
			else:
				string += str(sequencia[i]) + ' '
		lista.append(string)
	soma = 0.0

for k in lista:
	print k
