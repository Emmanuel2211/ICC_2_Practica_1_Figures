

from .figura import Figura


class PoligonoRegular(Figura):
    """
    Clase que representa cualquier polígono regular.

    Hereda de Figura. Esta clase define el metodo para calcular 
    el perimetro de cualquier poligono regular.
    """

    def __init__(self, numero_lados: int, longitud_lado: float, tipo_figura: str) -> None:
        """
        Inicializa cualquier polígono regular.

        Args:
            numero_lados (int): El numero de lados del polígono regular.
            longitud_lado (float): La longitud que comparten todos los lados.
            tipo_figura (str): El nombre del tipo de poligono regular.
        """
        self.numero_lados = numero_lados
        self.longitud_lado = longitud_lado
        self.tipo_figura = tipo_figura
    
    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro del polígono regualar de n lados.

        Returns:
            float: El perímetro del polígono regular.
        """
        perimetro = self.numero_lados * self.longitud_lado
        return perimetro

    def __str__(self) -> str:
        """
        Devuelve una representación en texto de la figura.

        Genera una cadena multilínea que incluye el tipo de figura, 
        la longitud de su lado (o diámetro), el área y el perímetro 
        con sus respectivas unidades.

        Returns:
            str: La información formateada de la figura.
        """
        resultados = (f"{self.tipo_figura} l = {self.longitud_lado}\n"
                      f"Área: {self.calcular_area():.3f} u²\n"
                      f"Perímetro: {self.calcular_perimetro():.3f} u\n")
        return resultados
