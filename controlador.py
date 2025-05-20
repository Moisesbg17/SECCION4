from flask import Flask, render_template, request, jsonify, redirect, url_for
import models as dbase
from product import Product

# Conexión a la base de datos
db = dbase.dbConnection()

# Inicializar la app
app = Flask(__name__)

# Ruta principal: muestra los productos
@app.route('/')
def inicio():
    products = db['products']  # Colección "products"
    productsReceived = products.find()  # Obtener todos los productos
    return render_template('index.html', products=productsReceived)

# Ruta para agregar productos desde un formulario
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        product = Product(name, price, quantity)
        products.insert_one(product.toDBCollection())
        return redirect(url_for('inicio'))
    else:
        return notFound()

# Ruta para manejar errores 404
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)
