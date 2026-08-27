"""
Paquete fig
===========

Contiene las clases que representan las figuras geométricas del proyecto.

Clases exportadas:
    - TrianguloEquilatero
    - Cuadrado
    - Pentagono
    - Circulo
"""

from .cuadrado import Cuadrado

from .triangulo_equilatero import TrianguloEquilatero

from .pentagono import Pentagono

from .circulo import Circulo

__all__ = [
    "TrianguloEquilatero",
    "Cuadrado",
    "Pentagono",
    "Circulo",
]