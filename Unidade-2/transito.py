#coding: utf-8
#Crispiniano
#Unidade 2: Perda de Tempo no Trânsito

minuto1 = float(raw_input())
minuto2 = float(raw_input())
minuto3 = float(raw_input())
minuto4 = float(raw_input())
minuto5 = float(raw_input())

soma = minuto1 + minuto2 + minuto3 + minuto4 + minuto5
media = float(soma)/5
semana = float(soma * 100)/7200
house = soma/50

print 'Você perdeu {:.0f} min na semana (média de {:.1f} min por dia).'.format(soma,media)
print 'Isso significa {:.2f}% da sua semana produtiva.'.format(semana)
print 'Daria para assistir {} episódio(s) de House.'.format(int(house))
