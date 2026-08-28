from .poligono_regular import PoligonoRegular

class Cuadrado(PoligonoRegular):
    """
    Clase que representa un caudrado.

    Hereda de PoligonoRegular y define la lógica para calcular 
    el área de una cuadrado.
    """

    def __init__(self, longitud_lado: float) -> None:
        """
        Inicializa un Cuadrado.

        Args:
            longitud_lado (float): La medida de uno de los lados del cuadrado.
        """
        super().__init__(4, longitud_lado, "Cuadrado")
        
    
    def calcular_area(self) -> float:
        """
        Calcula el área del cuadrado.

        Returns:
            float: El área calculada.
        """
        area = self.longitud_lado ** 2
        return area
