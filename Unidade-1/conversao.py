#coding: utf-8
#@Crispiniano 
#Unidade 1: Conversão de Medidas

milhas = float(raw_input())
libras = float(raw_input())
galoes = float(raw_input())
km = milhas * 1.60934
kg = libras * 0.453592
l = galoes * 3.78541

print '{} {} {}'.format(km,kg,l)
