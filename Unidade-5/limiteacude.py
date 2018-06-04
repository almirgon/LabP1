#coding: utf-8
#Crispiniano
#Unidade 5: Limite açude

limite = float(raw_input())
nivel = float(raw_input())

while True:
	if nivel >= limite:
		print 'Açude passou a liberar água.'
		print 'Nível: {:.2f}'.format(nivel)
		break
	dados = raw_input().split()
	if dados[0] == 'chuva' or dados[0] == 'afluente':
		nivel += float(dados[1])
	if dados[0] == 'demanda':
		if nivel - float(dados[1]) >= 0:
			nivel -= float(dados[1])
