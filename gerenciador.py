from main import Produto

def cadastrar_produto(produtos, nome, valor, quantidade):
    produto = Produto(nome, valor, quantidade)
    produtos.append(produto)
    return produto

def listar_produtos(produtos):
    return produtos

def calcular_imposto_produto(produto, taxa_imposto):
    valor_com_imposto = produto.calcular_imposto(taxa_imposto)
    return valor_com_imposto