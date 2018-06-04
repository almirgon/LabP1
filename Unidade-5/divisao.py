#coding: utf-8
#Crispiniano
#Unidade 5: Divisão por Subtração

D = int(raw_input())
d = int(raw_input())

cont = 0
if D > d:
    aux = D
    while aux >= d:
        print "%i: %i - %i = %i" % (cont+1, aux, d, aux - d)
        cont += 1
        aux -= d
    print '---'
    print 'quociente: %i' % cont
    print 'resto: %i' % aux
    print '{} = {} x {} + {}'.format(D,cont,d,aux)

elif D == d:

    print "%i - %i = 0" % (D, d)
    print '---'
    print 'quociente: 1'
    print 'resto: 0'
    print '{} = {} x {} + {}'.format(D,cont,d,aux)

else:
        print '---'
        print 'quociente: 0'
        print 'resto: %i' % D
        print '{} = {} x {} + {}'.format(D,cont,d,aux)
