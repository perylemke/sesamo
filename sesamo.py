#!/usr/bin/env python3

import os, sys, time, configparser, getpass

# ConfigParser start
home = os.environ['HOME']
config = configparser.ConfigParser()
config.read('%s/.config/sesamo/config.ini' % home)

# Catch sections
servers = config.sections()

def verify_user():
        user = getpass.getuser()

        if user == 'root':
            print("Você está acessando com o usuário %s. Favor acessar com seu usuário." % user)
            sys.exit(3)

def connect_server(opt):
    choice = int(opt) - 1
    ssh = config[servers[choice]]['ssh']
    os.system('ssh %s' % ssh)

def front():
    print("""
*** Bem vindo ao Sésamo ***

Escolha o server que você deseja acessar:
    """)

    n = 1

    while n <= len(servers):
        select_host = servers[n-1]
        print("%s - %s" %(n, select_host))

        n = n + 1

    print("0 - Sair")
    print("")

def run():
    should_exit = False

    while not should_exit:
        verify_user()
        front()
        host = input("Opção desejada: ")
        if host.isdigit():
            if host != '0':
                try:
                    should_exit = True
                    connect_server(host)
                except(IndexError):
                    should_exit = False
                    os.system('clear')
                    print("Opção inexistente. Tente novamente.")
            else:
                print("Bye!")
                sys.exit(0)
        else:
            os.system('clear')
            print ("Somente números são permitidos. Tente novamente.")

def main():
    try:
        run()
    except(Exception):
        print('')
        print('Bye!')
        sys.exit(0)
    except(KeyboardInterrupt):
        print('')
        print('Você executou um comando inválido. Sésamo fechando!')
        time.sleep(1)
        sys.exit(1)

if __name__ == '__main__':
    main()
