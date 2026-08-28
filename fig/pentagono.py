import math
from .poligono_regular import PoligonoRegular

class Pentagono(PoligonoRegular):
    """
    Clase que representa un pentagono.

    Hereda de PoligonoRegular y define la lógica para calcular 
    el área de un pentagono de cinco lados iguales.
    """

    def __init__(self, longitud_lado: float) -> None:
        """
        Constructor de un Pentagono.

        Args:
            longitud_lado (float): La medida de uno de los lados del pentagono.
        """
        super().__init__(5, longitud_lado, "Pentagono")

    def calcular_area(self) -> float:
        """
        Calcula el área del pentagono.

        Returns:
            float: El área calculada.
        """
        perimetro = self.calcular_perimetro()
        apotema = self.longitud_lado/(2 * math.tan(math.pi / 5))
        area = (perimetro * apotema) / 2
        return area
