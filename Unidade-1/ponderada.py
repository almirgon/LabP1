#coding: utf-8
#@Crispiniano 
#Unidade 1: Média Mágica 

nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
peso1 = float(raw_input())
peso2 = float(raw_input())

peso3 = 100 - (peso1+peso2)
media = (nota1*(peso1/100) + nota2*(peso2/100) + nota3*(peso3/100))

print "Média Final: {:.1f}".format(media)
