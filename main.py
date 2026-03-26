from entidades.maquina import Maquina
from entidades.tipoproducto import TipoProducto
from entidades.producto import Producto

productos = [
    Producto("Coca", 20, 5, TipoProducto.Bebida),
    Producto("Sabritas", 18, 3, TipoProducto.Snack)
]

maquina = Maquina(productos)

try:
    while True:
        print("Elija una opcion \n1-ver inventario \n2-Comprar producto")
        opcion = int(input())

        if opcion == 1:
            maquina.mostrar_inventario()
            
        elif opcion == 2:
            print("¿Que producto desea comprar?")
            producto = input()
            print("¿Cuantos desea comprar?")
            cantidad = int(input())
            break
        else:
            print("Elija una opcion valida :)")
except ValueError:
    print("Ingrese un valor correcto")