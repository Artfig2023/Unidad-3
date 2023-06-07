from ClaseHelado import Helado
from ClaseManejadorSabor import ManejoSabor
from ClaseSabor import Sabor

class ManejoHelado:

    def __init__(self):
        self.__listahelados = []

    def cargahelado(self):
        gramo = float(input('Ingrese gramos del helado: '))
        precio = float(input('Ingrese precio del helado: '))
        unhelado = Helado(gramo, precio)
        nomb = input('Ingrese nombre del sabor a añadir - Termina con "fin": ')
        while nomb.lower() != 'fin':
            unsabor = ManejoSabor.buscasabor(nomb)
            if unsabor is Sabor:
                unhelado.cargasabor(unsabor)
                ManejoSabor.cuentasabor(unsabor.getidsabor())
            else:
                print('Sabor no encontrado')
            nomb = input('Ingrese nombre del sabor a añadir - Termina con "fin": ')
        print('Helado cargado')

    def conseguirgramos(self, nomb):
        acum = 0
        for i in range(len(self.__listahelados)):
            sabores = self.__listahelados[i].getsabores()
            for j in range(len(sabores)):
                if sabores[j].getnombresabor().lower() == nomb.lower():
                    acum = self.__listahelados[i].getgramos() / len(sabores)
        return acum

    

    def obtenerimporte(self):
        importe = 0
        for i in range(len(self.__listahelados)):
            importe += self.__listahelados[i].getprecio()
        print('Importe total: ${}'.format(importe))