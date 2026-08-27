"""
Módulo figura
=============

Define la clase abstracta ``Figura``, que establece la interface común para
todas las figuras geométricas del proyecto.
"""

from abc import ABC, abstractmethod


class Figura(ABC):
    """
    Clase abstracta que representa una figura geométrica.

    Toda figura debe ser capaz de calcular su área y su perímetro.
    Además, proporciona una representación en texto con dicha
    información.
    """

    @abstractmethod
    def calcular_area(self) -> float:
        """
        Calcula el área de la figura.

        Este método debe ser implementado por las subclases.

        Returns:
            float:
                El área de la figura.

        Raises:
            NotImplementedError:
                Si una subclase no implementa este método.
        """
        raise NotImplementedError

    @abstractmethod
    def calcular_perimetro(self) -> float:
        """
        Calcula el perímetro de la figura.

        Este método debe ser implementado por las subclases.

        Returns:
            float:
                El perímetro de la figura.

        Raises:
            NotImplementedError:
                Si una subclase no implementa este método.
        """
        raise NotImplementedError

    def __str__(self) -> str:
        pass
