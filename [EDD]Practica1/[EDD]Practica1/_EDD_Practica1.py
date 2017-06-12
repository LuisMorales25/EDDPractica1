# -*- encoding: utf-8 -*-

import sys
import os
from xml.etree import ElementTree

   
class inicio:
 leido=False
 def leerArchivo(self,NombreArchivo,Direccion):
    #nombre_archivo="prueba.xml"
    nombre_archivo=NombreArchivo+".xml"
    archivo_completo= os.path.abspath(os.path.join(Direccion,nombre_archivo))
    dom=ElementTree.parse(archivo_completo)
    operaciones= dom.findall('operaciones/operacion')
    dimensionX=dom.findall('matriz/x')
    dimensionY=dom.findall('matriz/y')
    for c in dimensionX:
        #print ("componente x: "+c.text)
        x=c.text
        ojalaX.encolar(c.text)
    for c in dimensionY:
        #print ("componente y: "+c.text)
        y=c.text
        ojalaY.encolar(c.text)
    for c in operaciones:
        #print (c.text)
        colaFunciones.encolar(c.text)
      #self.crearMatriz(x,y)
    #print "eje x: "+ojalaX.primero.dato
    #print "eje y: "+ojalaY.primero.dato
    self.leido=True  

 def crear(self):
     nombre = raw_input("Nombre de usuario: ")
     if listaUser.buscar(nombre):
         print "usuario ya existe"
         self.crear()
     else:
        listaUser.agregar_inicio(nombre)
        
    
     password = raw_input("Contrase�a: ")
     listaPassword.agregar_inicio(password)
     #print nombre,password
     #listaUser.recorrer_inicio_fin()
     #listaPassword.recorrer_inicio_fin()
     self.menu()

 def menu_opcion2(self):
     usuario=raw_input("Nombre de usuario: ")
     if listaUser.buscar(usuario):
         contra=raw_input("Ingrese contraseña: ")
         if listaPassword.buscar(contra):
          self.subMenuOpcion2()
    
         else:
             print "contraseña invalida"
             self.menu_opcion2()
     else:
         print "usuario invalido"
         self.menu()
 
 def subMenuOpcion2(self):
      print "MENU\n"
      print "1. Leer archivo"
      print "2. Resolver operaciones"
      print "3. Operar matriz"
      print "4. Mostrar usuarios"
      print "5. Mostrar cola"
      print "6. Cerrar sesion"
      opcion2=input("Elija una opcion: ")
      if opcion2==1:
                 direccion=raw_input("ruta del archivo\n")
                 nombre_archivo=raw_input("ingrese nombre del archivo\n")
                 self.leerArchivo(nombre_archivo,direccion)
                 self.subMenuOpcion2()

      if opcion2==2:
               if self.leido==True:
                 self.subMenuopcion2Parte2()
               else:
                  print "Falta leer archivo"
                  self.subMenuOpcion2()
        
      if opcion2==3:
                 print "OPERAR MATRIZ\n"
                 print "1. Ingresar dato"
                 print "2. Operar Trasnpuesta"
                 print "3. Mostrar matriz original"
                 print "4. Mostrar matriz transpuesta"
                 print "5. Regresar"
                 op3=input("Elija una opcion: ")
                 if op3==1:
                     print "calmao aun falta"
                 if op3==2:
                     print "calmao aun falta"
                 if op3==3:
                     matriz=ListaMatriz()
                     print "eje X: "+ojalaX.primero.dato
                     print "eje Y: "+ojalaY.primero.dato
                     matriz.alto_matriz(int(ojalaY.primero.dato),int(ojalaX.primero.dato))
                     self.subMenuOpcion2()
                 if op3==4:
                     print "calmao aun falta"
                 if op3==5:
                     self.subMenuOpcion2()
      if opcion2==4:
                 print "primero a ultimo"
                 listaUser.recorrer_fin_inicio_horizontal()
                 print "***********"
                 print "ultimo a primero"
                 listaUser.recorrer_inicio_fin_Horizontal()
                 self.subMenuOpcion2()
      if opcion2==5:
                 colaFunciones.recorrerCola()
                 #print "calmao aun falta"
                 self.subMenuOpcion2()
      if opcion2==6:
                 self.menu()  
 
 def funcion(self,funcion):
    pilaPrueba=cola()
    pila2=pila()
    prueba=funcion

    #print  prueba.split(" ")
    aber=prueba.split(" ")
    for x in aber:
        pilaPrueba.encolar(x)
    #pilaPrueba.recorrerCola()
    #print "*********"
    aux=pilaPrueba.primero
    while aux:
        pila2.push(aux.dato)
        aux=aux.siguiente
        if  aux==None:
            break
    #pila2.recorrerPila()
    #print"*********"
    while pila2.primero:
        if pila2.primero.siguiente.siguiente.dato=="+" or pila2.primero.siguiente.siguiente.dato=="-" or pila2.primero.siguiente.siguiente.dato=="*":
            valor1=int(pila2.primero.dato)
            pila2.pop()
            valor2=int(pila2.primero.dato)
            pila2.pop()
            operador=pila2.primero.dato
            pila2.pop()
        else:
            valor1=int(pila2.primero.siguiente.dato)
            primerValor=pila2.primero.dato
            pila2.pop()
            valor2=int(pila2.primero.siguiente.dato)
            pila2.pop()
            operador=pila2.primero.siguiente.dato
            pila2.pop()
            pila2.pop()
            pila2.push(primerValor)
        if operador=="+":
            resultado=valor1+valor2
        elif operador=="-":
            resultado=valor1-valor2
        elif operador=="*":
            resultado=valor1*valor2
       # print int(resultado)
        num1=str(valor1)
        num2=str(valor2)
        res=str(resultado)
        print num1+operador+num2+"="+res
        #print "*****************"
        pila2.push(resultado)
        #pila2.recorrerPila()
        if pila2.primero==pila2.Ultimo:
            break
    print "Resultado: "+res
    print "*****************"
        

 def subMenuopcion2Parte2(self):
       print "RESOLVER OPERACIONES\n"
       print "1. Operar siguiente"
       print "2. Regresar"
       op2=input("Elija una opcion: ")
       if op2==1:
          if colaFunciones.Ultimo==None:
              print "No hay mas funciones"
          else:
                LastValue=colaFunciones.Ultimo.dato
                print "funcion a evaluar: "+LastValue
                self.funcion(LastValue)
          colaFunciones.desencolar()
          self.subMenuopcion2Parte2()
       if op2==2:
          self.subMenuOpcion2()
 def operar(self,num1,num2,operador):
    valor1=int(num1)
    valor2=int(num2)
    if operador=="+":
      resultado=valor1+valor2
    elif operador=="-":
        resultado=valor1-valor2
    elif operador=="*":
        resultado=valor1*valor2
    print int(resultado)

    
 def menu(self):
     print"INICIO\n"
     print "1. Crear Usuario"
     print "2. Ingresar al sistema"
     print "3. Salir del programa"
     opcion=input("Elija una opcion: ")
     if opcion==1:
        self.crear()  
     if opcion==2:
        self.menu_opcion2()             
     if opcion==3:
        sys.exit()
       #self.operar("5","3","*")


