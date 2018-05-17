#coding: utf-8
#Crispiniano
#Unidade 4: Grep

palavra = raw_input()
n = int(raw_input())
for i in range(n):
    e = raw_input()
    for i in range(len(e)-2):
        if e[i] == palavra[0] and e[i + 1] == palavra[1] and e[i + 2] == palavra[2]:
			print e
