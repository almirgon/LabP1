#coding: utf-8
#Crispiniano
#Unidade 6: Altera Consecutivos (Inverte 2 a 2)

def inverte2a2(seq):
	for i in range(0,(len(seq)-1),2):
		seq[i],seq[i+1] = seq[i+1],seq[i]

seq = [1,2,3,4,5,6]
inverte2a2(seq)
assert seq == [2,1,4,3,6,5]

seq = [1,2,3,4,5]
inverte2a2(seq)
assert seq == [2,1,4,3,5]
