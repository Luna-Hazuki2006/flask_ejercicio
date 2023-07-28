from flask import Flask, request, render_template, redirect,  url_for, flash
# 2 xbox ^ . drip coffee TOKYO - ZIP golf USA tokyo BESTBUY : 7 % @ 5 . yelp 
app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = '2x^.dcT-ZgUtB:7%@5.y'

@app.route("/palindromo/<palabra>", methods=['GET'])
def revisar(palabra):
    pass

@app.route("/tareas")
def tareas():
    tareas = [
        "Tocar la flauta", 
        "Mirar al techo", 
        "Responder los mensajes"
    ]
    return render_template('./tareas/index.html', tareas=tareas)

@app.route("/acerca")
def acerca():
    return render_template("./acerca/index.html")

mensajes_salvados = []

@app.route("/mensajes", methods=['GET', 'POST'])
def crear_mensaje():
    print(request.method)
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']

        if not titulo:
            flash("El título es obligatorio")
        if not contenido:
            flash('El contenido es obligatorio')

        if titulo and contenido:
            mensajes_salvados.append({'titulo': titulo, 'contenido': contenido})
            return redirect(url_for('mensajes'))
    return render_template("./crear_mensajes/index.html")

@app.route("/ver_mensajes")
def mensajes():
    return render_template("./mensajes/index.html", mensajes=mensajes_salvados)

if __name__ == '__main__':
    app.run(debug=True)