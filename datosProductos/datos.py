class Logica():
    precio = {
        'leche': 0.86,
        'galleta': 0.64,
        'cacao': 1.68,
        'naranja': 1.03,
        'aguacate': 4.67,
        'limon': 0.35,
        'magdalena': 1.45,
        'cereal': 1.56,
        'arroz': 0.48,
        'cafe': 1.34,
        'pimiento': 1.64,
        'sal': 0.23,
        'azucar': 0.79,
        'whisky': 14.85,
        'harina': 0.45,
        'huevo': 1.36
    }

    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def precioProducto(self):
        for llave, valor in self.precio.items():
            if self.producto == llave:
                return valor

    def calcular(self):

        for llave, valor in self.precio.items():

            if self.producto == llave:

                calc = float(self.cantidad) * valor

                return calc
