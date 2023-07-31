from flask import Flask, request, render_template, redirect,  url_for, flash

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = '2x^.dcT-ZgUtB:7%@5.y'

@app.route("/contactos")
def contactos():
    return render_template('./base/index.html')

lista_contactos = []

@app.route("/lista_contactos")
def listar():
    return render_template("./listar/index.html", lista_contactos=lista_contactos)

@app.route("/agregar_contacto", methods=['GET', 'POST'])
def agregar():
    print(request.method)
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        correo = request.form['correo']
        direccion = request.form['direccion']

        if not nombre:
            flash("El nombre es obligatorio")
        if not apellido:
            flash('El apellido es obligatorio')
        if not telefono:
            flash('El teléfono es obligatorio')
        if not correo:
            flash('El correo es obligatorio')
        if not direccion:
            flash('La dirección obligatoria')

        if nombre and apellido and telefono and correo and direccion:
            lista_contactos.append({
                'nombre': nombre, 'apellido': apellido, 
                'telefono': telefono, 'correo': correo, 
                'direccion': direccion})
            print(lista_contactos)
            return redirect(url_for('listar'))
    return render_template("./agregar/index.html")

@app.route("/contacto")
def ver():
    return render_template("./contacto/index.html")

if __name__ == '__main__':
    app.run(debug=True)