class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None

class ListaCircularDoblementeEnlazada:
    def __init__(self):
        self.primero=None
        self.Ultimo=None

    def vacia(self):
        if self.primero==None:
            return True
        else:
            return False

    def agregar_inicio(self,dato):
        if self.vacia():
            self.primero = self.Ultimo=Nodo(dato)
        else:
            aux=Nodo(dato)
            aux.siguiente=self.primero
            self.primero.anterior=aux
            self.primero=aux
        self.__unirNodos()


    def agregar_final(self, dato):
        if self.vacia():
            self.primero=self.Ultimo=Nodo(dato)
        else:
            aux=self.Ultimo
            self.Ultimo=aux.siguiente=Nodo(dato)
            self.Ultimo.anterior=aux
        self.__unirNodos()

    def __unirNodos(self):
        if self.primero != None:
            self.primero.anterior=self.Ultimo
            self.Ultimo.siguiente=self.primero

    def recorrer_inicio_fin(self):
        aux=self.primero
        while aux:
            print(aux.dato)
            aux=aux.siguiente
            if aux==self.primero:
                break
        print self.primero.dato  

    def recorrer_inicio_fin_Horizontal(self):
        aux=self.primero
        user=""
        while aux:
            #print(aux.dato)
            user=user+aux.dato+"->"
            aux=aux.siguiente
            if aux==self.primero:
                break
       # print self.primero.dato 
        print user+self.primero.dato
       

    def recorrer_fin_inicio_horizontal(self):
        aux=self.Ultimo
        user=""
        while aux:
            #print(aux.dato)
            user=user+aux.dato+"->"
            aux=aux.anterior
            if aux==self.Ultimo:
                break
        #print self.Ultimo.dato
        print user+self.Ultimo.dato

    def recorrer_fin_inicio(self):
        aux=self.Ultimo
        while aux:
            print(aux.dato)
            aux=aux.anterior
            if aux==self.Ultimo:
                break
        print self.Ultimo.dato

    def eliminar_inicio(self):
        if self.vacia():
            print "estructura vacia"
        elif self.primero==self.Ultimo:
            self.primero=self.Ultimo=None
        else:
            self.primero=self.primero.siguiente
        self.__unirNodos()

    def eliminar_ultimo(self):
        if self.vacia():
            print "estructura vacia"
        elif self.Ultimo==self.primero:
            self.Ultimo=self.primero=None
        else:
            self.Ultimo=self.Ultimo.anterior
        self.__unirNodos()

    def buscar(self,dato):
        aux =self.primero
        while aux:
            if aux.dato==dato:
                return True
            else:
                aux=aux.siguiente
                if aux==self.primero:
                    return False

