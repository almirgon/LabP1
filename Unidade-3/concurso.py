#coding: utf-8
#Crispiniano
#Unidade 3: Concurso

nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
idade1 = int(raw_input())
nota4 = float(raw_input())
nota5 = float(raw_input())
nota6 = float(raw_input())
idade2 = int(raw_input())

m1 = (nota1 * 0.30) + (nota2 * 0.40) + (nota3 * 0.30)
m2 = (nota4 * 0.30) + (nota5 * 0.40) + (nota6 * 0.30)

if m1 > m2:
	print 'O primeiro candidato foi aprovado com média {:.1f}.'.format(m1)
elif m1 < m2:
	print 'O segundo candidato foi aprovado com média {:.1f}.'.format(m2)
elif m1 == m2:
	if idade1 > idade2:
		print 'O primeiro candidato foi aprovado com média {:.1f}.'.format(m1)
	elif idade2 > idade1:
		print 'O segundo candidato foi aprovado com média {:.1f}.'.format(m2)
	else:
		print 'Empate.'
