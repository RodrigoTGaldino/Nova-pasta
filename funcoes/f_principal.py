from funcoes.funcao import (
    laod_json,
    adicinar_produto,
    save_json,
    lista_estoque,
    buscar_produto,
)


def menu():
    arq_cadastro = "cadastro.jason"
    cadastro = laod_json(arq_cadastro)

    while True:
        print(
            "\n1. Adicionar Produto ",
            "\n2. Estouque ",
            "\n3. Valor Produto ",
            "\n4. Sair",
        )

        opcao = input("\nEscolha uma opçao: ")

        if opcao == "1":
            produto = input("\nNome do Produto: ").capitalize()
            preco = float(input("Valor do produto: $").capitalize())
            quantidade = int(input("Quantidade de Produto: ").capitalize())

            novo_produto = {
                "produto": produto,
                "preco": preco,
                "quantidade": quantidade,
            }

            adicinar_produto(cadastro, novo_produto)
            save_json(cadastro, arq_cadastro)
            print("\nProduto cadastardo com sucesso!")

        elif opcao == "2":
            print("")
            lista_estoque(cadastro)

        elif opcao == "3":
            print("")
            nome_produto = input("Produto: ").capitalize()
            produto_encontrado = buscar_produto(cadastro, nome_produto)
            if produto_encontrado:
                print(
                    f'Produto: {produto_encontrado["produto"]} Preço: ${produto_encontrado["preco"]}'.capitalize()
                )
            else:
                print("Produto não encontrado.")

        elif opcao == "4":
            print("Sair")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
