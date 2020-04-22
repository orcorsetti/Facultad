# Implementar los metodos de la capa de negocio de socios.
from ejercicio_01 import Socio
from ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        soc = self.datos.buscar(id_socio)
        return soc

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        soc = self.datos.buscar_dni(dni_socio)
        return soc

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        lista = self.datos.todos()
        return lista

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        try:
            self.regla_1(socio)
            self.regla_2(socio)
            self.regla_3()
        except DniRepetido as e:
            print('Error: ', e.args)
            raise DniRepetido
        except LongitudInvalida as e:
            print('Error: ', e.args)
            raise LongitudInvalida
        except MaximoAlcanzado as e:
            print('Error: ', e.args)
            raise MaximoAlcanzado
        else:
            self.datos.alta(socio)
            return True

        

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        var = self.datos.baja(id_socio)
        return var

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        try:
            self.regla_2(socio)
        except LongitudInvalida as e:
            print('Error: ', e.args)
            raise LongitudInvalida
            #return False
        else:
            var = self.datos.modificacion(socio)
            if var is False:
                print("Error: el socio ingresado no se encuentra registrado.")
                return False
            else:
                return True

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        soc = self.datos.buscar_dni(socio.dni)
        """
        if soc is not None:
            if soc.dni == socio.dni:
                raise DniRepetido('El DNI ingresado ya esta registrado')
            else: 
                return True
        """
        if soc is not None:
            raise DniRepetido('El DNI ingresado ya se encuentra en uso')
        else:
            return True
            

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if (len(socio.apellido)<self.MIN_CARACTERES) or (len(socio.apellido)>self.MAX_CARACTERES) or (len(socio.nombre)<self.MIN_CARACTERES) or (len(socio.nombre)>self.MAX_CARACTERES):
            raise LongitudInvalida('El número de caracteres del nombre y/o apellido no son válidos.')
        else: 
            return True

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        lista = self.datos.todos()
        if len(lista) >= self.MAX_SOCIOS:
            raise MaximoAlcanzado('Se alcanzó la máxima cantidad de socios registrados')
        else:
            return True