from interface.modulo import *
from time import sleep
from arquivo import *
import os

arq1 = 'SI.txt'
arq2 = 'nomes.txt'
arq3 = 'numPares.txt'
arq4 = 'notas.txt'
arq5 = 'notaMaior.txt'

if not arquivoExiste(arq1):
    criarArquivo(arq1)
if not arquivoExiste(arq2):
    criarArquivo(arq2)
if not arquivoExiste(arq3):
    criarArquivo(arq3)
if not arquivoExiste(arq4):
    criarArquivo(arq4)
if not arquivoExiste(arq5):
    criarArquivo(arq5)


while True:
    resposta = menu(['Arquivo SI.txt', 'Registrar Nomes', 'Numeros Pares', 'Notas', 'Sair do programa'])
    if resposta == 1:
        # Escreva um programa que crie e abra um arquivo
        # chamado SI.txt, coloque algumas informações no
        # mesmo e no final feche-o.
        lerArquivoSI(arq1)
        sleep(5)

    elif resposta == 2:
        # Faça um programa que dê autonomia ao usuário para
        # digitar quantos nomes ele desejar, grave os nomes
        # em um arquivo e, depois, mostre os dados gravados.
        while True:
            r = menuNomes(['Cadastrar nome','Mostrar nomes cadastrados', 'Sair'])
            if r == 1:
                nome = str(input('Nome: '))
                cadastrarNomes(arq2, nome)

            elif r == 2:
                lerArquivo(arq2)

            elif r == 3:
                print('Saindo...')
                break

            else:
                print('\033[31mDigite uma opção válida\033[m')

            sleep(5)


    elif resposta == 3:
        # Faça um programa que grave em um arquivo os 20
        # primeiros números pares, e depois, mostre os dados
        # gravados.
        while True:
            o = menuPares(['Gerar números pares', 'Mostrar números pares', 'Sair'])
            if o == 1:
                for n in range(0, 21, 2):
                    par = int('{} '.format(n))
                    cadastrarPares(arq3, par)

            elif o == 2:
                lerArquivoPares(arq3)

            elif o == 3:
                print('Saindo...')
                break

            else:
                print('\033[31mDigite uma opção válida\033[m')

            sleep(5)
            os.system("cls")

    elif resposta == 4:
        #Escreva um algoritmo que leia a nota de 10 alunos e
        #armazene-as num arquivo. Em seguida, mostre
        #apenas as notas acima de 7,0.
        while True:
            r = menuNota(['Cadastrar nota', 'Mostrar notas acima de 7', 'Todas as notas', 'Sair'])
            if r == 1:
                nota = float(input('Nota: '))
                if nota >= 7 and nota < 10.1:
                    cadastrarNotaMaior(arq5, nota)
                    cadastrarNotaGeral(arq4, nota)

                elif nota <= 6.9 and nota >= 0:
                    cadastrarNotaGeral(arq4, nota)

                else:
                    print('\033[31mEssa nota é inválida!\033[m')

            elif r == 2:
                lerArquivoNotaMaior(arq5)

            elif r == 3:
                lerArquivoNotaGeral(arq4)

            elif r == 4:
                print('Saindo...')
                break

            else:
                print('\033[31mDigite uma opção válida\033[m')

            sleep(5)

    elif resposta == 5:
        cabecalho('Saindo')
        break

    else:
        print('\033[31mDigite uma opção válida\033[m')

    sleep(5)
