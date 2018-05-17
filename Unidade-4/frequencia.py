#coding: utf-8
#Crispiniano
#Unidade 4: Frequência elemento

n = raw_input()
seq = raw_input().split()

cont = 0

for i in range(len(seq)):
	if seq[i] == n:
		cont += 1

print cont 
