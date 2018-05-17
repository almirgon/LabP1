#coding: utf-8
#Crispiniano
#Unidade 4: Converte matrícula

matricula = raw_input()
resultado = ''
for i in range(len(matricula)):
	if i == 0:
		resultado += '1'
	else:
		resultado += matricula[i]
	if i == 4:
		resultado += '0'
	else:
		pass
print resultado 
