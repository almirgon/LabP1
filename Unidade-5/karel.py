#coding: utf-8
#Crispiniano
#Unidade 5: Karel o Robô

p = [0,0]
while True:
    direcao = raw_input().split()

    if direcao[0] == 'D':
        p[0] += int(direcao[1])
    elif direcao[0] == 'E':
        p[0] -= int(direcao[1])
    elif direcao[0] == 'C':
        p[1] += int(direcao[1])
    elif direcao[0] == 'B':
        p[1] -= int(direcao[1])

    if direcao[1] == '0':
        print 'Fim de jogo'
        break
    if abs(p[0]) == abs(p[1]) / 2 and p[0] != 0:
        print 'Parabéns, conquista do portal (%i, %i)' % (p[0],p[1])
        break
