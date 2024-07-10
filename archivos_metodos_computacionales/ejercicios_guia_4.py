import random
from typing import List, Dict, Tuple
import numpy as np
from algoritmo_gauss_jordan import *
from matrizRala import *
import scipy as sp
from scipy import linalg
import time


#Ejercicio 9

print("------------------------------------", "\n", "Ejercicio 9", "\n")


A = np.array(
    [
        [3, -5, -9],
        [8, 7, -6],
        [-5, -8, 3],
        [2, -2, -9]
    ]
)

y = np.array(
    [
        [-4],
        [-8],
        [6],
        [-5]
    ]
)

A_convertida_a_rala = convertir_a_rala(A)
y_convertida_a_rala = convertir_a_rala(y)


try:
    res = GaussJordan(A_convertida_a_rala, y_convertida_a_rala)
    print(f"y pertenece al subespacio generado por las columnas de A, con solucion: {res}")

except ArithmeticError as e:
    if e == "El sistema no tiene solucion":
        print("y no pertenece al sub espacio generado por las columnas de A")
    else:
        print("y pertenece al subespacio generado por las columnas de A")

print(reduce_matrix(A))

#Ejercicio 10

print("------------------------------------", "\n", "Ejercicio 10", "\n")

B = np.matrix(
    [
        [3, -5, -9],
        [8, 7, -6],
        [-5, -8, 3],
        [2, -2, -9]
    ]
)

w = np.array(
    [
        [1],
        [3],
        [-4]
    ]
)

resultado = B * w
print(resultado, "\n")

if resultado == np.zeros((len(w), 1)):
    print(f"{w} pertenece al espacio nulo de B")
else:
    print(f"{w} no pertenece al espacio nulo de B")

#Ejercicio 18

A = np.zeros((8, 8))

for i in range(0, 8):
    A[i, i] = 4

for i in range(0, 7):
    if i%2 == 1:
        A[i+1, i] = 0
        A[i, i+1] = 0
    else:
        A[i+1, i] = -1
        A[i, i+1] = -1

for i in range(0, 6):
    A[i+2, i] = -1
    A[i, i+2] = -1

print(A)

P, L, U = sp.linalg.lu(A)
print(f"P: {P}, L: {L}, U: {U}")

print(np.diag(L@U, k = -1), np.diag(A, k = -1))

for i in range(len(np.diag(A, k = -1))):
    print(A[i+1, i] == (L@U)[i+1, i])

resta = A - L@U

print(resta, resta == np.zeros((8,8)))

print(sp.linalg.inv(A)-A)

# Quiero resolver el sistema: Ly = b ^ Ux = y

b = np.array([5, 15, 0, 10, 0, 10, 20, 30])

tiempo_inicial = time.time()

primera_solucion = sp.linalg.solve(L, b)

segunda_solucion = sp.linalg.solve(U, primera_solucion)

tiempo_final = time.time()
print(f"Solucion: {segunda_solucion}. Con la factorizacio tardo: {tiempo_final-tiempo_inicial}")

tiempo_inicial_2 = time.time()

solucion_con_A = sp.linalg.solve(A, b)

tiempo_final_2 = time.time()

print(f"Solucion: {solucion_con_A}. Sin la factorizacion tardo: {tiempo_final_2-tiempo_inicial_2}")


#Ejercicio 19

A = np.zeros((4, 4))

C = 1

for i in range(0, 4):
    A[i, i] = 1 + 2*C

for i in range(0, 3):
    if i%2 == 1:
        A[i+1, i] = -C
        A[i, i+1] = -C
    else:
        A[i+1, i] = -C
        A[i, i+1] = -C

print(A)

P, L, U = sp.linalg.lu(A)
print(f"P: {P}, \n L: {L}, \n U: {U}")

t_cero = np.array([
    10, 15, 15, 10
])

# Quiero resolver el sistema de la forma A*t_k+1 = t_k. Que es equivalente a L*y = t_k ^ U*t_k+1 = y

t_k = t_cero
for i in range(1, 5):
    primera_solucion = sp.linalg.solve(L, t_k)
    t_k_mas_uno = sp.linalg.solve(U, primera_solucion)
    t_k = t_k_mas_uno
    print(f"el valor de t_{i} es {t_k_mas_uno}")