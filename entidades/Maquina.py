from entidades.producto import Producto

class Maquina:
    def __init__(self, productos: list[Producto]):
        self.productos = productos

    def mostrar_inventario(self):
        print("Inventario")
        1 = 1
        for i in self.productos:
            print(f"{i}. {i.nombre} - ${i.precio} (Cantidad: {i.cantidad})")
            i += 1

    