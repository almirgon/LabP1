#coding: utf-8
#@Crispiniano 
#Unidade 1: Orçamento Construção

unidade = float(raw_input('Digite o preço da unidade do tijolo (Em reais): '))
altura_t = float(raw_input('Digite a altura do tijolo (Em metros): '))
comp_t = float(raw_input('Digite o comprimento do tijolo (Em metros): '))
altura_p = float(raw_input('Digite a altura das paredes (Em metros): '))
comp_p = float(raw_input('Digite o comprimento das paredes (Em metros): '))

tijolo_1 = altura_p/altura_t
tijolo_2 = comp_p/comp_t

total = tijolo_1*tijolo_2
preco = total * unidade
print 'O número total de tijolos é {} e o orçamento final é de R$ {}'.format(total,preco)
