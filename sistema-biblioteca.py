import csv
import os

# Nome do arquivo onde os livros serão armazenados
nome_planilha = "lista.csv"

# Cabeçalhos utilizados no arquivo CSV
colunas_planilha = ["Titulo", "Autor", "ISBN", "Ano", "Status"]


def carregar_livros(nome_arquivo):
    # Cria uma lista para armazenar os livros carregados
    livros = []

    # Verifica se o arquivo já existe
    if not os.path.exists(nome_arquivo):
        return livros

    # Abre o arquivo para fazer a leitura dos livros
    with open(nome_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for livro in leitor:
            livros.append(livro)

    return livros


def salvar_livros(nome_arquivo, livros):
    # Abre o arquivo para salvar os livros cadastrados
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas_planilha)

        # Escreve os cabeçalhos no arquivo
        escritor.writeheader()

        # Salva cada livro no arquivo
        for livro in livros:
            escritor.writerow(livro)


def cadastrar_livro(acervo, titulo, autor, isbn, ano):

    # Verifica se já existe um livro com o mesmo ISBN
    for livro in acervo:
        if livro["ISBN"] == isbn:
            return False, "Um livro com esse ISBN já foi cadastrado!"

    # Cria um novo livro com as informações recebidas
    novo_livro = {
        "ISBN": isbn,
        "Titulo": titulo,
        "Autor": autor,
        "Ano": ano,
        "Status": "Disponivel"
    }

    # Adiciona o novo livro ao acervo
    acervo.append(novo_livro)

    return True, f"Livro {titulo} foi cadastrado!"


def emprestar_livro(acervo, isbn):

    # Procura o livro pelo ISBN informado
    for livro in acervo:

        if livro["ISBN"] == isbn:

            # Verifica se o livro está disponível para empréstimo
            if livro["Status"] == "Disponivel":
                livro["Status"] = "Emprestado"
                return True, "Livro emprestado com sucesso!"

            else:
                return False, "Este livro já está emprestado."

    return False, "Livro não encontrado!"


def devolver_livro(acervo, isbn):

    # Procura o livro pelo ISBN informado
    for livro in acervo:

        if livro["ISBN"] == isbn:

            # Verifica se o livro está emprestado
            if livro["Status"] == "Emprestado":
                livro["Status"] = "Disponivel"
                return True, "Livro devolvido com sucesso!"

            else:
                return False, "Este livro já está disponível."

    return False, "Livro não encontrado!"


def buscar_livro(acervo, busca):

    # Cria uma lista para guardar os livros encontrados
    encontrados = []

    # Percorre o acervo procurando pelo título ou autor
    for livro in acervo:

        if (busca.lower() in livro["Titulo"].lower()
                or busca.lower() in livro["Autor"].lower()):

            encontrados.append(livro)

    return encontrados


def ordenar_livros(acervo, criterio):

    # Ordena os livros de acordo com o critério escolhido
    if criterio == 1:

        for i in range(len(acervo)):
            for j in range(i + 1, len(acervo)):

                if acervo[i]["Titulo"].lower() > acervo[j]["Titulo"].lower():
                    acervo[i], acervo[j] = acervo[j], acervo[i]

        return True, "Livros ordenados por título."

    elif criterio == 2:

        for i in range(len(acervo)):
            for j in range(i + 1, len(acervo)):

                if acervo[i]["Autor"].lower() > acervo[j]["Autor"].lower():
                    acervo[i], acervo[j] = acervo[j], acervo[i]

        return True, "Livros ordenados por autor."

    elif criterio == 3:

        for i in range(len(acervo)):
            for j in range(i + 1, len(acervo)):

                if int(acervo[i]["Ano"]) > int(acervo[j]["Ano"]):
                    acervo[i], acervo[j] = acervo[j], acervo[i]

        return True, "Livros ordenados por ano."

    else:
        return False, "Critério de ordenação inválido."


def listar_livros(acervo):

    # Verifica se existem livros cadastrados
    if len(acervo) == 0:
        print("Nenhum livro cadastrado.")
        return

    print("\n========== ACERVO ==========\n")

    # Percorre o acervo mostrando as informações dos livros
    for livro in acervo:

        print(f"Título : {livro['Titulo']}")
        print(f"Autor  : {livro['Autor']}")
        print(f"ISBN   : {livro['ISBN']}")
        print(f"Ano    : {livro['Ano']}")
        print(f"Status : {livro['Status']}")
        print("-" * 40)


# Programa principal

# Carrega os livros salvos no arquivo ao iniciar o programa
acervo = carregar_livros(nome_planilha)

# Mantém o menu funcionando até o usuário escolher sair
while True:

    print("\n========== BIBLIOTECA ==========")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar livros")
    print("7 - Sair")
    print("================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        ano = input("Ano de publicação: ")

        sucesso, mensagem = cadastrar_livro(
            acervo, titulo, autor, isbn, ano
        )

        print(mensagem)

        if sucesso:
            salvar_livros(nome_planilha, acervo)

    elif opcao == "2":

        isbn = input("Digite o ISBN do livro: ")

        sucesso, mensagem = emprestar_livro(acervo, isbn)

        print(mensagem)

        if sucesso:
            salvar_livros(nome_planilha, acervo)

    elif opcao == "3":

        isbn = input("Digite o ISBN do livro: ")

        sucesso, mensagem = devolver_livro(acervo, isbn)

        print(mensagem)

        if sucesso:
            salvar_livros(nome_planilha, acervo)

    elif opcao == "4":

        listar_livros(acervo)

    elif opcao == "5":

        busca = input("Digite o título ou autor: ")

        resultados = buscar_livro(acervo, busca)

        if len(resultados) == 0:
            print("Nenhum livro encontrado.")

        else:

            for livro in resultados:

                print(f"\nTítulo: {livro['Titulo']}")
                print(f"Autor: {livro['Autor']}")
                print(f"ISBN: {livro['ISBN']}")
                print(f"Ano: {livro['Ano']}")
                print(f"Status: {livro['Status']}")

    elif opcao == "6":

        print("\n1 - Ordenar por título")
        print("2 - Ordenar por autor")
        print("3 - Ordenar por ano")

        criterio = int(input("Escolha o critério: "))

        sucesso, mensagem = ordenar_livros(acervo, criterio)

        print(mensagem)

    elif opcao == "7":

        salvar_livros(nome_planilha, acervo)

        print("Programa encerrado.")

        break

    else:

        print("Opção inválida. Tente novamente.")