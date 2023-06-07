from ClaseVehiculo import Vehiculo
import json
import datetime

class Lista:
    def __init__(self):
        self.vehiculos = []

    def __iter__(self):
        self.__indice = 0
        return self

    def __next__(self):
        if self.__indice < len(self.vehiculos):
            vehiculo = self.vehiculos[self.__indice]
            self.__indice += 1
            return vehiculo
        else:
            raise StopIteration

    def insertarvehiculo(self, posicion, vehiculo):
        self.vehiculos.insert(posicion, vehiculo)

    def agregarvehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrarvehiculo(self, posicion):
        return self.vehiculos[posicion]

    def mostrarvehiculoeconomico(self):
        menor = 0.0
        economico = None
        for vehiculo in self.vehiculos:
            if vehiculo.getimporteventa() < menor:
                menor = vehiculo.getimporteventa()
                economico = vehiculo
        return economico

    def mostrardatos(self):
        for vehiculo in self.vehiculos:
            print(vehiculo)

    def buscarvehiculo(self, patente):
        for vehiculo in self.vehiculos:
            if vehiculo.getpatente() == patente:
                return vehiculo
        return None

    def dictvehiculo(self, dicvehiculos):
        vehiculos = []
        for diccionario in dicvehiculos:
            vehiculo = Vehiculo(
                diccionario['modelo'],
                diccionario['puertas'],
                diccionario['color'],
                diccionario['precio base'],
                diccionario['patente'],
                diccionario['marca'],
                diccionario['anio'],
                diccionario['kilometraje']
            )
            vehiculos.append(vehiculo)
        return vehiculos

    def cargaarchivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                contenido = f.read()
                if contenido:
                    diccionarios = json.loads(contenido)
                    self.vehiculos = self.dictvehiculo(diccionarios)
                else:
                    print(f'Archivo vacio.. Iniciando nueva lista')
                    self.vehiculos = []
        except FileNotFoundError:
            print(f'Error. Archivo no existe.. Iniciando nueva lista')
            self.vehiculos = []