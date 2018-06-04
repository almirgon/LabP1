razao = float(raw_input())

criancas = 0
adultos = 0
peso_total = 0.0
while True:
	sequencia = raw_input().split()
	if sequencia[0] == "a":
		adultos += 1
		peso_total += float(sequencia[1])
	if sequencia[0] == "c":
		criancas += 1
		peso_total += float(sequencia[1])
	if criancas == 1 and adultos == 0 and razao >= 1:
		criancas -= 1
		peso_total -= float(sequencia[1])
		break
	if (criancas/adultos) >= razao:
		criancas -= 1
		peso_total -= float(sequencia[1])
		break
	if peso_total > 700:
		criancas -= 1
		peso_total -= float(sequencia[1])
		break

print 'Limite atingido'
print 'Elevador saiu com %i pessoas e %.2f kg.' % (criancas+adultos,peso_total)

# O primeiro if, verifica se é adulto, e se for, soma +1 adulto e dps soma o peso desse adulto

# O segundo if, verifica se é criança, e se for, soma +1 criança e dps soma o peso dessa criança

Obs: O peso é somando em uma variavel geral 'peso_total', não precisa somar em variaveis distintas

# O terceiro if eu explico por ultimo pq ele é um caso particular..

# O quarto if faz a verificação da razao, ele divide a quantidade de crianças pela de adulto, se o resultado dessa divisao
# for maior ou igual a razao, precisamos parar o código, porém, antes de parar, precisamos subtrair a ultima criança e o ultimo peso lido
# pois é dito na especificação: "Nota que essa configuração nao pode incluir a pessoa que fez com que um dos critérios não fosse verdadeiro"

# O quinto if faz a verificação do peso, se ele ultrapassou o limite de 700.00kg (dado na especificação), e caso tenha ultrapassado, ele para a leitura, porém, antes de parar de ler, ele também subtrai a ultima criança e o último peso lido (dado na especificação)

# Esse terceiro if, ele só é pra testar um caso particular, que é quando a razao é 1 e é informada uma criança antes de um adulto, se esse if nao for criado, ele vai dar um problema no segundo caso de teste, veja que no segundo caso é informado:
# 1
# c 150.00
# Limite atingido.
# Elevador saiu com 0 pessoas e 0.00 kg.
..
# Se nao criar esse if, ele vai tentar fazer a divisao la no segundo if: criança/adulto, porém, a quantidade de crianças é 1 e a quantidade de adultos é 0, ou seja: 1/0 e nao se pode dividir 1 por 0 né, por isso precisa criar esse terceiro if, ele é meio que um 'tapa buraco', pois ele só trata esse caso específico mesmo.
