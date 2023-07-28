from flask import Flask, request, render_template, redirect,  url_for, flash

app = Flask(__name__, template_folder="templates")

@app.route("/contactos")
def contactos():
    return render_template('./base/index.html')

@app.route("/lista_contactos")
def listar():
    return render_template("./acerca/index.html")

@app.route("/agregar_contacto", methods=['GET', 'POST'])
def agregar():
    print(request.method)
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']

        if not titulo:
            flash("El título es obligatorio")
        if not contenido:
            flash('El contenido es obligatorio')

        if titulo and contenido:
            return redirect(url_for('mensajes'))
    return render_template("./crear_mensajes/index.html")

@app.route("/contacto")
def ver():
    return render_template("./contacto/index.html")

if __name__ == '__main__':
    app.run(debug=True)