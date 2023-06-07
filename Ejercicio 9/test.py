import unittest
from ClaseVehiculo import Vehiculo
from ClaseLista import Lista

class TestVehiculos(unittest.TestCase):
    def SetUp(self):
        self.listavehiculos = Lista()
        self.vehiculo1 = Vehiculo('Ford', 'Fiesta', 7000, 20000)
        self.vehiculo2 = Vehiculo('Renault', 'Kangoo', 4000, 30000)

    def test_agregarvehiculo(self):
        self.listavehiculos.agregarvehiculo(self.vehiculo1)
        self.assertEqual(self.listavehiculos.mostrardatos(0), self.vehiculo1)

    def test_insertarvehiculo(self):
        self.listavehiculos.agregarvehiculo(self.vehiculo1)
        self.listavehiculos.insertarvehiculo(1, self.vehiculo2)
        self.assertEqual(self.listavehiculos.mostrardatos(1), self.vehiculo2)

    def test_obtenervehiculo(self):
        self.listavehiculos.agregarvehiculo(self.vehiculo1)
        vehiculo = self.listavehiculos.mostrardatos(0)
        self.assertEqual(vehiculo, self.vehiculo1)

    def test_modificarprecio(self):
        self.listavehiculos.agregarvehiculo(self.vehiculo1)
        nprecio = 45000
        self.vehiculo1.setprecio(nprecio)
        self.assertEqual(self.vehiculo1.getprecio(), nprecio)

if __name__ == '__main__':
    unittest.main()