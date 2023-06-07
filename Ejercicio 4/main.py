from ClaseMenu import Menu

if __name__ == '__main__':
    menu = Menu()
    band = False
    while not band:
        print('--------- Menu ---------')
        print('1- Registrar horas')
        print('2- Total de tareas')
        print('3- Ayuda economica')
        print('4- Calcular sueldo')
        print('5- Salir')
        print('------------------------')
        op = int(input('Opcion -> '))
        menu.opcion(op)
        band = op == '5'