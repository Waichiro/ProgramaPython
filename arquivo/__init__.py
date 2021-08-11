from interface.modulo import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("\033[31mHouve um erro na criacao do arquivo!\033[m")
    else:
        print(f'O arquivo {nome} foi criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo\033[m')
    else:
        cabecalho('Pessoas cadastradas')
        print(a.read())
    finally:
        a.close()

def cadastrarNomes(arq2, nome='desconhecido'):
    try:
        a = open(arq2, 'at')
    except:
        print('\033[31mHouve um erro na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{nome}\n')
        except:
            print('\033[31mHouve um erro na hora de escrever os dados\033[m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()

def cadastrarPares(arq3, par):
    try:
        a = open(arq3, 'at')
    except:
        print('\033[31mHouve um erro na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{par}\n')
        except:
            print('\033[31mHouve um erro na hora de escrever os dados\033[m')
        else:
            print(f'Novo registro de {par} adicionado.')
            a.close()

def lerArquivoNotaMaior(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo\033[m')
    else:
        cabecalho('Pessoas cadastradas')
        print(a.read())
    finally:
        a.close()

def lerArquivoNotaGeral(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo\033[m')
    else:
        cabecalho('Pessoas cadastradas')
        print(a.read())
    finally:
        a.close()

def cadastrarNotaMaior(arq5, nota=0):
    try:
        a = open(arq5, 'at')
    except:
        print('\033[31mHouve um erro na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{nota}\n')
        except:
            print('\033[31mHouve um erro na hora de escrever os dados\033[m')
        else:
            print(f'Novo registro de {nota} adicionado.')
            a.close()

def cadastrarNotaGeral(arq4, nota=0):
    try:
        a = open(arq4, 'at')
    except:
        print('\033[31mHouve um erro na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{nota}\n')
        except:
            print('\033[31mHouve um erro na hora de escrever os dados\033[m')
        else:
            print(f'Novo registro de {nota} adicionado.')
            a.close()

def lerArquivoPares(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo\033[m')
    else:
        cabecalho('Número Pares Cadastrados')
        print(a.read())
    finally:
        a.close()


def lerArquivoSI(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo\033[m')
    else:
        cabecalho('Arquivo SI')
        print(a.read())
    finally:
        a.close()