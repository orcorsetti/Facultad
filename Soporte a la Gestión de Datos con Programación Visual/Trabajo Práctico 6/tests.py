# Implementar los casos de prueba descriptos.

import unittest

from ejercicio_01 import Socio
from capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        #socio no valido
        socioNV = Socio(dni=12345679, nombre='Juan', apellido='Perezasdasdasdasdsd')
        self.assertRaises(LongitudInvalida, self.ns.alta, socioNV)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        socio = self.ns.buscar(1)
        self.assertRaises(DniRepetido, self.ns.regla_1, socio)

        socio = Socio(dni=39456701, nombre='Pablo', apellido='Porta')
        self.assertTrue(self.ns.regla_1(socio))

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))
        
        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Nahasapemapetiloni', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)


    def test_regla_2_apellido_menor_3(self):
         # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))
        
        # apellido menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Nahasa', apellido='Pe')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
         # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))
        
        # apellido mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Nahasa', apellido='Nahasapemapetiloni')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        self.assertTrue(self.ns.regla_3())

    def test_baja(self):
        #id_socio no cargado
        self.assertFalse(self.ns.baja(459))

        #id_socio válido
        self.assertTrue(self.ns.baja(1))

    def test_buscar(self):
        #invalido, socio inexistente
        self.assertIsNone(self.ns.buscar(100))
        #valido
        self.assertIsNotNone(self.ns.buscar(1))

    def test_buscar_dni(self):
        #invalido, socio inexistente
        self.assertIsNone(self.ns.buscar_dni(100))
        #valido
        self.assertIsNotNone(self.ns.buscar_dni(12345678))

    def test_todos(self):
        self.assertEqual(len(self.ns.todos()),0)

    def test_modificacion(self):
        #socio1 = Socio()
        socio = Socio(dni=12345678, nombre='Naasdsg', apellido='Nahasapemapetiloni')
        self.assertRaises(LongitudInvalida,self.ns.modificacion,socio)


tn = TestsNegocio()
tn.setUp()
tn.tearDown()
tn.test_alta()
tn.test_regla_1()
tn.test_regla_2_nombre_menor_3()
tn.test_regla_2_nombre_mayor_15()
tn.test_regla_2_apellido_menor_3()
tn.test_regla_2_apellido_mayor_15()
tn.test_regla_3()
tn.test_buscar()
tn.test_buscar_dni()
tn.test_baja()
tn.test_todos()
tn.test_alta()
tn.test_modificacion()
