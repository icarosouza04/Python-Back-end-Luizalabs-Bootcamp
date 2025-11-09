import os

class JogosFavoritos: # Usei o Chat-GPT para me auxiliar a encontrar o arquivo (O arquivo não estava sendo encontrado)
    def __init__(self, filename):
        # Obtém o diretório onde o script está
        base_dir = os.path.dirname(__file__)
        # Monta o caminho completo do arquivo
        full_path = os.path.join(base_dir, filename)
        # Abre o arquivo
        self.file = open(full_path, encoding="utf-8")
        print("Arquivo aberto em:", full_path)
        

    def __iter__(self):
        return self
    

    def __next__(self):
        line = self.file.readline()

        if line == "":
            self.file.close()
            raise StopIteration
        return line.strip()

        

for jogos in JogosFavoritos("Meus_jogos_favoritos.txt"):
    print(jogos)
