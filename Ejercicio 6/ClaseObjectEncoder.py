import json
from pathlib import Path

class ObjectEncoder:

    def decodificadordiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'ManejoVehiculo':
                vehiculos = d['vehiculos']
                dvehiculos = vehiculos[0]
                manejador = class_()
                for i in range(len(vehiculos)):
                    dvehiculos = vehiculos[i]
                    class_name = dvehiculos.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dvehiculos['__atributos__']
                    unvehiculo = class_(**atributos)
                    manejador.agregarElemento(unvehiculo)
        return manejador

    def guardarJSONarchivo(self, diccionario, archivo):
        with Path(archivo).open('w', encodings='UTF-8') as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONarchivo(self, archivo):
        with Path(archivo).open(encoding='UTF-8') as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def convertiradiccionario(self, texto):
        return json.loads(texto)