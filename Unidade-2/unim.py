#coding: utf-8
#Crispiniano
#Unidade 2: Unidades e Medidas

metros = float(raw_input())

jarda = (metros * 1)/0.9144
pes = (metros * 3)/0.9144
polegadas = (metros * 36)/ 0.9144

print 'Jardas: {:.3f} yd'.format(jarda)
print 'Pés: {:.3f} ft'.format(pes)
print 'Polegadas: {:.3f} in'.format(polegadas)

