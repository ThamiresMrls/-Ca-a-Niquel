cont = 0
moedas = 7
bonus = 5
aposta = 1
par = 15
trinca = 50
rodadas = 0


import random
import time
import niqueis


niqueis.apresentacao()

time.sleep(1)
escolhaRegraGeral = str.upper(input("Deseja ver as Regras Gerais? \n(SIM ou NÃO)\n"))
regraGeral = niqueis.validaEscolha(escolhaRegraGeral)
while(regraGeral != True):
    print('ERRO')
    escolhaRegraGeral = str.upper(input("Deseja ver as Regras Gerais? \n(SIM ou NÃO)\n"))
    regraGeral = niqueis.validaEscolha(escolhaRegraGeral)


time.sleep(1)
if(escolhaRegraGeral == "SIM"):
    niqueis.regraGeral()
time.sleep(1)


escolhaRegraAdicional = str.upper(input("Deseja ver as Regras Adicionais? \n(SIM ou NÃO)\n"))
regraAdicional = niqueis.validaEscolha(escolhaRegraAdicional)
while(regraAdicional != True):
    print('ERRO')
    escolhaRegraAdicional = str.upper(input("Deseja ver as Regras Adicionais? \n(SIM ou NÃO)\n"))
    regraAdicional = niqueis.validaEscolha(escolhaRegraAdicional)


time.sleep(1)
if(escolhaRegraAdicional == "SIM"):
    niqueis.regraAdicional()
time.sleep(1)

nome = str.upper(input('Informe seu nome:'))

time.sleep(1)
niqueis.exibirNome(nome)
time.sleep(1)

jogar = str.upper(input("Deseja Jogar?\n(SIM ou NÃO)\n"))
escolhaJogar = niqueis.validaEscolha(jogar)
while(escolhaJogar != True):
    print('ERRO')
    jogar = str.upper(input("Deseja Jogar?\n(SIM ou NÃO)\n"))
    escolhaJogar = niqueis.validaEscolha(jogar)

while(jogar == 'SIM') and (moedas > 0) and (rodadas < 7):

    moedas = moedas - aposta
    
    quantFruta = 0
    quantCoracao = 0
    quantCifrao = 0
    quantEstrela = 0
    quantNumero = 0
    quantPessoa = 0

    for cont in range(3):

        imagem = random.choice(["♥", "ಹ", "✰", "7","$","웃"])
        niqueis.exibicaoSorteio(imagem)
        if(imagem == "♥"):
            quantCoracao = quantCoracao + 1
        elif(imagem == "ಹ"):
            quantFruta = quantFruta + 1
        elif(imagem == "✰"):
            quantEstrela = quantEstrela + 1
        elif(imagem == "7"):
            quantNumero = quantNumero + 1
        elif(imagem == "$"):
            quantCifrao = quantCifrao + 1
        elif(imagem == "웃"):
            quantPessoa = quantPessoa + 1


    moedas = niqueis.calculaNiqueis(quantFruta, quantCoracao, quantNumero, quantPessoa, quantCifrao, quantEstrela, moedas, par, trinca, bonus)
    
    time.sleep(1)
    print('Você Possui', moedas, 'Moedas')

    time.sleep(1)
    jogar = str.upper(input("Deseja Jogar Novamente?\n(SIM ou NÃO)\n"))
    escolhaJogar = niqueis.validaEscolha(jogar)
    while(escolhaJogar != True):
        print('ERRO')
        jogar = str.upper(input("Deseja Jogar Novamente?\n(SIM ou NÃO)\n"))
        escolhaJogar = niqueis.validaEscolha(jogar)
    
if(jogar == "NÃO") or (jogar == "NAO"):
    print('FIM DE JOGO')
    print('Obrigado Pela sua Preferência e Volte Sempre')

if(moedas <= 0):
    print('Suas Moedas não são Suficiente')
    print('FIM DE JOGO')
    print('Obrigado Pela sua Preferência e Volte Sempre')

if(rodadas >= 7):
    print('Suas Rodadas Acabaram...')
    print('FIM DE JOGO')
    print('Obrigado Pela sua Preferência e Volte Sempre')
