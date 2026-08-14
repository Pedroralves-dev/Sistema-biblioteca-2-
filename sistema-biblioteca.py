import csv# Importei o csv para usar como banco de dados
import os
nome_planilha = "lista.csv" # Nome do arquivo onde os livros serão armazenados
colunas_planilha = ["Titulo","Autor","ISBN","Ano","Status"] # Cabeçalhos utilizados no arquivo CSV


def carregar_livros(nome_arquivo):
    livros = []

    if not os.path.exists(nome_arquivo):
        return livros

    with open(nome_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for livro in leitor:
            livros.append(livro)

    return livros


def salvar_livros(nome_arquivo, livros):
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas_planilha)
        escritor.writeheader()

    for livro in livros:
        escritor.writerow(livro)


def cadastrar_livro(acervo,autor,ano,isbn,titulo):
    for livro in acervo:
        if livro['isbn'] == isbn:
            return False, "Um livro com esse ISBN já foi cadastrado!!"
    novo_livro = {"Isbn": isbn, "Titulo": titulo, "Autor": autor, "Ano": ano, "Status": "Disponivel"}

    acervo.append(novo_livro)
    return True, f"Livro {titulo} foi cadastrado!!"




