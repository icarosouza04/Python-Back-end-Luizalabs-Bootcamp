from flask import Flask, request

# Aninhamento de rotas significa que você está criando uma URL que segue uma estrutura hierárquica para representar a relação entre diferentes recursos.
# Essa hierarquia faz com que a URL seja intuitiva e reflita como os dados estão organizados.

app = Flask(__name__)

@app.route("/users/<int:userID>/orders")
def get_orders(userID):
    # Lógica para buscar os pedidos do usuário
    return f"Pedidos do usuários {userID}"


if __name__ == "__main__":
    app.run(debug = True)

