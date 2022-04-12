'''

Titulo: Desarrollar la plantilla propuesta

Implementar esta class mediante las directrices de style code de python y documentar siguiendo las buenas practicas planteadas en clases.

Nota: Crear modulos para las clases Nodo y Arbol e implementar los metodos
basicos de getter y setter de cada clase propuesta
'''

class Node:
       def __init__(self, value):
       self.left = None
       self.right = None
       self.data = value

      def getData(self):
            return self.__data; 
      def setData(self, x):
            self.__data = x