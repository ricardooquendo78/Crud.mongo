class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def toDBCollection(self):
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

class Usuario:
    def __init__(self, nombre, correo, celular):
        self.nombre = nombre
        self.correo = correo
        self.celular = celular

    def toDBCollection(self):
        return {
            'nombre': self.nombre,
            'correo': self.correo,
            'celular': self.celular
        }

class Prestamo:
    def __init__(self, dia, hora, libro):
        self.dia = dia
        self.hora = hora
        self.libro = libro

    def toDBCollection(self):
        return {
            'dia': self.dia,
            'hora': self.hora,
            'libro': self.libro
        }