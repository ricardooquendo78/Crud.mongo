from flask import Flask, render_template, request, jsonify, redirect, url_for
import database as dbase
from product import Product, Usuario, Prestamo
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
def get_db_connection():
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',      # Cambia por tu usuario
            password='',      # Cambia por tu contraseña
            database='libreria_db'
        )
        return db
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None

# Middleware para manejar la conexión a la base de datos
@app.before_request
def before_request():
    db = get_db_connection()
    if db is None:
        return "Error al conectar con la base de datos", 500
    request.db = db

@app.teardown_request
def teardown_request(exception):
    if hasattr(request, 'db') and request.db.is_connected():
        request.db.close()

# Función auxiliar para ejecutar consultas
def execute_query(query, params=None, fetch=False, fetch_one=False):
    cursor = request.db.cursor(dictionary=True)
    try:
        cursor.execute(query, params or ())
        if fetch:
            result = cursor.fetchall()
        elif fetch_one:
            result = cursor.fetchone()
        else:
            request.db.commit()
            result = None
        return result
    except mysql.connector.Error as err:
        request.db.rollback()
        print(f"Error en la consulta: {err}")
        return None
    finally:
        cursor.close()

# Rutas de la aplicación
@app.route('/')
def home():
    query = "SELECT * FROM products"
    productsReceived = execute_query(query, fetch=True)
    return render_template('index.html', products=productsReceived or [])

# Method Post
@app.route('/products', methods=['POST'])
def addProduct():
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        query = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
        execute_query(query, (name, price, quantity))
        return redirect(url_for('home'))
    else:
        return notFound()

# Method delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
    query = "DELETE FROM products WHERE name = %s"
    execute_query(query, (product_name,))
    return redirect(url_for('home'))

# Method Put
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        query = "UPDATE products SET name = %s, price = %s, quantity = %s WHERE name = %s"
        execute_query(query, (name, price, quantity, product_name))
        return redirect(url_for('home'))
    else:
        return notFound()

# Rutas para Usuarios
@app.route('/usuarios')
def usuarios():
    query = "SELECT * FROM usuarios"
    usuariosReceived = execute_query(query, fetch=True)
    return render_template('usuarios.html', usuarios=usuariosReceived or [])

@app.route('/add_usuario', methods=['POST'])
def add_usuario():
    nombre = request.form['nombre']
    correo = request.form['correo']
    celular = request.form['celular']

    if nombre and correo and celular:
        query = "INSERT INTO usuarios (nombre, correo, celular) VALUES (%s, %s, %s)"
        execute_query(query, (nombre, correo, celular))
        return redirect(url_for('usuarios'))
    else:
        return notFound()

@app.route('/delete_usuario/<string:nombre>')
def delete_usuario(nombre):
    query = "DELETE FROM usuarios WHERE nombre = %s"
    execute_query(query, (nombre,))
    return redirect(url_for('usuarios'))

@app.route('/edit_usuario/<string:nombre>', methods=['POST'])
def edit_usuario(nombre):
    nuevo_nombre = request.form['nombre']
    correo = request.form['correo']
    celular = request.form['celular']

    if nuevo_nombre and correo and celular:
        query = "UPDATE usuarios SET nombre = %s, correo = %s, celular = %s WHERE nombre = %s"
        execute_query(query, (nuevo_nombre, correo, celular, nombre))
        return redirect(url_for('usuarios'))
    else:
        return notFound()

# Rutas para Prestamos
@app.route('/prestamos')
def prestamos():
    query = "SELECT * FROM prestamos"
    prestamosReceived = execute_query(query, fetch=True)
    return render_template('prestamos.html', prestamos=prestamosReceived or [])

@app.route('/add_prestamo', methods=['POST'])
def add_prestamo():
    dia = request.form['dia']
    hora = request.form['hora']
    libro = request.form['libro']

    if dia and hora and libro:
        query = "INSERT INTO prestamos (dia, hora, libro) VALUES (%s, %s, %s)"
        execute_query(query, (dia, hora, libro))
        return redirect(url_for('prestamos'))
    else:
        return notFound()

@app.route('/delete_prestamo/<string:dia>')
def delete_prestamo(dia):
    query = "DELETE FROM prestamos WHERE dia = %s"
    execute_query(query, (dia,))
    return redirect(url_for('prestamos'))

@app.route('/edit_prestamo/<string:dia>', methods=['POST'])
def edit_prestamo(dia):
    nuevo_dia = request.form['dia']
    hora = request.form['hora']
    libro = request.form['libro']

    if nuevo_dia and hora and libro:
        query = "UPDATE prestamos SET dia = %s, hora = %s, libro = %s WHERE dia = %s"
        execute_query(query, (nuevo_dia, hora, libro, dia))
        return redirect(url_for('prestamos'))
    else:
        return notFound()

# Manejo de errores
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