#coding: utf-8
#Crispiniano
#Unidade 5: Embarque organizado

sequencia = raw_input().split()

def paridade(numero):
    if int(numero) % 2 == 0:
        return 'par'
    else:
        return 'impar'
i = 0
condicao = False
while i < len(sequencia):
    if paridade(sequencia[i]) == 'par':
        condicao = True
    if condicao == True and paridade(sequencia[i]) == 'impar':
        print 'erro'
        break
    i += 1
else:
	print 'ok'
