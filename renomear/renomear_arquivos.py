# -*- coding: cp1252 -*-
import os
import shutil
PASTA_RELATORIO_CONTRATADOS = r'C:\ISS\relatorio_contratados'
PASTA_LIVRO_PRESTADOS = r'C:\ISS\livro_prestados'
# PASTA_RELATORIO_CONTRATADOS = r'C:\ISS\relatorio_contratados'
# PASTA_LIVRO_PRESTADOS = r'C:\ISS\livro_prestados'


def criar_nova_pasta(caminho):
    os.makedirs(caminho)


def criar_dicionario_empresas():
    with open('empresas.csv', encoding='cp1252') as arquivo:
        dic_empresas = {}
        cabecalho = True
        for registro in arquivo:
            emp = registro.strip().split(';')
            if not cabecalho:
                dic_empresas[emp[4]] = emp
            cabecalho = False
    return dic_empresas


def renomear_arquivos(old_name, new_name):
    os.rename(old_name, new_name)


def copiar_arquivos(origem, destino):
    shutil.copyfile(origem, destino)


def renomear_arquivos_contratados(empresas):

    for diretorio, subpastas, arquivos in os.walk(PASTA_RELATORIO_CONTRATADOS):

        for arquivo in arquivos:
            if arquivo != 'Thumbs.db':
                nome_empresa = empresas.get(arquivo.split(' ')[0])[1]
                data = arquivo.split(' ')[1][0:6]
                IM = arquivo.split(' ')[0]
                old_name = os.path.join(diretorio, arquivo)
                new_name = f'{PASTA_RELATORIO_CONTRATADOS}\\LIVRO ISSQN CONTRATADOS {nome_empresa} - IM {IM} {data}.pdf'
                print(old_name, new_name)
                renomear_arquivos(old_name, new_name)


def renomear_arquivos_prestados(empresas):

    for diretorio, subpastas, arquivos in os.walk(PASTA_LIVRO_PRESTADOS):

        for arquivo in arquivos:
            if arquivo != 'Thumbs.db':
                nome_empresa = empresas.get(arquivo.split(' ')[0])[1]
                data = arquivo.split(' ')[1][0:6]
                IM = arquivo.split(' ')[0]
                old_name = os.path.join(diretorio, arquivo)
                new_name = f'{PASTA_LIVRO_PRESTADOS}\\LIVRO ISSQN PRESTADOS {nome_empresa} - IM {IM} {data}.pdf'
                print(old_name, new_name)
                renomear_arquivos(old_name, new_name)


if __name__ == '__main__':

    dic_empresas = criar_dicionario_empresas()
    renomear_arquivos_contratados(dic_empresas)
    renomear_arquivos_prestados(dic_empresas)
