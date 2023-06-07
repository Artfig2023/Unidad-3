from ClaseSabor import Sabor
from ClaseManejadorHelado import ManejoHelado
import csv

class ManejoSabor:

    def __init__(self):
        self.__listasabores = []

    def testsabores(self):
        archivo = open('Sabores.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            unsabor = Sabor(fila[0], fila[1], fila[2])
            self.__listasabores.append(unsabor)
        print('Sabores cargados')

    def buscasabor(self, nombre):
        i = 0
        band = False
        sabor = None
        while i < len(self.__listasabores) and band == False:
            if self.__listasabores[i].getnombresabor().lower() == nombre.lower():
                sabor = self.__listasabores[i]
                band = True
            else:
                i += 1
        return sabor

    def cuentasabor(self, indice):
        self.__listasabores[indice-1].sumaacum()

    def muestramasvendidos(self):
        max = 0
        i = 0
        band = False
        while i < len(self.__listasabores) and band == False:
            if self.__listasabores.getacum() > max:
                max = self.__listasabores.getacum()
                print('{}'.format(self.__listasabores[i].getnombresabor()))

    def consultasabor(self):
        id = int(input('Ingrese numero del sabor: '))
        nomb = self.__listasabores[id - 1].getnombresabor()
        gramos = ManejoHelado.conseguirgramos(nomb)
        print('Helado: {} --- Cantidad de gramos vendidos: {}'.format(nomb, gramos))