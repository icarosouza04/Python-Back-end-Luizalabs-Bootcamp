from re import match
import functools

# Passagem de parâmetro

def mensagem(nome):
    print("Executando a função `mensagem`")
    return f"Olá, {nome}! Como vai?"


def mensagem_resposta(nome):
    print("Executando a função `mensagem_resposta`")
    return f"Eu estou bem!"


def executar(funcao):
    print("Executando a função `executar`")
    return funcao("Isabela")


# def executar(funcao, nome): Chamando a função com um segundo parâmetro
    
#     print("Executando a função `executar`")
#     return funcao(nome)

print(executar(mensagem))
print(executar(mensagem_resposta))

# print(executar(mensagem, "Rosa"))

# Função interna

def pai():
    print("Executando a função `pai`")
    
    def filho():
        print("Executando a função `filho`")


        def neto():
            print("Execuntando a função `neto")
            
        
        neto() # A função neto só existe na função filho, tal qual a função filho só existe na função pai. Ou seja, ambas são
               # internas e não podem ser chamadas fora da função pai.


    filho()

            
pai()

# Retorna função

def calculadora(operacao):
    def adicao(a, b):
        return a + b
    
    
    def subtracao(a, b):
        return a - b
    

    def multiplicacao(a , b):
        return a * b
    

    def divisao(a, b):
        return a / b
    

    match operacao:

        case "+":
            return adicao
        case "-":
            return subtracao
        case "*":
            return multiplicacao
        case "/":
            return divisao


resultado_adicao = calculadora("+")
print(resultado_adicao(5, 5))

resultado_subtracao = calculadora("-")
print(resultado_subtracao(20, 5))

resultado_multiplicacao = calculadora("*")
print(resultado_multiplicacao(4, 5))

resultado_divisao = calculadora("/")
print(resultado_divisao(125, 5))

# Primeiro decorador

def apresentacao(funcao):
    def nome():
        print("Qual é o seu nome?")
        funcao()
        print("É um prazer conhecê-lo, Icaro.")

    return nome


@apresentacao # O `@` serve para declarar a função como decoradora
def meu_nome():
    print("Meu nome é Icaro.")


# meu_nome = apresentacao(meu_nome)

meu_nome()

# Decorador com argumentos

def apresentacao(funcao):
    def nome(*args, **kwargs):
        print("Qual é o seu nome?")
        funcao(*args, **kwargs)
        print(f"É um prazer conhecê-lo, {nome}.")

    return nome


@apresentacao
def meu_nome(nome, idade):
    print(f"Meu nome é {nome}.")


meu_nome("Icaro", 21)

# Decorador retorna função decorada

def apresentacao(funcao):
    def nome(*args, **kwargs):
        print("Qual é o seu nome?")
        resultado = funcao(*args, **kwargs)
        print(f"É um prazer conhecê-lo, {nome}.")
        return resultado

    return nome


@apresentacao
def meu_nome(nome, idade):
    print(f"Meu nome é {nome}.")
    return nome.upper()


resultado = meu_nome("Icaro", 21)
print(resultado)

# Usando functools para alterar o nome da função

def apresentacao(funcao):
    @functools.wraps(funcao) # Essa função é responsável por manter os parâmetros e o nome correto da função. (instropecção)
    def nome(*args, **kwargs):
        print("Qual é o seu nome?")
        resultado = funcao(*args, **kwargs)
        print(f"É um prazer conhecê-lo, {nome}.")
        return resultado

    return nome


@apresentacao
def meu_nome(nome, idade):
    print(f"Meu nome é {nome}.")
    return nome.upper()


print(meu_nome.__name__)
