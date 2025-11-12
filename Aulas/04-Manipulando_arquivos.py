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

# arquivo = open(
#     r"C:\Users\Icaro Souza\Documents\Local_GitHub\Python-Back-end-Luizalabs-Bootcamp\Aulas\Meus_personagens_favoritos.txt",
#     "w"
# )

# arquivo.write("Ma Chao") # Escreve o conteúdo no arquivo (recomendado para textos grandes)
# arquivo.writelines(["\n", "Keiji Maeda", "\n", "Yoshitsune Minamoto", "\n", "Naomasa Li", "\n", "Kuro", "\n",
#                     "Godfrey", "\n", "Fera Clerical", "\n", "Kratos", "\n", "Kassandra", "\n", "Jin Sakai"])
#                    # Escreve o conteúdo no arquivo (um por vez)
# arquivo.close()

# Gerenciando arquivos e diretórios

import os
import shutil
from pathlib import Path # Biblioteca para facilitar a identificação do caminho

ROOT_PATH = Path(__file__).parent # __file__ representa o caminho do arquivo

# os.mkdir("Exemplo") # Cria um diretório

# os.rename("Exemplo.txt", "Novo_exemplo.txt") # Renomeia o diretório

# os.remove("Novo_exemplo.txt") # Remove um arquivo

# shutil.move("Exemplo.txt", "Novo_exemplo.txt") # Mover um arquivo

# os.mkdir(ROOT_PATH / "Arquivos")

# arquivo2 = open("Novo_arquivo.txt" "w")
# arquivo2.close()

# os.rename(ROOT_PATH / "Novo_arquivo.txt", ROOT_PATH / "Arquivo_definitivo.txt")

# os.remove(ROOT_PATH / "Arquivo_definitivo.txt")

# shutil.move(ROOT_PATH / "Meus_personagens_favoritos.txt", ROOT_PATH / "Arquivos" / "Meus_personagens_favoritos.txt")

# Tratamento de exceções em manipulação de arquivos

# try:
#     arquivo = open(ROOT_PATH / "Arquivos")
# except FileNotFoundError as exc:
#     print(f"Este arquivo não existe. {exc}")
# except IsADirectoryError as exc:
#     print(f"Não foi possível encontrar o caminho deste arquivo. {exc}")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo. {exc}")
# except Exception as exc:
#     print(f"Algum problema ocorreu ao tentar abrir o arquivo. {exc}")

# Boas práticas na manipulação de arquivos

# with open(ROOT_PATH / "Arquivos" / "Meus_personagens_favoritos.txt", "r") as arquivo:
#     print(f"Lendo o arquivo: {arquivo}")
#     print(arquivo.read())

# try:
#     with open(ROOT_PATH / "Arquivos" / "Meus_personagens_favoritos.txt", "r") as arquivo:
#         print(f"Lendo o arquivo: {arquivo}")
#         print(arquivo.read())
# except IOError as erro:
#     print(f"Erro ao abrir o arquivo.\n{erro}")

# try:
#     with open(ROOT_PATH / "Arquivos" / "Arquivo_utf-8.txt", "w", encoding = "utf-8") as arquivo:
#         arquivo.write(f"Aprendendo a manipular arquivos utilizando o Python.")
# except IOError as erro:
#     print(f"Erro ao abrir o arquivo.\n{erro}")

try:
    with open(ROOT_PATH / "Arquivos" / "Arquivo_utf-8.txt", "r", encoding = "ascii") as arquivo:
        print(arquivo.read())
except IOError as erro:
    print(f"Erro ao abrir o arquivo.\n{erro}")
except UnicodeDecodeError as erro:
    print(f"Não foi possível abrir o arquivo. Há um caractere não compatível com o modelo de abertura.\n{erro}")
