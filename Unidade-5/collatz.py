#coding: utf-8
#Crispiniano
#Unidade 5: collatz

def collatz(num):
    while num != 1:
        print(num)
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = int(3 * num + 1)
    else:
        print(num)

def main():
    num = int(raw_input())
    collatz(num)

main()
