# Tercera tarea de APA: Multiplicación de vectores y ortogonalidad

## Maurici Mestres

## Aviso Importante

> [!Caution]
>
> 
> El objetivo de esta tarea es programar en Python usando el pardigma de la programación
> orientada a objeto. Es el alumno quien debe realizar esta programación. Existen bibliotecas
> que, si lugar a dudas, lo harán mejor que él, pero su uso está prohibido.
>
> ¿Quiere saber más?, consulte con el profesorado.
  
## Fecha de entrega: 6 de abril a medianoche

## Clase Vector e implementación de la multiplicación de vectores

El fichero `algebra/vectores.py` incluye la definición de la clase `Vector` con los
métodos desarrollados en clase, que incluyen la construcción, representación y
adición de vectores, entre otros.

Añada a este fichero los métodos siguientes, junto con sus correspondientes
tests unitarios.

### Multiplicación de los elementos de dos vectores (Hadamard) o de un vector por un escalar

- Sobrecargue el operador asterisco (`*`, correspondiente a los métodos `__mul__()`,
  `__rmul__()`, etc.) para implementar el producto de Hadamard (vector formado por
  la multiplicación elemento a elemento de dos vectores) o la multiplicación de un
  vector por un escalar.

  - La prueba unitaria consistirá en comprobar que, dados `v1 = Vector([1, 2, 3])` y
    `v2 = Vector([4, 5, 6])`, la multiplicación de `v1` por `2` es `Vector([2, 4, 6])`,
    y el producto de Hadamard de `v1` por `v2` es `Vector([4, 10, 18])`.

- Sobrecargue el operador arroba (`@`, multiplicación matricial, correspondiente a los
  métodos `__matmul__()`, `__rmatmul__()`, etc.) para implementar el producto escalar
  de dos vectores.

  - La prueba unitaria consistirá en comprobar que el producto escalar de los dos
    vectores `v1` y `v2` del apartado anterior es igual a `32`.

### Obtención de las componentes normal y paralela de un vector respecto a otro

Dados dos vectores $v_1$ y $v_2$, es posible descomponer $v_1$ en dos componentes,
$v_1 = v_1^\parallel + v_1^\perp$ tales que $v_1^\parallel$ es tangencial (paralela) a
$v_2$, y $v_1^\perp$ es normal (perpendicular) a $v_2$.

> Se puede demostrar:
>
> - $v_1^\parallel = \frac{v_1\cdot v_2}{\left|v_2\right|^2} v_2$
> - $v_1^\perp = v_1 - v_1^\parallel$

- Sobrecargue el operador doble barra inclinada (`//`, métodos `__floordiv__()`,
  `__rfloordiv__()`, etc.) para que devuelva la componente tangencial $v_1^\parallel$.

- Sobrecargue el operador tanto por ciento (`%`, métodos `__mod__()`, `__rmod__()`, etc.)
  para que devuelva la componente normal $v_1^\perp$.

> Es discutible esta elección de las sobrecargas, dado que extraer la componente
> tangencial no es equivalente a ningún tipo de división. Sin embargo, está
> justificado en el hecho de que su representación matemática es dos barras
> paralelas ($\parallel$), similares a las usadas para la división entera (`//`).
>
> Por otro lado, y de manera *parecida* (aunque no idéntica) al caso de la división
> entera, las dos componentes cumplen: `v1 = v1 // v2 + v1 % v2`, lo cual justifica
> el empleo del tanto por ciento para la componente normal.

- En este caso, las pruebas unitarias consistirán en comprobar que, dados los vectores
  `v1 = Vector([2, 1, 2])` y `v2 = Vector([0.5, 1, 0.5])`, la componente de `v1` paralela
  a `v2` es `Vector([1.0, 2.0, 1.0])`, y la componente perpendicular es `Vector([1.0, -1.0, 1.0])`.

### Entrega

#### Fichero `algebra/vectores.py`

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno
  y los tests unitarios de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido
  de la función, los argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el
  uso de los estándares marcados por PEP-ocho.

#### Ejecución de los tests unitarios

```
$ python algebra/vectores.py -v
Trying:
    v1 = Vector([1, 2, 3])
Expecting nothing
ok
Trying:
    v2 = Vector([4, 5, 6])
Expecting nothing
ok
Trying:
    v1 * 2
Expecting:
    Vector([2, 4, 6])
ok
Trying:
    v1 * v2
Expecting:
    Vector([4, 10, 18])
ok
Trying:
    v1 @ v2
Expecting:
    32
ok
Trying:
    v1 = Vector([2, 1, 2])
Expecting nothing
ok
Trying:
    v2 = Vector([0.5, 1, 0.5])
Expecting nothing
ok
Trying:
    v1 // v2
Expecting:
    Vector([1.0, 2.0, 1.0])
ok
Trying:
    v1 % v2
Expecting:
    Vector([1.0, -1.0, 1.0])
ok
Trying:
    Vector([1, 2, 3]) * 2
Expecting:
    Vector([2, 4, 6])
ok
Trying:
    Vector([1, 2, 3]) * Vector([4, 5, 6])
Expecting:
    Vector([4, 10, 18])
ok
Trying:
    2 * Vector([1, 2, 3])
Expecting:
    Vector([2, 4, 6])
ok
Trying:
    Vector([1, 2, 3]) @ Vector([4, 5, 6])
Expecting:
    32
ok
Trying:
    Vector([2, 1, 2]) // Vector([0.5, 1, 0.5])
Expecting:
    Vector([1.0, 2.0, 1.0])
ok
Trying:
    Vector([2, 1, 2]) % Vector([0.5, 1, 0.5])
Expecting:
    Vector([1.0, -1.0, 1.0])
ok
12 items had no tests:
    __main__.Vector
    __main__.Vector.__add__
    __main__.Vector.__getitem__
    __main__.Vector.__init__
    __main__.Vector.__len__
    __main__.Vector.__neg__
    __main__.Vector.__repr__
    __main__.Vector.__rfloordiv__
    __main__.Vector.__rmatmul__
    __main__.Vector.__rmod__
    __main__.Vector.__str__
    __main__.Vector.__sub__
6 items passed all tests:
   9 tests in __main__
   1 tests in __main__.Vector.__floordiv__
   1 tests in __main__.Vector.__matmul__
   1 tests in __main__.Vector.__mod__
   2 tests in __main__.Vector.__mul__
   1 tests in __main__.Vector.__rmul__
15 tests in 18 items.
15 passed and 0 failed.
Test passed.
```

#### Código desarrollado

```python
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
```

#### Subida del resultado al repositorio GitHub y *pull-request*

La entrega se formalizará mediante *pull request* al repositorio de la tarea.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y
visualizarse correctamente en el repositorio, incluyendo la imagen con la ejecución de
los tests unitarios y el realce sintáctico del código fuente insertado.
