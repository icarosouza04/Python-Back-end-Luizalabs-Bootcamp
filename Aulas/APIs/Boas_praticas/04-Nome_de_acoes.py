from flask import Flask, request, jsonify

app = Flask(__name__)

# Abordagem Recomendada:
# URL: POST /users
# Aqui, estamos utilizando o método HTTP POST, que é tradicionalmente usado para criar novos recursos. 
# O recurso em questão é users. Portanto, POST /users indica a criação de um novo usuário.

@app.route("/users", methods = ["POST"])
def create_user():
    new_user = request.json
    # Lógica para criar o usuário
    return jsonify([{"message": "Usuário criado com sucesso!"}]), 201


if __name__ == "__main__":
    app.run(port = 5000)
