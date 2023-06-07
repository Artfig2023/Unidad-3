class Login():
    __nuvel = ''
    def __init__(self, nivel='comun'):
        self.__nivel = nivel

    def login(self):
        header = '+' + '-' * 50 + '+'
        print(header)
        user = input('Usuario: ')
        password = input('Contrasenia: ')
        if user.lower() == 'uTesorero'.lower() and password == 'ag@74ck':
            self.__nivel = 'Tesorero'
            print('Usted ingreso como {0}'.format(self.__nivel.upper()))
        elif user.lower() == 'uGerente'.lower() and password == 'ufC77#!1':
            self.__nivel = 'Gerente'
            print('Usted ingreso como {0}'.format(self.__nivel.upper()))
        else:
            print('Error.. Usuario o contraseña incorrecta')

    def logout(self):
        if self.__nivel != 'comun':
            print('Sesion cerrada como {0}'.format(self.__nivel.upper()))
        else:
            print('Sesion ya cerrada')
        return self.__nivel

    def getnivel(self):
        return self.__nivel