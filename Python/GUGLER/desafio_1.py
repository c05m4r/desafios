#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1) Escriba un programa que permita mostrar en forma inversa la tupla:
"""
nombres = (
    'Marcos', 
    'Alejandro',
    'Julián',
    'Luciano',
    'Néstor',
    'Nicolás',
    'Rubén',
    'Víctor'
)

print(nombres)
print(nombres[::-1])
print("\n\n")

"""
2) Escriba un programa que permita mostrar en forma ordenada la tupla: es la solucion mas vaga que se me ocurrio, pero es la mas eficiente? se podria realizar directamente? sorted(nombres)
"""
nombres = list(nombres)
nombres.sort()
print(tuple(nombres))
print("\n\n")

"""
3) Escriba un programa que permita mostrar sin repeticiones la siguiente lista de números:
"""
numeros = [
    64, 14, 59, 18, 76, 39, 69, 29, 34, 95, 35, 76, 68, 88, 17, 93, 9, 
    67, 53, 65, 25, 86, 81, 27, 81, 98, 99, 99, 94, 49, 10, 48, 37, 24, 
    23, 98, 46, 32, 89, 99, 29, 32, 90, 61, 10, 88, 21, 90, 74, 98, 49, 
    69, 84, 15, 29, 14, 29, 100, 45, 33, 18, 51, 47, 48, 52, 14, 99, 32, 
    18, 58, 38, 86, 97, 72, 43, 14, 97, 86, 13, 18, 77, 89, 73, 72, 58, 
    78, 56, 37, 36, 49, 32, 46, 5, 39, 47, 23, 45, 27, 35, 82, 76, 20, 
    16, 50, 53, 70, 86, 67, 19, 29, 77, 22, 53, 44, 3, 13, 69, 33, 30, 
    67, 71, 53, 21, 58, 45, 53, 19, 29, 65, 76, 55, 29, 21, 22, 19, 81, 
    56, 12, 23, 83, 11, 3, 35, 73, 64, 47, 100, 9, 40, 81, 51, 52, 28, 
    88, 68, 15, 16, 98, 22, 20, 28, 77, 68, 64, 19, 10, 30, 82, 57, 35, 
    22, 62, 85, 30, 0, 3, 10, 83, 2, 27, 61, 86, 88, 9, 69, 89, 76, 76, 
    16, 6, 21, 30, 22, 31, 38, 51, 22, 3, 16, 63, 36, 1, 50, 67, 69, 22, 
    89, 56, 88, 98, 86, 21, 54, 58, 92, 47, 25, 89, 91, 6, 15, 90, 98, 
    61, 60, 71, 99, 85, 34, 100, 97, 71, 92, 17, 10, 39, 23, 52, 27, 15, 
    85, 42, 2, 10, 43, 11, 45, 45, 13, 35, 81, 76, 51, 54, 91, 88, 15, 
    83, 92, 91, 27, 62, 88, 23, 34, 10, 37, 14, 98, 67, 89, 67, 7, 11, 
    18, 99, 77, 19, 86, 27, 15, 41, 50, 100, 56, 65, 76, 58, 71, 74, 62, 
    78, 19, 38, 30, 7, 35, 34, 18, 59, 97, 56, 38, 38, 19, 86, 70, 97, 
    97, 100, 87, 98, 6, 33, 70, 37, 60, 9, 97, 30, 21, 17, 69, 71, 92, 
    92, 71, 76, 40, 79, 41, 95, 32, 2, 15, 76, 53, 18, 70, 91, 81, 53, 
    95, 47, 55, 36, 41, 48, 94, 100, 72, 24, 96, 12, 50, 46, 82, 62, 1, 
    73, 7, 66, 23, 20, 54, 38, 8, 68, 42, 88, 60, 74, 97, 54, 33, 74, 
    31, 20, 84, 24, 3, 85, 72, 7, 51, 42, 91, 85, 60, 75, 86, 42, 78, 3, 
    98, 37, 57, 29, 0, 31, 29, 58, 31, 99, 66, 8, 98, 97, 84, 23, 7, 79,
    22, 98, 63, 49, 98, 7, 47, 67, 30, 78, 64, 38, 67, 57, 44, 28, 86, 
    87, 22, 28, 65, 98, 38, 100, 97, 16, 60, 66, 84, 6, 21, 77, 44, 45, 
    13, 12, 13, 13, 68, 90, 29, 9, 80, 70, 25, 31, 47, 35, 68, 95, 52, 
    76, 92, 6, 55, 47, 59, 4, 46, 4, 83, 38, 21, 49, 73, 17, 43, 7, 17, 
    76, 95, 46, 23, 54, 73, 62, 66, 96, 26, 18, 88, 19, 60, 12, 95, 6, 
    19, 69, 71, 17, 50, 4, 70, 76, 61, 49, 61, 67, 0, 3, 9, 83, 95, 43, 
    53, 39, 70, 3, 67, 1, 47, 13, 59, 91, 94, 63, 97, 30, 87, 67, 50, 91, 
    1, 20, 55, 67, 62, 100, 45, 43, 49, 14, 82, 95, 29, 33, 52, 26, 83, 
    5, 69, 65, 50, 38, 82, 72, 60, 19, 63, 57, 2, 31, 66, 0, 10, 24, 32, 
    57, 32, 75, 26, 24, 38, 27, 65, 88, 25, 58, 52, 54, 50, 79, 27, 100, 
    4, 87, 96, 59, 99, 13, 75, 1, 18, 11, 81, 76, 10, 81, 84, 11, 10, 48,
    56, 77, 49, 31, 60, 83, 74, 93, 41, 33, 98, 79, 29, 6, 1, 9, 90, 53, 
    90, 82, 19, 78, 1, 91, 54, 83, 43, 23, 82, 50, 20, 91, 26, 17, 4, 78, 
    6, 22, 86, 21, 40, 19, 15, 88, 72, 92, 13, 68, 44, 10, 90, 11, 74, 
    74, 9, 3, 28, 68, 1, 48, 2, 83, 25, 62, 80, 4, 34, 26, 80, 78, 10, 
    56, 16, 27, 19, 37, 29, 28, 67, 38, 44, 80, 91, 13, 85, 95, 91, 73, 
    51, 74, 84, 91, 5, 58, 64, 9, 10, 6, 8, 70, 57, 19, 55, 12, 86, 14, 
    23, 33, 60, 37, 36, 74, 66, 81, 68, 98, 54, 13, 70, 24, 3, 100, 89, 
    73, 44, 97, 76, 25, 44, 87, 49, 58, 4, 84, 35, 48, 46, 74, 84, 74, 
    4, 41, 58, 56, 68, 96, 23, 92, 75, 28, 10, 42, 81, 3, 50, 40, 46, 38, 
    1, 67, 29, 7, 100, 16, 16, 88, 85, 43, 93, 44, 7, 71, 49, 28, 1, 72, 
    44, 8, 45, 39, 56, 66, 36, 0, 6, 41, 72, 42, 55, 98, 72, 39, 82, 3,
    69, 2, 5, 60, 28, 80, 46, 22, 71, 26, 57, 74, 48, 39, 9, 66, 3, 54, 
    71, 46, 7, 75, 42, 22, 41, 18, 19, 86, 95, 26, 80, 65, 57, 27, 51, 
    49, 48, 2, 7, 45, 30, 2, 48, 53, 84, 62, 44, 60, 92, 64, 6, 96, 33, 
    65, 31, 2, 22, 100, 62, 99, 32, 38, 28, 69, 19, 5, 69, 4, 9, 6, 24, 
    75, 50, 45, 20, 52, 0, 45, 65, 28, 36, 40, 95, 38, 72, 52, 65, 54, 
    81, 6, 56, 62, 79, 38, 33, 59, 7, 44, 49, 1, 97, 45, 54, 78, 23, 19, 
    52, 4, 42, 36, 44, 21, 68, 19, 33, 28, 4, 29, 97, 25, 62, 45, 64, 37, 
    55, 65, 38, 24, 15, 77, 21, 59, 97, 55, 40, 29, 31, 45, 59, 90, 38, 
    56, 9, 13, 41, 70, 93, 63, 37, 39, 66, 76, 81, 95, 42, 64, 14, 17, 
    64, 9, 90, 4, 5, 92, 76, 47, 81, 44, 40, 83, 0, 65, 79, 54, 22, 57, 
    32, 76, 6, 4, 80, 52, 7, 75, 19, 87, 32, 17, 33, 40, 2, 18, 44, 20, 
    51, 31, 3, 24, 13, 95, 72, 95
]

print(list(frozenset(numeros)))
print("\n\n")

"""
4) Genere una secuencia con los números impares de la lista dada: Utilice los conceptos de comprehensión de listas.
"""
def es_par(numero):
    return numero % 2 == 0
    
numeros = [
    9, 37, 79, 89, 83, 4, 1, 10, 37, 57, 35, 64, 88, 24, 24, 5, 87, 11,
    66, 77, 88, 8, 64, 89, 5, 44, 4, 91, 42, 41, 49, 83, 4, 36, 87, 73,
    91, 18, 61, 37, 69, 84, 6, 92, 31, 66, 100, 95, 76, 95
]
impares = [x for x in numeros if es_par(x) == False]
print(impares)
print("\n\n")

"""
5) Diccionarios - Genere un diccionario relacionando los nombres de la primera lista con losdatos correspondientes de la segunda lista:
"""
nombres = (
    'Marcos',
    'Alejandro',
    'Julián',
    'Luciano',
    'Néstor',
    'Nicolás',
    'Rubén',
    'Víctor'
)

numeros = (
    [9, 37, 79, 89],
    [83, 4, 1, 10],
    [37, 57, 35, 64],
    [88, 24, 24, 5],
    [87, 11, 66, 77],
    [88, 8, 64, 89],
    [5, 44, 4, 91],
    [42, 41, 49, 83],
    [4, 36, 87, 73],
    [91, 18, 61, 37],
    [69, 84, 6, 92],
    [31, 66, 100, 95]
)

mapped = zip(nombres, numeros)
mapped = dict(mapped)
print(mapped)