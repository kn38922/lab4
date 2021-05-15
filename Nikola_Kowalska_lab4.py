# -*- coding: utf-8 -*-
"""
Created on Sat May 15 09:05:58 2021

@author: Nikola 
"""

def sortowanie(lista):
    n=len(lista)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if lista[i]>lista[j]:
                pom=lista[i]
                lista[i]=lista[j]
                lista[j]=pom
                
        print(lista)
                
lista=[7,9,2,1,4,0,32]


sortowanie(lista)


