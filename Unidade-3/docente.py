#coding: utf-8
#Crispiniano
#Unidade 3: Avaliação Docente

semestres = int(raw_input())
ensino = float(raw_input())
intelectual = float(raw_input())
orientacao = float(raw_input())
administrativa = float(raw_input())

media = (ensino + intelectual + orientacao + administrativa)/ 4

if semestres < 4:
	print 'Promoção indeferida. Número de semestres insuficiente.'
elif ensino < 320 or intelectual < 100 or orientacao < 20:
	print 'Promoção indeferida. Pontuação mínima não alcançada.'
elif media < 140:
	print 'Promoção indeferida. Média insuficiente.'
else:
	print 'Promoção deferida. Parabéns!'
