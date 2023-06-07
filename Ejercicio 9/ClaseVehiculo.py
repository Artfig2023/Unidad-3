import datetime


class Vehiculo:
    def __init__(self, modelo, puertas, color, preciobase, usado=False, marca=None, patente=None, año=0, kilometraje=0,
                 version=None, gastospat=0):
        self.__modelo = modelo
        self.__puertas = puertas
        self.__color = color
        self.__preciobase = preciobase
        self.__usado = usado
        self.__marca = marca
        self.__patente = patente
        self.__año = año
        self.__kilometraje = kilometraje
        self.__version = version
        self.__gastos_patentamiento = gastospat

    def __str__(self):
        return f"Modelo: {self.__modelo}, Puertas: {self.__puertas}, Color: {self.__color}, Importe de venta: {self.get_importe_venta()}"

    def getmodelo(self):
        return self.__modelo

    def getpuertas(self):
        return self.__puertas

    def getcolor(self):
        return self.__color

    def getprecio(self):
        return self.__precio_base

    def setprecio(self, precio_base):
        self.__precio_base = precio_base

    def getusado(self):
        return self.__usado

    def getmarca(self):
        return self.__marca

    def getpatente(self):
        return self.__patente

    def getaño(self):
        return self.__año

    def getkilometraje(self):
        return self.__kilometraje

    def getversion(self):
        return self.__version

    def set_usado(self, patente, marca, anio, kilometraje):
        self.patente = patente
        self.marca = marca
        self.anio = anio
        self.kilometraje = kilometraje

    def calcularimporteventausado(self):
        precio_venta = self.precio_base_venta
        if self.anio:
            precio_venta -= (2023 - self.anio) * 1000
        if self.kilometraje:
            precio_venta -= self.kilometraje * 0.1
        return precio_venta

    def getimporteventa(self):
        if self.__usado:
            return self.__precio_base * (
                        1 - 0.01 * (datetime.datetime.now().year - self.__año)) - self.__precio_base * 0.02 * (
                               self.__kilometraje - 100000) if self.__kilometraje > 100000 else self.__precio_base * (
                        1 - 0.01 * (datetime.datetime.now().year - self.__año))
        else:
            return self.__precio_base + self.__precio_base * 0.10 + self.__precio_base * 0.02 if self.__version == "full" else self.__precio_base + self.__precio_base * 0.10