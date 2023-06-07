import csv
import numpy as np
from datetime import date
from ClaseEmpleado import Empleado
from ClaseEmpleadoPlanta import Planta
from ClaseEmpleadoContratado import Contratado
from ClaseEmpleadoExterno import Externo

class Coleccion:
    __arreEmpleados = None
    __dimension = 0
    __indice = 0
    def __init__(self):
        self.__arreEmpleados = np.empty(self.__dimension, dtype=Empleado)

    def agregaempleado(self, unempleado):
        self.__arreEmpleados[self.__indice] = unempleado
        self.__indice += 1

    def cargaplanta(self):
        archivo = open('Planta.csv')
        reader = csv.reader(archivo,delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                unplanta = Planta(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                self.agregaempleado(unplanta)
        archivo.close()
        print('Empleados de planta cargados')

    def cargacontratados(self):
        archivo = open('Contratados.csv')
        reader = csv.reader(archivo,delimiter= ';')
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                auxfecha = fila[4].split('/')
                fechainicio = date(int(auxfecha[0]), int(auxfecha[1]), int(auxfecha[2]))
                auxfecha = fila[5].split('/')
                fechafin = date(int(auxfecha[0]), int(auxfecha[1]), int(auxfecha[2]))
                uncontratado = Contratado(fila[0], fila[1], fila[2], fila[3], fechafin, fechafin, fila[6])
                self.agregaempleado(uncontratado)
        archivo.close()
        print('Empleados contratados cargados')

    def cargaexternos(self):
        archivo = open('Externos.csv')
        reader = csv.reader(archivo,delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = not band
            else:
                auxfecha = fila[5].split('/')
                fechainicio = date(int(auxfecha[0]), int(auxfecha[1]), int(auxfecha[2]))
                auxfecha = fila[6].split('/')
                fechafin = date(int(auxfecha[0]), int(auxfecha[1]), int(auxfecha[2]))
                viatico = float(fila[7])
                costo = float(fila[8])
                seguro = float(fila[9])
                unexterno = Externo(fila[0], fila[1], fila[2], fila[3], fila[4],
                                    fechainicio, fechafin, viatico, costo, seguro)
                self.agregaempleado(unexterno)
        archivo.close()
        print('Empleados externos cargados')

    def registrarhoras(self):
        dni = int(input('Ingrese DNI: '))
        band = False
        for i in range(self.__dimension):
            if self.__arreEmpleados[i].getdni() == dni:
                band = True
                if isinstance(self.__arreEmpleados[i], Contratado):
                    horas = int(input('Ingrese horas trabajadas hoy: '))
                    self.__arreEmpleados[i].sethoras(horas)
                    break
                else:
                    print('El DNI no pertenece a un empleado contratadp')
        if band == False:
            print('DNI incorrecto o inexistente')

    def totaltarea(self):
        op = int(input('Ingrese numero de tarea: \n1- Carpinteria\n2-Electricidad\n3-Plomeria'))
        assert op ('1' or '2' or '3', print('Opcion incorrecta'))
        if op == 1:
            tarea = 'Carpinteria'
        elif op == 2:
            tarea = 'Electricidad'
        elif op == 3:
            tarea = 'Plomeria'
        total = 0.0
        fechahoy = date.today()
        for i in range(len(self.__arreEmpleados)):
            if isinstance(self.__arreEmpleados[i], Externo):
                if self.__arreEmpleados[i].gettarea() == tarea:
                    if self.__arreEmpleados[i].getfechafin() > fechahoy:
                        total += self.__arreEmpleados[i].calcularsueldo()
        print('Tarea: {} --- Total a pagar: ${}'.format(str(tarea), float(total)))

    def ayudaeconomica(self):
        print('---- Lista de empleados que acceden a la ayuda economica ----')
        print('----------------------------------')
        print('Nombre / Telefono / Sueldo')
        for i in range(len(self.__arreEmpleados)):
            print('{} / {} / {}'.format(self.__arreEmpleados[i].getnombre(), str(self.__arreEmpleados[i].__telefono()),
                                        float(self.__arreEmpleados[i].calcularsueldo())))
        print('----------------------------------')

    def mostrarempleados(self):
        for i in range(len(self.__arreEmpleados)):
            if isinstance(self.__arreEmpleados[i], Planta):
                print('----------- Contratado -----------')
                print('Nombre: {}'.format(self.__arreEmpleados[i].getnombre()))
                print('DNI: {}'.format(self.__arreEmpleados[i].getdni()))
                print('Direccion: {}'.format(self.__arreEmpleados[i].getdireccion()))
                print('Telefono: {}'.format(self.__arreEmpleados[i].gettelefono()))
                print('Sueldo basico: ${}'.format(self.__arreEmpleados[i].getsueldobasico()))
                print('Antiguedad: {} años'.format(self.__arreEmpleados[i].getantiguedad()))
                print('Sueldo total: ${}'.format(self.__arreEmpleados[i].calcularsueldo()))
                print('---------------------------------')
            if isinstance(self.__arreEmpleados[i], Contratado):
                print('Nombre: {}'.format(self.__arreEmpleados[i].getnombre()))
                print('DNI: {}'.format(self.__arreEmpleados[i].getdni()))
                print('Direccion: {}'.format(self.__arreEmpleados[i].getdireccion()))
                print('Telefono: {}'.format(self.__arreEmpleados[i].gettelefono()))
                print('Fecha de inicio: {}'.format(self.__arreEmpleados[i].getfechainicio()))
                print('Fecha de finalizacion: {}'.format(self.__arreEmpleados[i].getfechafin()))
                print('Cantidad de horas trabajadas: {}'.format(self.__arreEmpleados[i].sethoras()))
                print('Valor por hora: ${}'.format(self.__arreEmpleados[i].getvalorhora()))
                print('Sueldo total: ${}'.format(self.__arreEmpleados[i].calcularsueldo()))
                print('---------------------------------')
            if isinstance(self.__arreEmpleados[i], Externo):
                print('Nombre: {}'.format(self.__arreEmpleados[i].getnombre()))
                print('DNI: {}'.format(self.__arreEmpleados[i].getdni()))
                print('Direccion: {}'.format(self.__arreEmpleados[i].getdireccion()))
                print('Telefono: {}'.format(self.__arreEmpleados[i].gettelefono()))
                print('Tarea: {}'.format(self.__arreEmpleados[i].gettarea()))
                print('Fecha de inicio: {}'.format(self.__arreEmpleados[i].getfechainicio()))
                print('Fecha de finalizacion: {}'.format(self.__arreEmpleados[i].getfechafin()))
                print('Monto del viatico: ${}'.format(self.__arreEmpleados[i].getviatico()))
                print('Costo de la obra: ${}'.format(self.__arreEmpleados[i].getcostobra()))
                print('Monto del seguro de vida: ${}'.format(self.__arreEmpleados[i].getmontoseguro()))
                print('Sueldo total: ${}'.format(self.__arreEmpleados[i].calcularsueldo()))
                print('---------------------------------')