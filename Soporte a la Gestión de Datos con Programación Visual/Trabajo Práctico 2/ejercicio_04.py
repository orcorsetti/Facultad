# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

"""import random


class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre= nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.generar_dni()

    def es_mayor_edad(self):
        if self.edad >= 21:
            return True
        else:
            return False

    # llamarlo desde __init__
    def generar_dni(self):
        self.dni = random.randint(10000000, 99999999)

    def print_data(self):
        print(self.__dict__)


class Estudiante(Persona):

    def __init__(self, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self)
        self.carrera= carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas


    def avance(self):
        return ((self.cantidad_aprobadas * 100) / self. cantidad_materias), '%'

    # implementar usando modulo datetime
    def edad_ingreso(self):
        pass


e = Estudiante("ISI",4,60,40)"""

import random as ran
from datetime import datetime
from ejercicio_03 import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self, nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cant_materias = cantidad_materias
        self.cant_aprobadas = cantidad_aprobadas

    def avance(self):
        return str((self.cant_aprobadas/self.cant_materias)*100) + "%"

    def edad_ingreso(self):
        anio_actual = datetime.now()
        anio_actual = anio_actual.year
        return self.edad - (anio_actual - self.anio)

    def devCarrera(self):
        return self.carrera


est = Estudiante("Andrés",22,"M",79,185,"ISI",2016, cantidad_materias = 60,cantidad_aprobadas = 40)

assert est.avance() == str((40/60)*100) + "%"
assert est.edad_ingreso() == 22 - (2019- 2016)


