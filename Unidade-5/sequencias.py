#coding: utf-8
#Crispiniano
#Unidade 5: Imprime Sequencias

def metade_maior(alvo,lista):
    cont = 0
    for e in lista:
        if int(e) > alvo:
            cont += 1
    if cont > len(lista)/2:
        return True
    return False

alvo = int(raw_input())
cont2 = 0
while True:
    entrada = raw_input()
    cont2 += 1
    if entrada == 'fim':
        break
    if metade_maior(alvo, entrada.split()):
        print 'sequencia %i: %s' % (cont2,entrada)
