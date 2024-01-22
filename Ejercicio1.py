class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        self.__precio = valor
    
    def calcular_total(self, unidades):
        return self.__precio * unidades

    def __str__(self):
     return 'Codigo: ' + str(self.__codigo) + ', nombre: ' + self.__nombre + ', precio: ' + str(self.__precio)

P1 = Producto(1, 'Producto 1', 5)
P2 = Producto(2, 'Producto 2', 10)
P3 = Producto(3, 'Producto 3', 20) 

print(P1)
print(P2)
print(P3)

print(P1.calcular_total(5))
print(P2.calcular_total(5))
print(P3.calcular_total(5))