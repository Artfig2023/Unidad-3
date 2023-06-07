from zope.interface import implementer
import numpy as np
from datetime import datetime
from datetime import date
from ClaseEmpleado import Empleado
from ClaseContratado import Contratado
from ClaseExterno import Externo
from ClasePlanta import Planta
from ClaseITesorero import ITesorero
from ClaseIGerente import IGerente
from ClaseMenu import Menu


@implementer(IGerente)
@implementer(ITesorero)
class ManejadorEmpleados:
    # Atributos
    __empleados = None
    __actual = 0
    __dimension = 0

    def __init__(self, dimension=0):
        self.__empleados = np.empty(dimension, dtype=Empleado)
        self.__dimension = dimension

    def addEmpleado(self, empleado):
        if isinstance(empleado, Empleado):
            if self.__actual == self.__dimension:
                self.__empleados.resize(len(self.__empleados) + 1)
                self.__dimension += 1
            self.__empleados[self.__actual] = empleado
            self.__actual += 1
        else:
            print('Error: No corresponde a un empleado.')

    def crearEmpleadoPlanta(self, dni, nom, dir, tel, basico, ant):
        try:
            if dni.isdigit() and tel.isdigit():
                basico = float(basico)
                ant = int(ant)
                newEmpleado = Planta(dni, nom, dir, tel, basico, ant)
                self.addEmpleado(newEmpleado)
            else:
                print('Error: No se pudo cargar el empleado de planta')
        except ValueError:
            print('Error: No se pudo cargar el empleado de planta')

    def crearEmpleadoContratado(self, dni, nom, dir, tel, fIn, fFin, CantH):
        try:
            if dni.isdigit() and tel.isdigit():
                # convierto string a objeto fecha hora
                fIn = datetime.strptime(fIn, '%d/%m/%y')
                fFin = datetime.strptime(fFin, '%d/%m/%y')
                # Quito la hora, convierte objeto datetime en date
                fIn = fIn.date()
                fFin = fFin.date()
                CantH = int(CantH)
                newEmpleado = Contratado(dni, nom, dir, tel, fIn, fFin, CantH)
                self.addEmpleado(newEmpleado)
            else:
                print('Error: No se pudo cargar el empleado contratado')
        except ValueError:
            print('Error: No se pudo cargar el empleado contratado')

    def crearEmpleadoExterno(self, dni, nom, dir, tel, tarea, fIn, fFin, viatico, cObra, mSeguro):
        try:
            if dni.isdigit() and tel.isdigit():
                # convierto string a objeto fecha hora
                fIn = datetime.strptime(fIn, '%d/%m/%y')
                fFin = datetime.strptime(fFin, '%d/%m/%y')
                # Quito la hora, convierte objeto datetime en date
                fIn = fIn.date()
                fFin = fFin.date()
                # Conversion de otros atributos
                viatico = float(viatico)
                cObra = float(cObra)
                mSeguro = float(mSeguro)
                if tarea.lower() in Externo.tareas:
                    newEmpleado = Externo(dni, nom, dir, tel, tarea, fIn, fFin, viatico, cObra, mSeguro)
                    self.addEmpleado(newEmpleado)
                else:
                    print('Error: Tarea no permitida')
            else:
                print('Error: No se pudo cargar el empleado externo')
        except ValueError:
            print('Error: No se pudo cargar el empleado externo')

    def cambiarHorasEmpC(self, dni):
        empleado = self.buscarPorDNI(dni)
        if isinstance(empleado, Contratado):
            header = self.__generaHeader('EMPLEADO CONTRATADO')
            empleado.mostrarempleado()
            print(header)
            horas = input('Ingrese horas trabajadas: ')
            empleado.addhora(horas)
            print(header)
            empleado.mostrarempleado()
            print(header)
        elif isinstance(empleado, Empleado):
            print('Error: Se ha ingresado el DNI de un empleado: {}'.format(empleado.getTipo().upper()))
        else:
            print('No se encontro el DNI indicado.')

    def totalTarea(self):
        menu = Menu()
        opciones = []
        i = 1
        for tarea in Externo.tareas:
            opciones.append('[{0}]- '.format(str(i)) + tarea)
            i += 1
        opciones.append('[0]- Volver al menu principal')
        menu.define_menu('TAREAS DISPONIBLES', opciones)
        menu.mostrarempleado()
        op = menu.selectOption()
        while op != 0:
            miTarea = Externo.tareas[op - 1]
            monto = 0.0
            fechaHoy = date.today()
            for i in range(self.__actual):
                empleado = self.__empleados[i]
                if isinstance(empleado, Externo):
                    tarea = empleado.gettarea()
                    if miTarea == tarea and fechaHoy < empleado.getfechafin():
                        monto += empleado.getnom()
            # Imprimo resultados:
            header = self.__generaHeader(miTarea.upper())
            print('| Monto total [$]: {:32}|'.format(str(monto)))
            print(header)
            print('Nota: Solo se consideran las tareas que no han finalizado.\n')
            input('Presione ENTER para continuar...')
            menu.define_menu('TAREAS DISPONIBLES', opciones)
            menu.mostrarempleado()
            op = menu.selectOption()

    # ----------------------------------------------#
    #            Ejercicio 4- Apartado 3           #
    # ----------------------------------------------#

    # Muestro empleados que recibiran ayuda solidaria
    def listBeneficiarios(self):
        header = self.__generaHeader('BENEFICIARIOS AYUDA SOLIDARIA')
        for i in range(self.__actual):
            empleado = self.__empleados[i]
            sueldo = empleado.calcSueldo()
            if sueldo < 25000:
                condicion = empleado.getTipo()
                print('| DNI: {:44}|'.format(empleado.getDNI()))
                print('| Nombre: {:41}|'.format(empleado.getNom()))
                print('| Direccion: {:38}|'.format(empleado.getDir()))
                print('| Sueldo [$]: {:37}|'.format(str(sueldo)))
                print('| Condicion: {:38}|'.format(condicion.upper()))
                print(header)

    # ----------------------------------------------#
    #            Ejercicio 4- Apartado 4           #
    # ----------------------------------------------#

    # Listar todos los empleados con su sueldo
    def listarEmpleados(self):
        header = self.__generaHeader('LISTA DE EMPLEADOS')
        for i in range(self.__actual):
            empleado = self.__empleados[i]
            sueldo = empleado.calcSueldo()
            print('| Nombre: {0:33}| {1:6}|'.format(empleado.getNom(), 'N° ' + str(i + 1)))
            print('| Telefono: {0:31}+-------|'.format(empleado.getTel()))
            print('| Sueldo [$]: {0:37}|'.format(str(sueldo)))
            print(header)

    # ----------------------------------------------#
    #  Ejericio 8 - Funcionalidades para TESORERO  #
    # ----------------------------------------------#

    def gastosSueldoPorEmpleado(self, dni):
        empleado = self.buscarPorDNI(dni)
        header = self.__generaHeader('GASTO DE SUELDO')
        if isinstance(empleado, Empleado):
            empleado.mostrarempleado()
            print(header)
            sueldo = empleado.calcSueldo()
            print(header)
            print('| SUELDO [$]: {:37}|'.format(sueldo))
            print(header)

    # ----------------------------------------------#
    #  Ejericio 8 - Funcionalidades para GERENTE   #
    # ----------------------------------------------#

    # Modifica el sueldo basico de un empleado de planta en particular
    def modificarBasicoEPlanta(self, dni, nuevoBasico):
        if nuevoBasico.isdigit():
            nuevoBasico = int(nuevoBasico)
            empleado = self.buscarPorDNI(dni)
            if isinstance(empleado, Planta):
                header = self.__generaHeader('MODIFICAR SUELDO BASICO EMPLEADO DE PLANTA')
                empleado.mostrarempleado()
                print(header)
                empleado.setbasico(nuevoBasico)
                print(' Sueldo basico modificado correctamente!')
                print(header)
                empleado.mostrarempleado()
                print(header)
            elif isinstance(empleado, Empleado):
                print('Error: Se ha ingresado el DNI de un empleado: {}'.format(empleado.getTipo().upper()))
            else:
                print('No se encontro el DNI indicado.')
        else:
            print('El nuevo basico debe ser un entero.')

    # Modifica el monto en concepto de viatico de un empleado externo en particular
    def modificarViaticoEExterno(self, dni, nuevoViatico):
        if nuevoViatico.isdigit():
            nuevoViatico = int(nuevoViatico)
            empleado = self.buscarPorDNI(dni)
            if isinstance(empleado, Externo):
                header = self.__generaHeader('MODIFICAR VIATICO EMPLEADO EXTERNO')
                empleado.mostrarempleado()
                print(header)
                empleado.setviatico(nuevoViatico)
                print(' Viatico modificado correctamente!')
                print(header)
                empleado.mostrarempleado()
                print(header)
            elif isinstance(empleado, Empleado):
                print('Error: Se ha ingresado el DNI de un empleado: {}'.format(empleado.getTipo().upper()))
            else:
                print('No se encontro el DNI indicado.')
        else:
            print('El nuevo viatico debe ser un entero.')

    # Modifica el valor que se paga por hora para un empleado contratado en particular
    def modificarValorEPorHora(self, dni, nuevoValorHora):
        if nuevoValorHora.isdigit():
            nuevoValorHora = int(nuevoValorHora)
            empleado = self.buscarPorDNI(dni)
            if isinstance(empleado, Contratado):
                header = self.__generaHeader('MODIFICAR VALOR HORA EMPLEADO CONTRATADO')
                empleado.mostrarempleado()
                print(header)
                empleado.setvalorhora(nuevoValorHora)
                print(' Valor por hora trabajada modificado correctamente!')
                print(header)
                empleado.mostrarempleado()
                print(header)
            elif isinstance(empleado, Empleado):
                print('Error: Se ha ingresado el DNI de un empleado: {}'.format(empleado.getTipo().upper()))
            else:
                print('No se encontro el DNI indicado.')
        else:
            print('El nuevo valor por hora debe ser un entero.')

    # ----------------------------------------------#
    #              Metodos auxiliares              #
    # ----------------------------------------------#

    # Devuelve el empleado segun el dni pasado por parametro
    def buscarPorDNI(self, dni):
        empleado = None
        if dni.isdigit():
            esta = False
            i = 0
            while i < self.__actual and not esta:
                if self.__empleados[i].getDNI() == dni:
                    esta = True
                else:
                    i += 1
            if esta:
                empleado = self.__empleados[i]
        else:
            print('DNI incorrecto.')
        return empleado

    # Genero un encabezado para los distintos apartados
    def __generaHeader(self, titulo):
        header = '+' + '-' * 50 + '+'
        print(header)
        print('|{0:^50}|'.format(titulo))
        print(header)
        return header