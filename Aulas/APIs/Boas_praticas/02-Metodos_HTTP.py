from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

# 1 - GET: Recuperar Recursos
# O método GET é usado para solicitar dados de um servidor. Ele não altera o estado dos dados no servidor; apenas os recupera.

@app.route("/users", methods = ["GET"]) # Método GET 
def get_users(): # Substantivo em rotas
    return jsonify(users), 200


# 2 - POST: Criar Novos Recursos
# O método POST é usado para enviar dados ao servidor para criar um novo recurso. Diferente do GET, ele altera o estado do servidor, geralmente criando um novo registro.

@app.route("/users", methods = ["POST"]) # Método POST
def add_users(): # Substantivo em rotas
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201


if __name__ == "__main__":
    app.run(debug = True)


novo_usuario = {"nome": "João", "idade": 30}
response = request.post("https://api.exemplo.com/usuarios/1", json = novo_usuario)

print(response.json())


# 3 - PUT/PATCH: Atualizar Recursos Existentes
#     PUT substitui completamente um recurso existente no servidor.
#     PATCH realiza uma atualização parcial, alterando apenas os campos especificados.

atualizacao_usuario = {"idade": 31} # Método PATCH
response = request.patch("https://api.exemplo.com/usuarios/1", json = atualizacao_usuario)


# 4 - DELETE: Excluir Recursos
# O método DELETE é usado para remover um recurso específico do servidor.

response = request.delete("https://api.exemplo.com/usuarios/1") # Método DELETE

print(response.json())

# Conclusão
# GET para recuperar dados sem modificar o servidor.
# POST para criar novos recursos.
# PUT ou PATCH para atualizar recursos existentes.
# DELETE para remover recursos.
