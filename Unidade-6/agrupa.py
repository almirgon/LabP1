#coding: utf-8
#Crispiniano
#Unidade 6: Agrupa Próximos

def agrupa_proximos(lista, valor, criterio):
	x = valor - criterio + 1
	y = valor + criterio - 1
	
	nova_lista = []
	for num in lista:
		if num >= x and num <= y:
			nova_lista.append(num)
	return nova_lista

l = [1,2,3,4,8,22,3,5]
assert agrupa_proximos(l,20,3) == [22]
