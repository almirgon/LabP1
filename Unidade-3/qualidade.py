#coding: utf-8
#Crispiniano
#Unidade 3: Controle de Qualidade

antes = float(raw_input())
depois = float(raw_input())

diferenca = depois - antes 

porcentagem = abs(diferenca * 100)/antes

if 5 <= porcentagem < 10:
	print '{:.1f}% do peso do produto é de água congelada.'.format(porcentagem)
	print 'Produto em conformidade.'
elif porcentagem < 5:
	print '{:.1f}% do peso do produto é de água congelada.'.format(porcentagem)
	print 'Produto qualis A.'
else:
	print '{:.1f}% do peso do produto é de água congelada.'.format(porcentagem)
	print 'Produto não conforme.'
