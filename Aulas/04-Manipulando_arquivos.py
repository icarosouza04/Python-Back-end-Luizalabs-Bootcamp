# Abrindo e fechando arquivos

# file = open("exemplo.txt", "r") # Para ler um arquivo

# file = open("exemplo.txt", "w") # Para escrever um arquivo

# file = open("exemplo.txt", "a") # Para anexar conteúdo a um arquivo existente

# Lendo um arquivo

# file = open("exemplo.txt", "r") # Para abrir o arquivo no modo leitura
# print(file.read()) # Para ler o arquivo e exibir
# file.close() # Para fechar o arquivo

# arquivo = open(
#     r"C:\Users\Icaro Souza\Documents\Local_GitHub\Python-Back-end-Luizalabs-Bootcamp\Aulas\Meus_jogos_favoritos.txt",
#     "r")

# print(arquivo.read()) # Retorna o conteúdo do arquivo inteiro
# print(arquivo.readline()) # Retorna uma linha do arquivo por vez
# print(arquivo.readlines()) # Retorna uma lista com todas as linhas do arquivo

# while len(linha := arquivo.readline()): # Enquanto o tamanho da linha for maior que 0, atribui o conteúdo para a variável linha e exibe a mesma em loop
#     print(linha)

# arquivo.close()

# Escrevendo um arquivo

# file = open("exemplo.txt", "w") # Para abrir o arquivo no modo de escrita
# file.write("Olá, mundo!") # Para escrever algo no arquivo
# file.close() # Para fechar o arquivo

arquivo = open(
    r"C:\Users\Icaro Souza\Documents\Local_GitHub\Python-Back-end-Luizalabs-Bootcamp\Aulas\Meus_personagens_favoritos.txt",
    "w"
)

arquivo.write("Ma Chao") # Escreve o conteúdo no arquivo (recomendado para textos grandes)
arquivo.writelines(["\n", "Keiji Maeda", "\n", "Yoshitsune Minamoto", "\n", "Naomasa Li", "\n", "Kuro", "\n",
                    "Godfrey", "\n", "Fera Clerical", "\n", "Kratos", "\n", "Kassandra", "\n", "Jin Sakai"])
                   # Escreve o conteúdo no arquivo (um por vez)
arquivo.close()
