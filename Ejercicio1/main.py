from ClaseMenu import Menu

if __name__ == '__main__':
    menu = Menu()
    band = False
    while not band:
        print('-------------- Menu --------------')
        print('1- Consultar Facultad')
        print('2- Consultar Carrera')
        print('3- Salir')
        print('----------------------------------')
        op = int(input('Opcion -> '))
        menu.opcion(op)
        band = op = '0'