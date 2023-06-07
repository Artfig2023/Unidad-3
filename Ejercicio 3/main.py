from ClaseMenu import Menu
from ClaseManejadorTalleres import ManejoTalleres

if __name__ == '__main__':
    menu = Menu()
    talleres = ManejoTalleres()
    talleres.testtalleres()
    band = False
    while not band:
        print('------------- Menu -------------')
        print('1- Inscribir una persona')
        print('2-  Consultar inscripción')
        print('3- Consultar inscriptos')
        print('4- Registrar pago')
        print('5- Guardar inscripciones')
        print('6- Salir')
        print('-------------------------------')
        op = int(input('Opcion -> '))
        menu.opcion(op)
        band = op == '6'