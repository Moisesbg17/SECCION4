class Product:
    def __init__(self, name, price, quantity):
        self.name = name         # Nombre del producto
        self.price = price       # Precio del producto
        self.quantity = quantity # Cantidad del producto

    # Convierte el objeto a un diccionario para guardarlo en la base de datos
    def toDBCollection(self):
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

