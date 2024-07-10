import random
from typing import List, Dict, Tuple
import numpy as np

#Ejercicio 1

# n = tamaño de la matriz. La matriz es cuadrada. Esto aplica para todas las funciones

def symmetric_matrix(n: int) -> List[List[int]]:
    value_i_diagonal: int = random.randint(-100, 100)
    res: List[List[int]] = []
    dict_of_values: Dict[Tuple[int, int], int] = dict()
    for i in range(0, n):
        res.append([])
        for j in range(0, n):
            if i == j:
                res[i].append(value_i_diagonal)
            elif j > i:
                value: int = random.randint(-100, 100)
                dict_of_values[(j,i)] = value
                res[i].append(value)
            else:
                res[i].append(None)
    
    for i in range(0, n):
        for j in range(0, n):
            if res[i][j] == None:
                res[i][j] = dict_of_values[(i,j)]

    return res

def sum_equal_one_between_symmetric_positions(n: int) -> List[List[int]]:
    res: List[List[int]] = []
    dict_of_values: Dict[Tuple[int, int], int] = dict()
    for i in range(0, n):
        res.append([])
        for j in range(0, n):
            if i == j:
                res[i].append(1)
            elif j > i:
                value: int = random.randint(-99, 100)
                dict_of_values[(j,i)] = value
                res[i].append(value)
            else:
                res[i].append(None)
    
    for i in range(0, n):
        for j in range(0, n):
            if res[i][j] == None:
                res[i][j] = 1 - dict_of_values[(i,j)]
    return res

def anisymmetric_matrix(n: int) -> List[List[int]]:
    
    value_i_diagonal: int = random.randint(-100, 100)
    res: List[List[int]] = []
    dict_of_values: Dict[Tuple[int, int], int] = dict()
    for i in range(0, n):
        res.append([])
        for j in range(0, n):
            if i == j:
                res[i].append(value_i_diagonal)
            elif j > i:
                value: int = random.randint(-100, 100)
                dict_of_values[(j,i)] = value
                res[i].append(value)
            else:
                res[i].append(None)
    
    for i in range(0, n):
        for j in range(0, n):
            if res[i][j] == None:
                res[i][j] = -dict_of_values[(i,j)]
    
    return res

def null_trace_matrix(n: int) -> List[List[int]]:
    res: List[List[int]] = []
    bottom_limit: int = -100
    top_limit: int = 100
    sum_of_diagonal: int = 0
    for i in range(0, n):
        res.append([])
        for j in range(0, n):
            value: int = None
            if i == j:
                if sum_of_diagonal > 0:
                    value = random.randint(bottom_limit, top_limit-sum_of_diagonal)
                else:
                    value = random.randint(bottom_limit-sum_of_diagonal, top_limit)
                sum_of_diagonal += value
            
            elif i == j and i == n-1:
                value = -sum_of_diagonal
            
            else:
                value = random.randint(-100, 100)
            
            res[i].append(value)
            
    return res

def some_null_row(n: int) -> List[List[int]]:
    res: List[List[int]] = []
    pos_of_null_row: int = random.randint(0, n-1)
    for i in range(0, n):
        res.append([])
        for j in range(0, n):
            value: int = None
            if i == pos_of_null_row:
                value = 0
            else:
                value = random.randint(-100, 100)
            res[i].append(value)
    return res

def upper_triangle_matrix(n: int) -> List[List[int]]:
    res: List[List[int]] = []
    for i in range(0, n):
        for j in range(0,n):
            value: int = None
            if  i < j:
                value = 0
            else:
                value = random.randint(-100, 100)
            res[i].append(value)
    return res

#Ejericcio 11

matriz_aleatoria_A : List[List[int]] = np.random.randint(-100, 100, size=(4,4))
print(matriz_aleatoria_A)
identidad: List[List[int]] = np.identity(4)
producto: List[List[int]] = (matriz_aleatoria_A+identidad) * (matriz_aleatoria_A-identidad)
print(producto)
calculo: List[List[int]] = producto - (matriz_aleatoria_A*matriz_aleatoria_A - identidad)
print(calculo)
print(calculo == np.zeros((4,4)))

matriz_aleatoria_B : List[List[int]] = np.random.randint(-100, 100, size=(4,4))
producto_de_sumas_A_B: List[List[int]] = (matriz_aleatoria_A+matriz_aleatoria_B)*(matriz_aleatoria_A-matriz_aleatoria_B)
resta_de_cuadrados: List[List[int]] = matriz_aleatoria_A*matriz_aleatoria_A - matriz_aleatoria_B*matriz_aleatoria_B

print(producto_de_sumas_A_B == resta_de_cuadrados, "\n")

#Ejercicio 12

ones_in_diagonal_incomplete: List[List[int]] = np.eye(5,5,1)
print(ones_in_diagonal_incomplete, "\n")
for i in range(2,7):
    print(np.linalg.matrix_power(ones_in_diagonal_incomplete, i), "\n")


#Ejercicio 13

matriz: List[List[int]] = [[1/6, 0.5, 1/3,], [0.5, 0.25, 0.25], [1/3, 0.25, 5/12]]

for i in range(2,20):
    print(np.linalg.matrix_power(matriz, i), "\n")

# A^k tiende a [[1/3, 1/3, 1/3], [1/3, 1/3, 1/3],[1/3, 1/3, 1/3]] cuando k tiende a infinito

#Ejercicio 14

matrix_M: List[List[int]] = np.matrix([[1,0,-1,0], [0,1,0,0], [-1,0,1,0], [0,0,0,1]])
matrix2 = np.matrix([[1,1,1,1]])
print("matrix M: ", matrix_M, matrix2*matrix_M, "matrix")

def vector_is_part_of_the_pattern(vector_transposed: np.matrix, pattern_matrix: np.matrix) -> bool:
    print(vector_transposed, type(vector_transposed))
    result: np.matrix = vector_transposed*pattern_matrix
    result2 = result*(np.transpose(vector_transposed))
    #print(result2, type(result2))
    matrix_zeros = np.zeros((1,1))
    #print(matrix_zeros, "AAA")
    print("resultado: ", result2, "cumple: ", result2 == np.zeros((1,1)))
    return result2 == np.zeros((1,1))

#Los vectores son de R^4

def calculate_it_for_every_vector(vector: List[int]) -> None:
    if len(vector) == 4:
        vector_to_matrix: np.matrix = np.matrix([[x for x in vector]])
        vector_is_part_of_the_pattern(vector_to_matrix, matrix_M)
    else:
        list_temp: List[int] = list(vector)
        list_temp.append(1)
        calculate_it_for_every_vector(list_temp)
        list_temp.pop()
        list_temp.append(0)
        calculate_it_for_every_vector(list_temp)

print(calculate_it_for_every_vector([]))