class cola:
     def __init__(self):
        self.primero=None
        self.Ultimo=None
        self.nombreCola=None
    
     def vacia(self):
        if self.primero==None:
            return True
        else:
            return False
     def __unirNodos(self):
        if self.primero != None:
            self.primero.anterior=self.Ultimo
            self.Ultimo.siguiente=self.primero

     def encolar(self,dato):

        if self.vacia():
            self.primero = self.Ultimo=Nodo(dato)
        else:
            aux=Nodo(dato)
            aux.siguiente=self.primero
            self.primero.anterior=aux
            self.primero=aux
     
     def desencolar(self):
        if self.vacia():
            print "estructura vacia"
        elif self.Ultimo==self.primero:
            self.Ultimo=self.primero=None
        else:
            self.Ultimo=self.Ultimo.anterior
            #self.Ultimo.siguiente=self.Ultimo
        self.__unirNodos()
            

     def recorrerCola(self):
        aux=self.primero
        while aux:
            print(aux.dato)
            aux=aux.siguiente
            if aux==self.primero:
                break
     def nombre(self,user):
         self.nombreCola=user
         if self.nombreCola==user:
             return True
         else:
             return False
    
        
class pila:
     def __init__(self):
        self.primero=None
        self.Ultimo=None
    
     def vacia(self):
        if self.primero==None:
            return True
        else:
            return False
     def __unirNodos(self):
        if self.primero != None:
            self.primero.anterior=self.Ultimo
            self.Ultimo.siguiente=self.primero
     def push(self,dato):
        if self.vacia():
            self.primero = self.Ultimo=Nodo(dato)
        else:
            aux=Nodo(dato)
            aux.siguiente=self.primero
            self.primero.anterior=aux
            self.primero=aux
     def pop(self):
        if self.vacia():
            print "estructura vacia"
        elif self.primero==self.Ultimo:
            self.primero=self.Ultimo=None
        else:
            self.primero=self.primero.siguiente
     def recorrerPila(self):
        aux=self.primero
        while aux:
            print(aux.dato)
            aux=aux.siguiente
            if aux==None:
                break
 
class NodoMatriz:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None
        self.arriba=None
        self.abajo=None
        self.cabeza=None

class ListaMatriz:
    def __init__(self):
        self.primero=None
     
    def vacia(self):
        if self.primero==None:
            return True
        else:
            return False    
    
    def insertarMatriz(self):
        if self.vacia():
            self.primero =NodoMatriz("0")
        else:
            aux=NodoMatriz("0")
            aux.siguiente=self.primero
            self.primero=aux

    def lista_Matriz(self,ancho):
        self.primero=None
        for x in range(ancho):
            self.insertarMatriz()

   
    def alto_matriz(self,alto,ancho):
        aux=self.lista_Matriz(ancho)
        auxNodo=NodoMatriz("")
        for x in range(alto):
            auxNodo.abajo=aux
            self.recorrerListaMatriz()

    def insertar_dato_matriz(self,x,y):
        aux=self.primero
        for i in range(x):
            aux=aux.siguiente
            for j in range(y):
                aux=aux.abajo
        print aux.dato
    
    

    def recorrerListaMatriz(self):
        aux=self.primero
        orden=""
        while aux:
           # print(aux.dato)
            orden=orden+aux.dato
            aux=aux.siguiente
            if aux==None:
                break
        print orden

class MatrizOrtogonal:
    global altura, anchura
    def __init__(self):
        self.altura=0
        self.anchura=0

    def Matriz_Ortogonal(self,altura,anchura):
        casilla=""
        ultima=ListaMatriz()
        self.altura=altura
        self.anchura=anchura
        if altura>0 and anchura>0:
            ultima=ultima.lista_Matriz(anchura)
            for x in range(altura):
                aux=ListaMatriz()
                aux.lista_Matriz(anchura)
                recorredorAux=NodoMatriz(aux.primero.dato)
                recorredorUltima=NodoMatriz(ultima.primero.dato)
                while recorredorAux!=None and recorredorUltima!=None:
                    recorredorAux.arriba(recorredorUltima)
                    recorredorUltima.abajo(recorredorAux)
                    recorredorUltima=recorredorUltima.siguiente
                    recorredorAux=recorredorAux.siguiente
                ultima=aux

"""user="luis"
auxuser=user
auxuser=cola()
if auxuser.nombre("luis"):
    auxuser.encolar("saber")
    auxuser.encolar("saber2")
    auxuser.recorrerCola()
    print "funciono"
else:
    print "cagada"
   
   
pruebaListaMatriz=ListaMatriz()
ancho=input("ancho de la matriz: ")
#pruebaListaMatriz.lista_Matriz(ancho)
#pruebaListaMatriz.recorrerListaMatriz()
alto=input("alto de la matriz: ")
pruebaListaMatriz.alto_matriz(alto,ancho)
#pruebaListaMatriz.insertar_dato_matriz(2,2)""" 
ojalaY=cola()
ojalaX=cola()
colaFunciones=cola()
listaUser=ListaCircularDoblementeEnlazada()
listaPassword=ListaCircularDoblementeEnlazada()
usuario=inicio()
usuario.menu()


            
