#!/usr/bin/env python3

import os
import sys
import time
import configparser

# ConfigParser configurate
config = configparser.ConfigParser()
config.read('/etc/sesamo.ini')

# Variaveis
version = config.get('SESAMO', 'version')
username = config.get('AHGORA', 'user')
hostname = config.get('AHGORA', 'host')

# Funcoes

def bro():
    os.system("ssh %s@bro.%s" % (username, hostname))

def bro2():
    os.system('ssh %s@bro2.%s' % (username, hostname))

def bro3():
    os.system('ssh %s@bro3.%s' % (username, hostname))

def bro4():
    os.system('ssh %s@bro4.%s' % (username, hostname))

def bro5():
    os.system('ssh %s@bro5.%s' % (username, hostname))

# Funcao Principal
def main():
    print('########################################')
    print('#         Sésamo Version: %s        #' % version)
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
        os.system('clear')
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
        print('Você executou um comando inválido. Sésamo fechando!')
        time.sleep(1)
        sys.exit(1)
