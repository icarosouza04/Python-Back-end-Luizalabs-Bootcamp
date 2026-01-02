from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route("/resource")
def get_resource():
    resource = None

    if resource:
        return jsonify(resource), 200
    else:
        abort(404, description = "Recurso não encontrado")


@app.errorhandler(400)
def bad_request(error):
    return str(error), 400


if __name__ == "__main__":
    app.run(port = 3000)


# 200 OK: Sucesso, o servidor cumpriu sua parte e entregou o que foi solicitado.
# 400 Bad Request: A requisição não foi entendida devido a um erro do cliente.
# 404 Not Found: O recurso solicitado não foi encontrado no servidor.
