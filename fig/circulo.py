
import math

from .figura import Figura


class Circulo(Figura):
    """
    Clase que representa un círculo.

    Hereda de Figura y define la lógica para calcular
    el área y perímetro de un círculo dado su diametro.
    """
    
    def __init__(self, diametro: float) -> None:
        """
        Inicializa un Círculo.

        Args:
            diametro (float): El diametro del círculo.
        """
        self.diametro = diametro
        self.tipo_figura = "Círculo"
    
    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro del círculo.

        Returns:
            float: El perímetro del círculo.
        """
        area = math.pi * self.diametro
        return area

    def calcular_area(self) -> float:
        """
        Calcula el área del círculo.

        Returns:
            float: El área del círculo.
        """
        area = (math.pi * (self.diametro / 2) ** 2)
        return area

    def __str__(self) -> str: 
       """
       Devuelve una representación en texto de la figura.

       Genera una cadena multilínea que incluye el tipo de figura, 
       la longitud de su lado (o diámetro), el área y el perímetro 
       con sus respectivas unidades.

       Returns:
           str: La información formateada de la figura.
       """
       resultados = (f"{self.tipo_figura} d = {self.diametro}\n"
                     f"Área: {self.calcular_area():.2f} u²\n"
                     f"Perímetro: {self.calcular_perimetro():.2f} u\n")
       return resultados
