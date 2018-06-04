#coding: utf-8
#Crispiniano
#Unidade 5: Consulta Exercicios

exercicios = raw_input().split()
alunos = raw_input().split()

while True:
	cont = 0
	saida = '-'
	n, k = raw_input().split()
	if n == '0' and k == '0':
		break
	for i in range(len(exercicios)):
		if int(exercicios[i]) <= int(k):
			cont +=1
			if cont == int(n):
				saida = '{} {}'.format(alunos[i], exercicios[i])
	print saida
	
		
