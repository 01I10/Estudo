from flask import Flask, request

from routes import insertUsuario

app = Flask("eCommerce")


@app.route("/compras", methods=["GET"])
def compreAqui():
    return "compreAqui"

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():

    body = request.get_json()


    usuario = insertUsuario(body['id'], body['name'], body['birth_date'], body['state'], body['phone'])

    return usuario

app.run()