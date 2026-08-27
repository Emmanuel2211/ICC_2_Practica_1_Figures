"""
Práctica 1
==========

Programa principal de la práctica.

Crea instancias de las figuras geométricas disponibles en el paquete
``fig`` y muestra en pantalla su nombre, área y perímetro.
"""

from fig import *


def main() -> None:
    """
    Función principal del programa.

    Crea un cuadrado, un triángulo equilátero, un pentágono y un círculo,
    para posteriormente imprimir la información de cada uno.

    Returns:
        None
    """
    cd = Cuadrado(3.45)
    tr = TrianguloEquilatero(2.98)
    pt = Pentagono(6.73)
    cr = Circulo(2.71)

    print(cd)
    print(tr)
    print(pt)
    print(cr)


if __name__ == "__main__":
    main()