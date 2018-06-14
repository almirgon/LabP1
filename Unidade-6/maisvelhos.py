#coding: utf-8
#Crispiniano
#Unidade 6: Mais Velhos Primeiro

def idosos_inicio(fila):
	indice = 0
	for i in range(len(fila)):
		if int(fila[i]) >= 60:
			fila[i], fila[indice] = fila[indice], fila[i]
			indice += 1

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila)
assert fila == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]
