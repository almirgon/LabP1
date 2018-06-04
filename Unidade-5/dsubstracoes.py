#coding: utf-8
#Crispiniano
#Unidade 5: Divisão por subtrações

entrada = raw_input().split()
D = int(entrada[0])
d = int(entrada[1])

cont = 0
if D > d:
    aux = D
    while aux >= d:
        print "%i - %i = %i" % (aux, d, aux - d)
        cont += 1
        aux -= d
    print "%i - %i < 0" % (aux, d)
    print '==='
    print 'quociente = %i' % cont
    print 'resto = %i' % aux
elif D == d:

    print "%i - %i = 0" % (D, d)
    print "0 - %i < 0" % (d)
    print '==='
    print 'quociente = 1'
    print 'resto = 0'

else:
        print "%i - %i < 0" % (D,d)
        print '==='
        print 'quociente = 0'
        print 'resto = %i' % D
