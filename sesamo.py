#!/usr/bin/env python3

import os
import sys

# Variaveis
version = '0.0.1'

# Funcoes

def bro():
    os.system('ssh pery@bro.ahgora.com.br')

def bro2():
    os.system('ssh pery@bro2.ahgora.com.br')

def bro3():
    os.system('ssh pery@bro3.ahgora.com.br')

def bro4():
    os.system('ssh pery@bro4.ahgora.com.br')

def bro5():
    os.system('ssh pery@bro5.ahgora.com.br')

def main():
    print('########################################')
    print('#         Sesamo Version: %s        #' % version)
    print('########################################')
    print('#         Servers Disponíveis          #')
    print('########################################')
    print('#            1 - Bro                   #')
    print('#            2 - Bro2                  #')
    print('#            3 - Bro3                  #')
    print('#            4 - Bro4                  #')
    print('#            5 - Bro5                  #')
    print('#            0 - Sair                  #')
    print('########################################')
    print('#        Mantenedor: Peronium          #')
    print('########################################')
    opt = input("Opção desejada: ")

    if opt == '1':
        bro()
    elif opt == '2':
        bro2()
    elif opt == '3':
        bro3()
    elif opt == '4':
        bro4()
    elif opt == '5':
        bro5()
    elif opt == '0':
        print('Bye!')
        sys.exit(0)
    else:
        print("Opção inválida. Tente novamente!")
        main()

if __name__ == '__main__':
    try:
        main()
    except(Exception):
        print('')
        print('Bye!')
        sys.exit(0)
    except(KeyboardInterrupt):
        print('')
        print('Bye!')
        sys.exit(0)
