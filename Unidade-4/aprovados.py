#coding: utf-8
#Crispiniano
#Unidade 4: Aprovados e Reprovados

n = int(raw_input())

reprovados = 0
aprovados = 0
media_r = 0
media_a = 0

for i in range(n):
	notas = float(raw_input())
	if notas < 7.0:
		reprovados += 1
		media_r += notas
	elif notas >= 7.0:
		aprovados += 1
		media_a += notas 

print 'Reprovados: {}'.format(reprovados)
if reprovados >= 1:
	print 'Média: {:.1f}'.format(media_r/reprovados)
print '\nAprovados: {}'.format(aprovados)

if aprovados >= 1:
	print 'Média: {:.1f}'.format(media_a/aprovados)
