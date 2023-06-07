from ClaseVehiculo import Vehiculo

class Usado(Vehiculo):
    __marca = ''
    __patente = ''
    __año = 0
    __kilometraje = 0
    def __init__(self, mod:str, cant:int, col:str, pre:float, marc:str, pat:str, anio:int, km:int):
        super().__init__(mod, cant, col, pre)
        self.__marca = marc
        self.__patente = pat
        self.__año = anio
        self.__kilometraje = km

    def getpatente(self): return self.__patente

    def calcularimporte(self):
        antiguedad = 2022 - self.__año
        if self.__kilometraje >= 100000:
            importe = super().getprecio() - (((super().getprecio() * 2) / 100) * antiguedad)
        else:
            importe = super().getprecio() - ((super().getprecio() / 100) * antiguedad)
        return importe

    def mostrar(self):
        print('Modelo: ', super().getmodelo())
        print('Cantidad de puertas ', super().getpuertas())
        print('Color: ', super().getcolor())
        print('Precio base: $', super().getprecio())
        print('Marca: ', self.__marca)
        print('Patente: ', self.__patente)
        print('Año: ', self.__año)
        print('Kilometraje: ', self.__kilometraje)
        print('Importe de venta: $', self.calcularimporte())

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                modelo = super().getmodelo(),
                cant_puetas = super().getpuertas(),
                color = super().getcolor(),
                preciobase = super().getprecio(),
                marca = self.__marca,
                patente = self.__patente,
                año = self.__año,
                kilometraje = self.__kilometraje
            )
        )
        return d