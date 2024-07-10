from typing import List
from matrizRala import *

def GaussJordan(A, b):
    # Hallar solucion x para el sistema Ax = b
    # Devolver error si el sistema no tiene solucion o tiene infinitas soluciones, con el mensaje apropiado
    # Chequear que el tamaño de b sea correcto. Chequear al inicio si b tiene alguna posicion que no es 0 y en A esa fila es todo 0's

    cantPivotes = min(A.shape[0], A.shape[1])
    matriz_temp_gj = A
    pos_pivotes_usados: List[int] = []
    pivote = None
    pos_columna_pivote = None

    for pos_fila_pivotes in range(cantPivotes):
        print(matriz_temp_gj)
        if pos_fila_pivotes not in matriz_temp_gj.filas.keys():
            if b[pos_fila_pivotes, 0] != 0:
                raise ArithmeticError("El sistema no tiene solucion")
        else:

            nodo = matriz_temp_gj.filas[pos_fila_pivotes].raiz
            encontrado = False
            while nodo is not None and not encontrado:
                if nodo.valor[1] != 0 and nodo.valor[0] not in pos_pivotes_usados:
                    encontrado = True
                    pos_pivotes_usados.append(nodo.valor[0])
                    pos_columna_pivote = nodo.valor[0]
                    pivote = A[pos_fila_pivotes, pos_columna_pivote]

                nodo = nodo.siguiente

            print("pivote", pivote)

            if pivote != 1:
                nodo = matriz_temp_gj.filas[pos_fila_pivotes].raiz
                while nodo is not None:
                    print("pos", nodo.valor)
                    matriz_temp_gj[pos_fila_pivotes, nodo.valor[0]] /= pivote
                    nodo = nodo.siguiente

                b[pos_fila_pivotes, 0] /= pivote

            print("primera", repr(matriz_temp_gj))
            filas_a_restar = list(matriz_temp_gj.filas.keys()).copy()
            filas_a_restar.remove(pos_fila_pivotes)
            for fila in filas_a_restar:
                multiplicador: float = matriz_temp_gj[fila, pos_columna_pivote]
                for columna in range(matriz_temp_gj.shape[1]):
                    if matriz_temp_gj[pos_fila_pivotes, columna] != 0:
                        matriz_temp_gj[fila, columna] = (
                            matriz_temp_gj[fila, columna]
                            - multiplicador * matriz_temp_gj[pos_fila_pivotes, columna]
                        )

                b[fila, 0] = b[fila, 0] - b[pos_fila_pivotes, 0] * multiplicador

        # primera_vez = False

    res = MatrizRala(A.shape[1], 1)

    print(repr(matriz_temp_gj), repr(b))

    filas = set([x for x in range(A.shape[0])])
    filas_restantes = filas - set(matriz_temp_gj.filas.keys())
    print(filas, filas_restantes)
    for nro_fila in filas_restantes:
        if b[nro_fila, 0] != 0:
            raise ArithmeticError("El sistema no tiene solucion")

        raise ArithmeticError("El sistema tiene infinitas soluciones")

    for nro_fila, fila in matriz_temp_gj.filas.items():
        for nodo in fila:
            # print(nodo)
            if nodo[1] != 0:
                res[nodo[0], 0] = b[nro_fila, 0]

    return res

def reduce_matrix(m):
    """
    Funcion que implementa el algoritmo de Gauss-Jordan para la reduccion de una matriz
    """
    matrix = m.astype(float).copy()
    pivot_col = 0
    n_rows, n_cols = matrix.shape
    for row in range(n_rows):

        if pivot_col >= n_cols:
            return matrix.round(2)

        row_pivot = row
        while abs(matrix[row_pivot][pivot_col]) < 1e-5:
            row_pivot += 1
            if row_pivot == n_rows:
                row_pivot = row
                pivot_col += 1
                if n_cols == pivot_col:
                    return matrix.round(2)
            else:
                matrix[[row_pivot,row]] = matrix[[row, row_pivot]]

        pivot = matrix[row][pivot_col]
        matrix[row] = [mrx / float(pivot) for mrx in matrix[row]]

        for other_row in range(n_rows):
            if other_row != row:
                below_pivot = matrix[other_row][pivot_col]
                matrix[other_row] = [iv - below_pivot * rv for rv, iv in zip(matrix[row], matrix[other_row])]
        pivot_col += 1
    return matrix.round(2)