from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from product import Product, Usuario, Prestamo

db = dbase.dbConnection()

app = Flask(__name__)

# Rutas de la aplicación
@app.route('/')
def home():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products=productsReceived)

# Method Post
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        product = Product(name, price, quantity)
        products.insert_one(product.toDBCollection())
        return redirect(url_for('home'))
    else:
        return notFound()

# Method delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name': product_name})
    return redirect(url_for('home'))

# Method Put
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        products.update_one({'name': product_name}, {'$set': {'name': name, 'price': price, 'quantity': quantity}})
        return redirect(url_for('home'))
    else:
        return notFound()

# Rutas para Usuarios
@app.route('/usuarios')
def usuarios():
    usuarios = db['usuarios']
    usuariosReceived = usuarios.find()
    return render_template('usuarios.html', usuarios=usuariosReceived)

@app.route('/add_usuario', methods=['POST'])
def add_usuario():
    usuarios = db['usuarios']
    nombre = request.form['nombre']
    correo = request.form['correo']
    celular = request.form['celular']

    if nombre and correo and celular:
        usuario = Usuario(nombre, correo, celular)
        usuarios.insert_one(usuario.toDBCollection())
        return redirect(url_for('usuarios'))
    else:
        return notFound()

@app.route('/delete_usuario/<string:nombre>')
def delete_usuario(nombre):
    usuarios = db['usuarios']
    usuarios.delete_one({'nombre': nombre})
    return redirect(url_for('usuarios'))

@app.route('/edit_usuario/<string:nombre>', methods=['POST'])
def edit_usuario(nombre):
    usuarios = db['usuarios']
    nuevo_nombre = request.form['nombre']
    correo = request.form['correo']
    celular = request.form['celular']

    if nuevo_nombre and correo and celular:
        usuarios.update_one(
            {'nombre': nombre},
            {'$set': {'nombre': nuevo_nombre, 'correo': correo, 'celular': celular}}
        )
        return redirect(url_for('usuarios'))
    else:
        return notFound()

# Rutas para Prestamos
@app.route('/prestamos')
def prestamos():
    prestamos = db['prestamos']
    prestamosReceived = prestamos.find()
    return render_template('prestamos.html', prestamos=prestamosReceived)

@app.route('/add_prestamo', methods=['POST'])
def add_prestamo():
    prestamos = db['prestamos']
    dia = request.form['dia']
    hora = request.form['hora']
    libro = request.form['libro']

    if dia and hora and libro:
        prestamo = Prestamo(dia, hora, libro)
        prestamos.insert_one(prestamo.toDBCollection())
        return redirect(url_for('prestamos'))
    else:
        return notFound()

@app.route('/delete_prestamo/<string:dia>')
def delete_prestamo(dia):
    prestamos = db['prestamos']
    prestamos.delete_one({'dia': dia})
    return redirect(url_for('prestamos'))

@app.route('/edit_prestamo/<string:dia>', methods=['POST'])
def edit_prestamo(dia):
    prestamos = db['prestamos']
    nuevo_dia = request.form['dia']
    hora = request.form['hora']
    libro = request.form['libro']

    if nuevo_dia and hora and libro:
        prestamos.update_one(
            {'dia': dia},
            {'$set': {'dia': nuevo_dia, 'hora': hora, 'libro': libro}}
        )
        return redirect(url_for('prestamos'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000)