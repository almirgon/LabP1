#coding: utf-8
#Crispiniano
#Unidade 3: Verifica Login

email = raw_input()
senha = raw_input()

if email == 'admin@tst.ufcg.edu.br' and senha == 'TstAdminProg1':
	print 'Login efetuado com sucesso!'
if email == 'admin@tst.ufcg.edu.br' and senha != 'TstAdminProg1':
	print 'Senha inválida. Tente novamente.'
if email != 'admin@tst.ufcg.edu.br' and senha == 'TstAdminProg1':
	print 'Email inválido.'
if email != 'admin@tst.ufcg.edu.br' and senha != 'TstAdminProg1':
	print 'Login inválido.'
