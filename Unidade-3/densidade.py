#coding: utf-8
#Crispiniano
#Unidade 3: Densidade

massa1 = float(raw_input())
volume1 = float(raw_input())
massa2 = float(raw_input())
volume2 = float(raw_input())
massa3 = float(raw_input())
volume3 = float(raw_input())

densidade1 = massa1/volume1
densidade2 = massa2/volume2
densidade3 = massa3/volume3

if densidade3 > densidade1 < densidade2:
	print 'O líquido 1, com densidade {:.2f}, irá ocupar a parte de cima do recipiente.'.format(densidade1)
elif densidade3 > densidade2 < densidade1 :
	print 'O líquido 2, com densidade {:.2f}, irá ocupar a parte de cima do recipiente.'.format(densidade2)
elif densidade1 > densidade3 < densidade2:
	print 'O líquido 3, com densidade {:.2f}, irá ocupar a parte de cima do recipiente.'.format(densidade3)
