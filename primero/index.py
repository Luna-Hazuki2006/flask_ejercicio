from flask import Flask, request, render_template

app = Flask(__name__, template_folder="./prueba")

@app.route("/")
def hola_mundo():
    return "¡Hola Mundo!"

@app.route("/ana", methods=["GET"])
def hola():
    return "¡Hola Ana!"

@app.route("/saludar/<nombre>", methods=["GET"])
def saludar(nombre):
    return f"¡Hola {nombre}!"

@app.route("/despedir", methods=["GET"])
def despedir():
    nombre = request.args.get("nombre")
    return f"Adiós {nombre}"

@app.route("/mensaje", methods=["POST"])
def mesajear():
    cuerpo = request.get_json()
    nombre = cuerpo["nombre"]
    edad = cuerpo["edad"]
    return f"Hola {nombre}, tienes {edad} años"

@app.route("/saludos/<nombre>", methods=["GET"])
def saludos(nombre):
    return render_template("index.html", nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)