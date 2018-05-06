#coding: utf-8
#Crispiniano
#Unidade 2: Vendas

total = int(raw_input())
teresa = int(raw_input())
carla = int(raw_input())

joaquim = total - (carla + teresa)

p1 = float(teresa * 100)/total
p2 = float(joaquim * 100)/total
p3 = float(carla * 100)/total

print 'Teresa vendeu {} (de {}) brinquedos. ({:.2f}%)'.format(teresa,total,p1)
print 'Joaquim vendeu {} (de {}) brinquedos. ({:.2f}%)'.format(joaquim,total,p2)
print 'Carla vendeu {} (de {}) brinquedos. ({:.2f}%)'.format(carla,total,p3)
