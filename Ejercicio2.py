import Producto

class Pedido:
      
    def __init__(self, lista_producto, lista_cantidades):
        self.__lista_producto = lista_producto
        self.__lista_cantidades = lista_cantidades
        
    def total_pedido(self):
        total = 0
        for (p, c) in zip(self.__lista_producto, self.__lista_cantidades):
            total = p.total_pedido(c) + total
        return total

    def mostrar_producto(self):
        for (p, c) in zip(self.__lista_producto, self.__lista_cantidades):
            print ('producto', p.nombre, 'cantidades', str(c))

producto = [p1. p2. p3]
cantidades = [5, 10, 15]

pedido = Pedido(producto, cantidades)