#coding: utf-8
#@Crispiniano 
#Unidade 1: Campos de Futebol

area_1 = float(raw_input())
area_2 = float(raw_input())
area_3 = float(raw_input())

campo_1 = area_1/4000
campo_2 = area_2/4000
campo_3 = area_3/4000

media = (campo_1+campo_2+campo_3)/3

print '{:.2f}'.format(campo_1)
print '{:.2f}'.format(campo_2)
print '{:.2f}'.format(campo_3)
print '{:.2f}'.format(media)
