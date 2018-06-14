#coding: utf-8
#Crispiniano
#Unidade 6: Quanto Tempo


def quanto_tempo(horario1,horario2):
	h1 = int(horario1[0] + horario1[1])
	m1 = int(horario1[3] + horario1[4])
	minutos_totais_1 = h1 * 60 + m1
	
	h2 = int(horario2[0] + horario2[1])
	m2 = int(horario2[3] + horario2[4])
	minutos_totais_2 = h2 * 60 + m2

	diferenca = minutos_totais_2 - minutos_totais_1
	h3 = diferenca // 60
	m3 = diferenca % 60
	
	saida = '%i hora(s) e %i minuto(s)' % (h3, m3)
	return saida
assert quanto_tempo("07:15", "09:18") == "2 hora(s) e 3 minuto(s)"
