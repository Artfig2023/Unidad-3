import json
from pathlib import Path

class ObjectEncoder:
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_= eval(class_name)
        if class_name == 'Manejador':
            agentes = d['agentes']
            dagentes = agentes[0]
            manejador = class_()
            for i in range(len(agentes)):
                dagentes = agentes[i]
                class_name = dagentes.pop('__class__')
                class_ = eval(class_name)
                atributos = dagentes['__atributos__']
                unagente = class_(**atributos)
                manejador.agregar(unagente)
        return manejador

    def guardarJSON(self, diccionario, archivo):
        with Path(archivo).open(encoding="UTF-8") as destino:
            json.dumps(diccionario, destino, indent=4)
            destino.close()

    def leerJSON(self, diccionario, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def convertirdiccionario(self, texto):
        return json.load(texto)