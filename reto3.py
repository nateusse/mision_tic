from collections import Counter
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 22:14:06 2021

@author: nat
"""

entrada = ['']

lista = []
for i in input(" ").split(' '):
    if i == entrada[-1]:
        lista[-1] +=1
    else:
        entrada.append(i)
        lista.append(1)
print(' '.join(map(str,entrada)) ,'\n',' '.join(map(str,lista)))


'''
G G U U U U A A A Z Z Z T T T V V Q Q A A A

'''