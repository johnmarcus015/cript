# -*- coding: utf-8 -*-

def main():        
    op = 0    
    while(op!=3):
        op = int(input('CRIPTOGRAFIA:\n1 - CRIPTOGRAFAR\n2 - DESCRIPTOGRAFAR\n3 - SAIR\nEscolha um numero:\n'))
        if op == 1:
            print('Mensagem criptografada:\n%s'%criptografar())
        elif op == 2:
            print('Mensagem decriptografada:\n%s'%descriptografar())        
        elif op == 3:
            print()
        else:
            print('numero invalido')

main()
def criptografar():
    msg = input('Mensagem:\n').lower()
    key = 0
    while(key<111111):
        key = int(input('Chave:\n'))
    msgCifrada = ''    
    for letra in msg:
        s = cifras.find(letra) + key
        m = int(s) % len(cifras)
        msgCifrada = msgCifrada + str(cifras[m])
    return msgCifrada 

def descriptografar():
    msg = input('Mensagem:\n').lower()
    key = 0
    while(key<111111):
        key = int(input('Chave:\n'))
    msgCifrada = ''
    for letra in msg:
        s = cifras.find(letra) - key
        m = int(s) % len(cifras)        
        msgCifrada = msgCifrada + str(cifras[m])
    return msgCifrada

cifras = 'abcdefghijklmnopqrstuvwxyz '    
