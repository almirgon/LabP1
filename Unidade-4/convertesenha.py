#coding: utf-8
#Crispiniano
#Unidade 4: Converte Senha

senha = raw_input()
primeira = senha[0]
nova_senha = ''
cont = 0
for i in range(1,len(senha)):
	if senha[i] == 'a' or senha[i] == 'A':
		nova_senha += '4'
		cont += 1
	elif senha[i] == 'e' or senha[i] == 'E':
		nova_senha += '3'
		cont += 1
	elif senha[i] == 'i' or senha[i] == 'I':
		nova_senha += '1'
		cont += 1
	elif senha[i] == 'o' or senha[i] == 'O':
		nova_senha += '0'
		cont += 1
	else:
		nova_senha += senha[i]

print '{} ({} troca(s))'.format(primeira+nova_senha,cont)
