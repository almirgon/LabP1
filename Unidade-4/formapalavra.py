#coding: utf-8
#Crispiniano
#Unidade 4: Forma Palavra (qualitativa)

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
'o','p','q','r','s','t','u','v','w','x','y','z']

palavra1 = raw_input()
palavra2 = raw_input()
palavra3 = raw_input()

novapalavra = ''
auxiliar = -1
listaChar =[]

for i in range(len(palavra1)):
    for l in range(len(alfabeto)):
        if palavra1[i] == alfabeto[l]:
            if auxiliar < l:
                auxiliar = l
                
        if palavra2[i] == alfabeto[l]:
            if auxiliar < l:
                auxiliar = l
                
        if palavra3[i] == alfabeto[l]:
            if auxiliar < l:
                auxiliar = l
        
    listaChar.append(auxiliar)
    auxiliar = 0
        
for indice in listaChar:
    novapalavra += alfabeto[indice]
    
print novapalavra
