from ClaseMenu import Menu

if __name__ == '__main__':
    menu = Menu()
    band = False
    while not band:
        print('------------- Menu -------------')
        print('1- Insertar vehiculo')
        print('2- Agregar vehiculo')
        print('3- Mostrar vehiculo')
        print('4- Modificar precio base')
        print('5- Mostrar vehiculo economico')
        print('6- Listar vehiculos')
        print('7- Guardar datos de vehiculos')
        print('8- Cargar datos de vehiculos')
        print('9- Salir')
        print('--------------------------------')
        op = int(input('Opcion -> '))
        menu.opcion(op)
        band = op == '9'