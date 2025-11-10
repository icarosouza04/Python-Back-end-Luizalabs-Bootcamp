# Geradores

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2


for numero in meu_gerador(numeros = [1, 2, 3, 4, 5]):
    print(numero)
