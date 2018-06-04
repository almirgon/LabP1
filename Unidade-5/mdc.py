#coding: utf-8
#Crispiniano
#Unidade 5: MDC (Euclides)

D = int(raw_input())
d = int(raw_input())

resto = 0
if D > d:
    aux = D
    while aux >= d:
        aux -= d
	resto = aux 
