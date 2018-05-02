#coding: utf-8
#@Crispiniano 
#Unidade 1: MRU

s_inicial = float(raw_input())
velocidade = float(raw_input())
tempo = float(raw_input())

s_final = s_inicial + (velocidade*tempo)

print 'Posição final do móvel'
print 'S({}) = {:.1f} m'.format(tempo,s_final)
