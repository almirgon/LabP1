#coding: utf-8
#Crispiniano
#Unidade 5: MDC (Euclides)

D = int(raw_input())
d = int(raw_input())

maior = 0
menor = 0
resto = 0
if (D == d and d != 0) or d == 0:
	print D
elif D == 0:
	print d
	
elif D > d:
    resto = D
    maior = D
    menor = d
    while resto >= d:
        resto -= d
    maior = menor
    menor = resto
    while menor< maior:
		maior -= menor

elif d > D:
    resto = d
    maior = d
    menor = D
    while resto >= D:
        resto -= D
    maior = menor
    menor = resto
    while menor < maior:
		maior -= menor
if D != d and D != 0 and d != 0:
	print maior
