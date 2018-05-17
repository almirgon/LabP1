#coding: utf-8
#Crispiniano
#Unidade 4: Campanha

vitorias = 0
derrotas = 0
saldo_pro = 0
saldo_contra = 0
pontos_em_casa = 0
pontos_fora = 0 
empates = 0

for i in range(10):
	r = raw_input() 
	if r[0] > r[2] and r[5] == 'c':
		vitorias = vitorias + 1
		saldo_pro = saldo_pro + int(r[0])
		saldo_contra = saldo_contra + int(r[2]) 
		pontos_em_casa = pontos_em_casa + 3
		
	if r[0] < r[2] and r[5] == 'f':
		vitorias = vitorias +1
		saldo_pro = saldo_pro + int(r[2])
		saldo_contra = saldo_contra + int(r[0])
		pontos_fora = pontos_fora + 3
		
	if r[0] > r[2] and r[5] == 'f':
		derrotas = derrotas + 1
		saldo_pro = saldo_pro + int(r[2])
		saldo_contra = saldo_contra + int(r[0])
		
	if r[0] < r[2] and r[5] == 'c':
		derrotas = derrotas + 1
		saldo_pro = saldo_pro + int(r[0])
		saldo_contra = saldo_contra + int(r[2])
		
	if r[0] == r[2] and r[5] == 'c':
		empates = empates + 1
		pontos_em_casa = pontos_em_casa + 1
		saldo_pro = saldo_pro + 1
		saldo_contra = saldo_contra + 1
		
	if r[0] == r[2] and r[5] == 'f':
		empates = empates + 1
		pontos_fora = pontos_fora + 1
		saldo_pro = saldo_pro + 1
		saldo_contra = saldo_contra + 1		
		
saldo_de_gol = int(saldo_pro) - int(saldo_contra)
pontos = int(pontos_em_casa) + int(pontos_fora)
print '%sv, %se, %sd' % (vitorias, empates, derrotas)
print 'pontos: %i' % pontos
print 'saldo: %i (%i pro, %i contra)' % (saldo_de_gol, saldo_pro, saldo_contra)
print 'pontos em casa: %s' % pontos_em_casa
print 'pontos fora: %s'	% pontos_fora
