class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


livros = []


while True:
    print("\n--- BIBLIOTECA ---")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Quantidade de livros")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")

        livro = Livro(titulo, autor)
        livros.append(livro)

        print("Livro cadastrado!")

    elif opcao == "2":
        if len(livros) == 0:
            print("Nenhum livro cadastrado.")
        else:
            for livro in livros:
                print("Título:", livro.titulo)
                print("Autor:", livro.autor)
                print("----------------")

    elif opcao == "3":
        busca = input("Digite o título: ")

        for livro in livros:
            if busca.lower() == livro.titulo.lower():
                print("Livro encontrado!")
                print("Título:", livro.titulo)
                print("Autor:", livro.autor)
                break
        else:
            print("Livro não encontrado.")

    elif opcao == "4":
        print("Quantidade de livros:", len(livros))

    elif opcao == "5":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")