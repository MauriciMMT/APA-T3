"""
Clase Vector para la manipulación de vectores algebraicos.

Alumno: Maurici Mestres

Tests unitarios:

>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])

Multiplicación por escalar:
>>> v1 * 2
Vector([2, 4, 6])

Producto de Hadamard:
>>> v1 * v2
Vector([4, 10, 18])

Producto escalar:
>>> v1 @ v2
32

Componente paralela:
>>> v1 = Vector([2, 1, 2])
>>> v2 = Vector([0.5, 1, 0.5])
>>> v1 // v2
Vector([1.0, 2.0, 1.0])

Componente perpendicular:
>>> v1 % v2
Vector([1.0, -1.0, 1.0])
"""


class Vector:
    """
    Clase que representa un vector algebraico de dimensión arbitraria.

    Argumentos:
        iterable: Secuencia de valores numéricos que forman el vector.
    """

    def __init__(self, iterable):
        """
        Constructor de la clase Vector.

        Argumentos:
            iterable: Secuencia de valores numéricos.
        """
        self.vector = list(iterable)

    def __repr__(self):
        """Representación oficial del vector."""
        return f"Vector({self.vector!r})"

    def __str__(self):
        """Representación legible del vector."""
        return str(self.vector)

    def __len__(self):
        """Longitud (dimensión) del vector."""
        return len(self.vector)

    def __getitem__(self, index):
        """Acceso a elementos por índice."""
        return self.vector[index]

    def __add__(self, other):
        """
        Suma de dos vectores elemento a elemento.

        Argumentos:
            other: Vector a sumar.

        Salida:
            Nuevo Vector resultado de la suma.
        """
        return Vector(a + b for a, b in zip(self.vector, other.vector))

    def __neg__(self):
        """Negación del vector (cambio de signo de todos los elementos)."""
        return Vector(-a for a in self.vector)

    def __sub__(self, other):
        """
        Resta de dos vectores.

        Argumentos:
            other: Vector a restar.

        Salida:
            Nuevo Vector resultado de la resta.
        """
        return self + (-other)

    def __mul__(self, other):
        """
        Multiplicación de un vector por un escalar o producto de Hadamard con otro vector.

        Si `other` es un escalar (int o float), multiplica cada elemento del vector
        por ese escalar. Si `other` es otro Vector, devuelve el producto de Hadamard
        (multiplicación elemento a elemento).

        Argumentos:
            other: Escalar (int/float) o Vector.

        Salida:
            Nuevo Vector resultado de la operación.

        >>> Vector([1, 2, 3]) * 2
        Vector([2, 4, 6])
        >>> Vector([1, 2, 3]) * Vector([4, 5, 6])
        Vector([4, 10, 18])
        """
        if isinstance(other, (int, float)):
            return Vector(a * other for a in self.vector)
        return Vector(a * b for a, b in zip(self.vector, other.vector))

    def __rmul__(self, other):
        """
        Multiplicación por escalar con el escalar a la izquierda.

        Argumentos:
            other: Escalar (int/float).

        Salida:
            Nuevo Vector resultado de la multiplicación.

        >>> 2 * Vector([1, 2, 3])
        Vector([2, 4, 6])
        """
        return self.__mul__(other)

    def __matmul__(self, other):
        """
        Producto escalar (dot product) de dos vectores usando el operador @.

        Argumentos:
            other: Vector con el que calcular el producto escalar.

        Salida:
            Escalar resultado del producto escalar.

        >>> Vector([1, 2, 3]) @ Vector([4, 5, 6])
        32
        """
        return sum(a * b for a, b in zip(self.vector, other.vector))

    def __rmatmul__(self, other):
        """
        Producto escalar con el vector a la derecha.

        Argumentos:
            other: Vector con el que calcular el producto escalar.

        Salida:
            Escalar resultado del producto escalar.
        """
        return self.__matmul__(other)

    def __floordiv__(self, other):
        """
        Componente de self paralela (tangencial) a other usando el operador //.

        Calcula v1_paralela = (v1 · v2 / |v2|²) * v2

        Argumentos:
            other: Vector de referencia al que se proyecta.

        Salida:
            Nuevo Vector con la componente paralela a `other`.

        >>> Vector([2, 1, 2]) // Vector([0.5, 1, 0.5])
        Vector([1.0, 2.0, 1.0])
        """
        return (self @ other) / (other @ other) * other

    def __rfloordiv__(self, other):
        """
        Componente paralela cuando self es el vector de referencia (other // self).

        Argumentos:
            other: Vector a descomponer.

        Salida:
            Nuevo Vector con la componente de `other` paralela a self.
        """
        return Vector(other).__floordiv__(self)

    def __mod__(self, other):
        """
        Componente de self perpendicular (normal) a other usando el operador %.

        Calcula v1_perp = v1 - v1_paralela

        Argumentos:
            other: Vector de referencia respecto al que se obtiene la componente normal.

        Salida:
            Nuevo Vector con la componente perpendicular a `other`.

        >>> Vector([2, 1, 2]) % Vector([0.5, 1, 0.5])
        Vector([1.0, -1.0, 1.0])
        """
        return self - (self // other)

    def __rmod__(self, other):
        """
        Componente perpendicular cuando self es el vector de referencia (other % self).

        Argumentos:
            other: Vector a descomponer.

        Salida:
            Nuevo Vector con la componente de `other` perpendicular a self.
        """
        return Vector(other).__mod__(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
