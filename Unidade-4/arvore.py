#coding: utf-8
#Crispiniano
#Unidade 4: Árvore de Natal

altura = int(raw_input())

espacos = altura - 1
tronco = " " * espacos + "o"

for camada in range(1, altura * 2, 2):
    margem = " " * espacos
    folhas = "o" * camada

    print margem + folhas
    espacos -= 1

print tronco
