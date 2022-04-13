'''
Titulo: Clase Nodo para desarrollar una estructura ADT Tree
Autor: Carlos Alberto Laime Navia
Fecha: 13/04/22
Version: v1.0
'''
#. Clase Node que representará la estructura ADT Tree
class Node:
      ''' Metodo que crea la instancia de la clase Node''' 
      def __init__(self, value):
            self.__left = None
            self.__right = None
            self.__data = value
      ''' Argumentos de la clase Node
      Nota:
            los atributos "left", "right" y "data" son tres
            atributos privados definidos para la creación de
            las hojas que conformarán el árbol.
      Argumentos:
            "left": hace referencia a otro nodo que se debe
            encontrar a la izquierda de este.
            "right": hace referencia a otro nodo que se debe
            encontrar a la derecha de este.
            "data": hace referencia al valor que almacenará 
            el nodo actual.
      Retorna:
            "left": retornará la referencia del nodo izqdo.
            "right": retornará la referencia del nodo derecho.
            "data": retornará el valor que contenga el nodo 
            actual.
      '''
#. Metodos de la clase Node
#. Metodos getter y setter de la clase Node 
      def getData(self):
            ''' 
            Este métotodo devuelve el valor de un dato 
            almacenado en la instancia de la clase Node.
            '''
            return self.__data; 

      def setData(self, x):
            ''' 
            Este método settea el valor ingresado por 
            parámetro mediante la variable "x" y lo 
            almacena en el atributo "data" de la 
            instancia creada.
            '''
            self.__data = x
      
      def getLeft(self):
            '''
            Este métotodo devuelve el valor que contiene
            el atributo "Left" en la instancia de la 
            clase Node.
            '''
            return self.__left;
      
      def setLeft(self, x):
            ''' 
            Este método settea el valor ingresado por 
            parámetro mediante la variable "x" y lo 
            almacena en el atributo "Left" de la 
            instancia creada.
            '''
            self.__left = x
      
      def getRight(self):
            '''
            Este métotodo devuelve el valor que contiene
            el atributo "Right" en la instancia de la 
            clase Node.
            '''
            return self.__right;
      
      def setRight(self, x):
            ''' 
            Este método settea el valor ingresado por 
            parámetro mediante la variable "x" y lo 
            almacena en el atributo "Right" de la 
            instancia creada.
            '''
            self.__right = x

      
