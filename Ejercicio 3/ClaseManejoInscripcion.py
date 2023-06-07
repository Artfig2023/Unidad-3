import csv

from ClaseInscripcion import Inscripcion
from ClaseManejadorTalleres import ManejoTalleres
from ClaseTaller import Taller
import datetime
from ClasePersona import Persona

class ManejoInscripcion:

    def __init__(self):
        self.__listainscriptos = []

    def inscripcion(self):
        nomtaller = input('Ingrese nombre del taller: ')
        untaller = ManejoTalleres.buscataller(nomtaller)
        if untaller is Taller:
            if untaller.getvacantes() > 0:
               fecha = datetime.date.today()
               verifpago = False
               nomb = input('Ingrese nombre: ')
               direc = input('Ingrese direccion: ')
               dni = input('Ingrese DNI: ')
               unapersona = Persona(nomb, direc, dni)
               unainscripcion = Inscripcion(fecha, verifpago, unapersona, untaller)
               self.__listainscriptos.append(unainscripcion)
               print('Inscripcion realizada')
            else: print('Error. Taller sin vacantes')

    def consultainscripcion(self):
        dni = int(input('Ingrese DNI: '))
        for i in range(len(self.__listainscriptos)):
            if self.__listainscriptos[i].getpago() == False:
                persona = self.__listainscriptos[i].getpersona()
                if persona.getdni() == dni:
                    taller = self.__listainscriptos[i].gettaller()
                    print('DNI del inscripto: {} --- Taller: {}'.format(dni, taller.getnombre()))
                    print('Monto adeudado: ${}'.format(taller.getmontoinscripcion()))

    def listarinscriptos(self):
        id = int(input('Ingrese ID del taller: '))
        for i in range(len(self.__listainscriptos)):
            taller = self.__listainscriptos[i].gettaller()
            if taller.getidtaller() == id:
                persona = self.__listainscriptos[i].getpersona()
                print(persona)

    def verificarpago(self):
        dni = int(input('Ingrese DNI: '))
        for i in range(len(self.__listainscriptos)):
            persona = self.__listainscriptos[i].getpersona()
            if persona.getdni() == dni:
                if self.__listainscriptos[i].get.getpago() == False:
                    self.__listainscriptos[i].realizarpago()
        print('Pago realizado')

    def guardarinscripciones(self):
        archivo = open('Inscripciones.csv', 'w')
        writer = csv.writer(archivo,delimiter=';')
        for i in range(len(self.__listainscriptos)):
            dni = self.__listainscriptos[i].getpersona().getdni()
            idtaller = self.__listainscriptos[i].gettaller().getidtaller()
            fechains = self.__listainscriptos[i].getfecha()
            pago = False
            if self.__listainscriptos[i].getpago():
                pago = True
            fila = [dni, idtaller, fechains.strftime('%d/%m/%Y'), str(pago)]
            writer.writerow(fila)
        archivo.close()
        print('Inscripciones guardadas')