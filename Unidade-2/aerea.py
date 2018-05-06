#coding: utf-8
#Crispiniano
#Unidade 2: Passagem Aérea

taxa_aeroporto = 51.0
desconto_avista = 0.75
desconto_parcelado6x = 0.95

milhas = float(raw_input())
aliquota = float(raw_input())

passagem = milhas * aliquota + taxa_aeroporto
passagem_avista = passagem * desconto_avista

passagem_parcelada6x = passagem * desconto_parcelado6x
parcela_6x = passagem_parcelada6x / 6
parcela_10x = passagem / 10

print "Valor da passagem: R$ %.2f\n" % passagem
print "Pagamento:\n1. À vista. R$ %.2f" % passagem_avista
print "2. Em 6 parcelas. Total: R$ %.2f" % passagem_parcelada6x
print "   6 x R$ %.2f" % parcela_6x
print "3. Em 10 parcelas. Total: R$ %.2f" % passagem
print "   10 x R$ %.2f" % parcela_10x
