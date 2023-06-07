from ClaseVehiculo import Vehiculo

class Nuevo(Vehiculo):
    __marca = 'Ford'
    __version = ''
    def __init__(self, mod:str, cant:int, col:str, pre:float, ver:str):
        super().__init__(mod, cant, col, pre)
        self.__version = ver

    def calcularimporte(self):
        patent = ((10 * super().getprecio()) / 100)
        full = ((2 * super().getprecio()) / 100)
        if self.__version() == 'Full':
            importe = super().getprecio() + patent + full
        else:
            importe = super().getprecio() + patent
        return importe

    def mostrar(self):
        print('Modelo: ', super().getmodelo())
        print('Cantidad de puertas ', super().getpuertas())
        print('Color: ', super().getcolor())
        print('Precio base: $',super().getprecio())
        print('Marca: ', self.__marca)
        print('Version: ', self.__version)
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
                version = self.__version
            )
        )
        return d