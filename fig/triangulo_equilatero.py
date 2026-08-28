import math

from .poligono_regular import PoligonoRegular

class TrianguloEquilatero(PoligonoRegular):
    """
    Clase que representa un triángulo equilatero.

    Hereda de PoligonoRegular y define la lógica para calcular 
    el área especifica de un triángulo con lados iguales.
    """

    def __init__(self, longitud_lado: float) -> None:
        """
        Inicializa un TrianguloEquilatero.

        Args:
            longitud_lado (float): La medida de uno de los lados del triángulo.
        """
        super().__init__(3, longitud_lado, "TrianguloEquilatero")

    def calcular_area(self) -> float:
        """
        Calcula el área del triángulo.

        Return:
            float: El área calculada.
        """
        altura = math.sqrt(self.longitud_lado ** 2 - (self.longitud_lado / 2) ** 2)
        area = (self.longitud_lado * altura)/2
        return area


