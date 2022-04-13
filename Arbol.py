'''
Titulo: Clase Arbol para desarrollar una estructura ADT Tree
Nombre: Carlos Alberto Laime Navia
Fecha: 13/04/22
Version: v1.0
'''
from Nodo import Node
'''Importación de la clase "Node" para ayudar a crear la
clase Arbol'''
#. Clase Arbol que representará la estructura ADT Tree
class Arbol:
    ''' Metodo que crea la instancia de la clase Arbol'''
    def __init__(self):
        self.__raiz = None
    ''' Argumentos de la clase Arbol
	Nota: 
		El atributo "raiz" es privado definido para la 
		creación del Arbol y el Nodo origen del mismo
	Argumentos:
		"raiz": hace referencia a un Nodo que se tomará como 
		punto de origen para la creación de otros nodos 
		llamados también hojas.
	Retorna:
		"raiz": retornará la referencia del nodo.
	'''  
#. Metodos de la clase Arbol
#. Metodos getter y setter de la clase Arbol
    def getRaiz(self):
        ''' 
        Este método retorna la referencia en memoria de la 
        instancia "raiz".
        '''
        return self.__raiz;

    def setRaiz(self, x):
        '''
        Este método asignará la referencia de un nodo como 
        punto de origen del objeto árbol.
        '''
        self.__raiz = x
        