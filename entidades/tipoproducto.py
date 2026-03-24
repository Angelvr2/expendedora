from entidades.maquina import Maquina
from enum import Enum

class TipoProducto(Enum):
    Bebida = "Bebida"
    Pan = "Pan"
    Snack = "Snack"
    Otro = "Otro"