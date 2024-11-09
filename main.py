# Definicao da classe Produto#

class Produto:
    def __init__(self,nome,valor,quantidade):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade

#Calculador de imposto#

    def calcular_imposto(self, taxa_imposto):
        imposto = self.valor * taxa_imposto
        return self.valor + imposto
    

