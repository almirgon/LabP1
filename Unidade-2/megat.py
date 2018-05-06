#coding: utf-8
#Crispiniano
#Unidade 2: Mega Tripla

n1 = int(raw_input())
n2 = int(raw_input())
n3 = int(raw_input())

v1 = n1 % 11
v2 = n2 % 11 
v3 = n3 % 11 

print '{:02.0f}-{:02.0f}-{:02.0f}'.format(v1,v2,v3)

