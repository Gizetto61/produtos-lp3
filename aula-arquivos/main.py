# abrir o arquivo

arquivo = open("dados.txt")

# conteudo = arquivo.read()
# conteudo = arquivo.readlines()

# print(conteudo)
# print(conteudo)

linhas = []
for linha in arquivo:
    linhas.append(linha.strip())
print(linhas)

arquivo.close()

# bloco with
with open("dados.txt", "r") as arquivo2:
    conteudo = arquivo2.read()
    print(conteudo)

# w = subtitui todo conteudo
# escrever mo arquivo
# with open("dados.txt", "w") as arquivo3:
#     arquivo3.write("Fritassssssss")

# a = adicionar uma nova linha (a = append)
with open("dados.txt", "a") as arquivo4:
    arquivo4.write("\nFritassss")

# ler o arquivo produtos.csv
# carregar uma memória na lista
# na qual cada produto é um dict

def linha_para_produto(linha):
    dados = linha.strip().split(",")
    return {
        "nome": dados[0],
        "descricao": dados[1],
        "preco": dados[2],
        "imagem": dados[3]
        }

def obter_produtos():
    with open("produtos.csv", "r") as arquivo_produtos:
        produtos = []
        for linha in arquivo_produtos:
            produto = linha_para_produto(linha)
            produtos.append(produto)

        return produtos

print(obter_produtos())

def salvar_produto(nome, descricao, preco, imagem):
    texto = f"\n{nome}, {descricao}, {preco}, {imagem}"
    with open("produtos.csv", "a") as arquivo_produtos:
        arquivo_produtos.write(texto)

salvar_produto("celular", "Tita foto", "1500.00", "celular.jpg")
salvar_produto("Tablet", "Tela Grande", "2500.00", "tablet.jpg")