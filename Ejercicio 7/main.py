from ClaseMenu import Menu

if __name__ == '__main__':
    menu = Menu()
    band = False
    while not band:
        print('------------------ Menu ------------------')
        print('1- Insertar agentes a la coleccion')
        print('2- Agregar agentes a la coleccion')
        print('3- Mostrar agente por posicion')
        print('4- Mostrar carrera de investigacion')
        print('5- Contar investigadores por area')
        print('6- Consultar sueldo de agentes')
        print('7- Listado e importe total de categoria')
        print('8- Guardar JSON')
        print('9- Cargar JSON')
        print('10 Salir')
        print('-----------------------------------------')
        op = int(input('Opcion -> '))
        menu.opcion(op)
        band = op == '0'