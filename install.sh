#!/bin/bash
#
# versao 1.0
#
# NOME
#   install.sh
#
# DESCRICAO
#   Script para instalação do Sesamo no Linux.
#
# NOTA
#   Executar como root.
########################################################################################

echo "Verificando se é o root executando..."
[ "$(id -u)" != "0" ] && { echo "Executar esse script novamente como root"; exit 1; }

echo "Copiando o arquivo de configuração..."
mkdir -p $HOME/.config/sesamo
cp -pv ./config.ini.example $HOME/.config/sesamo/config.ini

echo "Criando o executável do Sesamo..."
cp -pv ./sesamo.py /usr/local/bin/sesamo
chmod +x /usr/local/bin/sesamo

exit 0
