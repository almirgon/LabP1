#coding: utf-8
#Crispiniano
#Unidade 3: Cálculo do IMC

peso = float(raw_input())
altura = float(raw_input())

imc = peso/(altura**2)

if imc < 16:
	print 'IMC: {:.1f} - Magreza grave'.format(imc)
elif 16 <= imc and imc < 17:
	print 'IMC: {:.1f} - Magreza moderada'.format(imc)
elif 17 <= imc and imc < 18.5:
	print 'IMC: {:.1f} - Magreza leve'.format(imc)
elif 18.5 <= imc and imc < 25:
	print 'IMC: {:.1f} - Saudável'.format(imc)
elif 25 <= imc and imc < 30:
	print 'IMC: {:.1f} - Sobrepeso'.format(imc)
elif 30 <= imc and imc < 35:
	print 'IMC: {:.1f} - Obesidade Grau I'.format(imc)
elif 35 <= imc and imc < 40:
	print 'IMC: {:.1f} - Obesidade Grau II (severa)'.format(imc)
elif imc >= 40:
	print 'IMC: {:.1f} - Obesidade Grau III (mórbida)'.format(imc)
