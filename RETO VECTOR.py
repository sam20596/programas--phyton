# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:50:30 2020

@author: Xp
"""


print("MENU VECTOR ")
print("  0. SALIR  ")
print(" 1. VECTOR CARACTER ")
print(" 2. VECTOR NUMERO ")
print("--------------------------------------------------------")
op = int(input("Opcion: "))
while op !=0:
    

    if op == 0:
        print(" ")

    if op == 1:
        auxiliar=str()
        nombre=str()
        vector=[str()for ind0 in range(100)]
        print("ingresa el tamaño del vector")
        tamanovector=int(input())
        for i in range(1,tamanovector+1):
            print("ingrese el nombre del estudiante",i)
            nombre=input()
            vector[i-1]=nombre
            print("el valor en la posicion",i,"es",vector[i-1])
        for j in range(1,tamanovector+1):
            for l in range(1,tamanovector):
                if vector[l-1]>vector[l]:
                    auxiliar=vector[l-1]
                    vector[l-1]=vector[l]
                    vector[l]=auxiliar
        for k in range(1,tamanovector+1):
            print("el vector ordenad en la posicion",k,"es",vector[k-1])
                
        
        
        

    if op == 2:
        print("escoga la forma de ordenar la serie")
        print("0. SALIR")
        print("3. ASCENDENTE ")
        print("4. DESCENDENTE")
        opc = int(input("Opcion: "))
        while opc !=0:
           if opc==3:
               from random import randint
               from time import sleep
               auxiliar=int()
               vector =[int()for ind0 in range(100)]
               print("ingrese tamaño del vector")
               tamanovector=int(input())
               for i in range (1,tamanovector +1):
                    vector[i-1]=randint(0,99)
                    print("el valor en la posicion",i,"es",vector[i-1])
                    sleep(1)
               sleep(1)
               for j in range(1,tamanovector+1):
                   for l in range(1,tamanovector):
                       if vector[l+1]>vector[l]:
                            auxiliar=vector[l+1]
                            vector[l+1]=vector[l]
                            vector[l]=auxiliar
               for k in range(1,tamanovector+1): 
                   print("el vector ordenado en la posicion",k,"es",vector[k-1])
                   sleep(1)
                
                    
           if opc==0:
               print(" ")
               
           if opc==4:
               from random import randint
               from time import sleep
               auxiliar=int()
               vector =[int()for ind0 in range(100)]
               print("ingrese tamaño del vector")
               tamanovector=int(input())
               for i in range (1,tamanovector +1):
                   vector[i-1]=randint(0,99)
                   print("el valor en la posicion",i,"es",vector[i-1])
                   sleep(1)
               sleep(1)
               for j in range(1,tamanovector+1):
                   for l in range(1,tamanovector):
                       if vector[l+1]>vector[l]:
                           auxiliar=vector[l+1]
                           vector[l+1]=vector[l]
                           vector[l]=auxiliar
               for k in range(1,tamanovector+1):
                   print("el vector ordenado en la posicion",k,"es",vector[k-1])
                   sleep(1)
                   
                   
        print("escoga la forma de ordenar la serie")
        print("0. SALIR ")
        print("3. ASCENDENTE")
        print(" 4. DESCENDENTE")
        opc = int(input("ESCOJA OTRA OPCION "))          
    

    
        
            

    
        
               
               
        
            
                        
                        
                
                    
                    
                    
            
        
    
            
                
                   
   


    
        
            

           
           
           

    print("MENU ")
    print("0. SALIR ")
    print("1. VECTOR CARACTER ")
    print("2. VECTOR NUMERICO ")
    print("----------------------------------------------------------")
    op = int(input("Escoja otra opcion: "))
