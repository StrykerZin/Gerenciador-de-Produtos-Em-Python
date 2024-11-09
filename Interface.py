import tkinter as tk
from tkinter import messagebox
from gerenciador import cadastrar_produto, listar_produtos, calcular_imposto_produto

def cadastrar_produto_callback():
    nome = entry_nome.get()
    valor_str = entry_valor.get()
    quantidade_str = entry_quantidade.get()

    # Verifica se os valores são numéricos
    if valor_str.replace('.', '', 1).isdigit() and quantidade_str.isdigit():
        valor = float(valor_str)
        quantidade = int(quantidade_str)
        produto = cadastrar_produto(produtos, nome, valor, quantidade)
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
    else:
        messagebox.showerror("Erro", "O valor e a quantidade devem ser números válidos.")

def listar_produtos_callback():
    listbox_produtos.delete(0, tk.END)
    produtos_cadastrados = listar_produtos(produtos)
    for produto in produtos_cadastrados:
        listbox_produtos.insert(tk.END, f"Nome: {produto.nome}, Valor: R${produto.valor}, Quantidade: {produto.quantidade}")

def calcular_imposto_produto_callback():
    produto_index = listbox_produtos.curselection()
    if produto_index:
        produto = produtos[produto_index[0]]
        taxa_imposto = 0.15  # 15% de imposto fixo
        valor_com_imposto = calcular_imposto_produto(produto, taxa_imposto)
        messagebox.showinfo("Imposto Calculado", f"Produto: {produto.nome}, Valor com Imposto: R${valor_com_imposto}")
    else:
        messagebox.showwarning("Atenção", "Por favor, selecione um produto.")

# Inicialização da interface
root = tk.Tk()
root.title("Gerenciador de Produtos")

# Componentes da interface
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_valor = tk.Label(root, text="Valor:")
label_valor.grid(row=1, column=0, padx=5, pady=5)
entry_valor = tk.Entry(root)
entry_valor.grid(row=1, column=1, padx=5, pady=5)

label_quantidade = tk.Label(root, text="Quantidade:")
label_quantidade.grid(row=2, column=0, padx=5, pady=5)
entry_quantidade = tk.Entry(root)
entry_quantidade.grid(row=2, column=1, padx=5, pady=5)

button_cadastrar = tk.Button(root, text="Cadastrar Produto", command=cadastrar_produto_callback)
button_cadastrar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

listbox_produtos = tk.Listbox(root, width=50)
listbox_produtos.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

button_listar = tk.Button(root, text="Listar Produtos", command=listar_produtos_callback)
button_listar.grid(row=5, column=0, padx=5, pady=5)

button_calcular = tk.Button(root, text="Calcular Imposto", command=calcular_imposto_produto_callback)
button_calcular.grid(row=5, column=1, padx=5, pady=5)

# Lista para armazenar os produtos
produtos = []

root.mainloop()