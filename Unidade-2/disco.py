#coding: utf-8
#Crispiniano
#Unidade 2: Espaço em Disco Simplificado 

usuario1 = raw_input()
espaco1 = int(raw_input())

usuario2 = raw_input()
espaco2 = int(raw_input())

usuario3 = raw_input()
espaco3 = int(raw_input())

espaco1 = (espaco1 / 1024.0) / 1024.0
espaco2 = (espaco2 / 1024.0) / 1024.0
espaco3 = (espaco3 / 1024.0) / 1024.0

total = espaco1 + espaco2 + espaco3
media = total / 3.0

print "SPLab - Espaço utilizado pelos usuários"
print "---------------------------------------------"
print "Nr., Usuário, Espaço Utilizado\n"
print "1, {}, {:.2f} MB".format(usuario1, espaco1)
print "2, {}, {:.2f} MB".format(usuario2, espaco2)
print "3, {}, {:.2f} MB".format(usuario3, espaco3)
print "\nEspaço total ocupado: {:.2f} MB".format(total)
print "Espaço médio ocupado: {:.2f} MB".format(media)
