import json

def adicinar_produto(cadastro, produto):
    cadastro.append(produto)

def lista_estoque(cadastro):
    for produto in cadastro:
        print(
            f'ID: {produto ['id']}, Nome: {produto['nome']}, Valor: {produto['valor']}, Quantidade: {produto['quantidade']}'
        )