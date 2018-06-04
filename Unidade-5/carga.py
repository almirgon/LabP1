#coding: utf-8
#Crispiniano
#Unidade 5: Carga Trabalho Professor

soma = 0
rejeitadas = 0
while True:
	atividade = int(raw_input())
	if atividade > 10:
		rejeitadas += 1
	else:
		soma += atividade
		if soma > 60:
			soma -= atividade
			rejeitadas += 1
		elif soma == 60:
			break
	
	
print "Rejeitadas = %i" % rejeitadas
print "Fim de semana!"
