import json


def adicinar_produto(cadastro, produto):
    cadastro.append(produto)


def lista_estoque(cadastro):
    for produto in cadastro:
        print(
            f"Produto: {produto['produto']} | Preço: ${produto['preco']} | Quantidade: {produto['quantidade']}"
        )


def buscar_produto(cadastro, nome):
    for produto in cadastro:
        if produto["produto"] == nome:
            return produto
    return None


def save_json(cadastro, arq_mercadoria):
    with open(arq_mercadoria, "w") as arquivo:
        json.dump(cadastro, arquivo, indent=4)


def laod_json(arq_mercadoria):
    try:
        with open(arq_mercadoria, "r") as arquivo:
            cadastro = json.load(arquivo)
            return cadastro
    except FileNotFoundError:
        return []
