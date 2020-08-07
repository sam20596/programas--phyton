# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:51:19 2020

@author: Xp
"""
a=print("ingrese contador inicial")
a=int(input(a))
b=print("ingrese contador final")
b=int(input(b))
if a < b:
    print("1.B/N")
    print("2.Color")
    impresiones=b-a
    
    op=int(input("opcion"))
    if op!=0:
        if op ==1:
            a=int(a)
            b=int(b)
            c=(b-a)*0.06
            print("impresiones:",impresiones)
            print("costo:",c)
        if op==2:
            c=(b-a)*0.12
            print("impresiones:",impresiones)
            print("costo:",c)
else:
    print("error")
    b=print("ingrese contador final")
    b=int(input(b))
    if a < b:
       print("1.B/N")
       print("2.Color")
       impresiones=b-a
       
       op=int(input("opcion"))
       if op!=0:
           if op ==1:
               a=int(a)
               b=int(b)
               c=(b-a)*0.06
               print("impresiones:",impresiones)
               print("costo:",c)
               
           if op==2:
                c=(b-a)*0.12
                print("impresiones:",impresiones)
                print("costo:",c)
                
           
        
        
    
    
        
        

    
    


