from flask import Flask, render_template, request, jsonify, redirect, url_for
import models as dbase
from product import Product
from bson import ObjectId

db = dbase.dbConnection()
app = Flask(__name__)

@app.route('/')
def inicio():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products=productsReceived)

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

@app.route('/delete/<string:product_id>')
def delete(product_id):
    products = db['products']
    products.delete_one({'_id': ObjectId(product_id)})
    return redirect(url_for('inicio'))

@app.route('/edit/<string:product_id>', methods=['POST'])
def edit(product_id):
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        products.update_one(
            {'_id': ObjectId(product_id)},
            {'$set': {'name': name, 'price': price, 'quantity': quantity}}
        )
        return redirect(url_for('inicio'))
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
    app.run(debug=True)

