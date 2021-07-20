#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 09:14:06 2021

@author: nat
"""

def grupos (lista_clases):
    resultado = []
    for item in lista_clases:
        if item not in resultado:
            resultado.append(item)
    return resultado
'''
print(grupos (["patines", "raquetas", "patines", "balón", "gafas", "bicicleta", "patines", "raquetas", "gafas", "balón"]))
'''

def faltantes(codes,lista,article):
  
  resultado = []
  for elemento in codes:
    if lista[elemento] == article:
        resultado.append(elemento)
  return resultado


print(faltantes([2,3,6,8],["patines", "raquetas", "patines", "balón", "gafas", "bicicleta", "patines", "raquetas", "gafas", "balón"]
                ,"patines"))


print(faltantes([39, 7, 29, 35, 4, 25, 36, 26, 14, 31, 2, 28, 42, 32, 0, 9, 3, 38, 19, 12, 6]
       , [3, 2, 2, 2, 1, 3, 3, 2, 2, 1, 1, 1, 3, 1, 2, 3, 3, 1, 3, 3, 3, 2, 3, 3, 2, 1, 2, 1, 1, 2, 1, 3, 3, 3, 2, 3, 2, 2, 3, 3, 1, 3, 1]
       ,1))


'''
mi output : [4, 9, 42, 25, 28]
'''
'''
print(faltantes([0,3,0,8],[0,1,0,3,4,5,0,7,8,9], 1)) 
'''
def inexistentes(deporte_extremo, geizer_inc):
    resultado = []
    for i in deporte_extremo:
        if i not in geizer_inc:
            resultado.append(i)
    return resultado
'''
print(inexistentes([3,5,7,10,15,16],[4,10,5,8]))
'''

def trueque(codigosG,codigosDE):

    setG=set(codigosG)
    setDE = set(codigosDE)
    resultado1 =setG.difference(setDE)
    resultado2 =setDE.difference(setG)
    if len(resultado1) > len(resultado2):
        return len(resultado2)
    else:
        return len(resultado1)
   
'''
print(trueque([28, 6, 36, 15, 25, 40, 38, 9, 30, 16, 26, 21, 31, 37, 34, 20, 14, 13],
              [37, 38, 43, 25, 7, 32, 44, 35, 2, 0, 8, 26, 39, 12, 14])
)

'''