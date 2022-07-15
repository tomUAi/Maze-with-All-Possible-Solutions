# Laberintaso
# Grupo 5

import numpy as np


# esta funcion saca la matriz del archivo input.txt
def get_matriz(archivo):
    matrix = np.loadtxt(archivo, dtype=int)
    return matrix


# esta funcion busca el punto de entra y de salida, y lo guarda en la lista incfin
def busqueda(m, incfin):
    incfin.append(([item[0] for item in m]).index(0))
    incfin.append(([item[len(m) - 1] for item in m]).index(0))


# esta funcion Analiza que el punto de partida este correcto
# esta funcion verifica si se puede seguir avanzando o no
# esta funcion genera un recorrido por tdo el laberinto, de manera recursiva.
# esta funcion Alaiza si cada pazo se en cuentra en la salida. Si es asi lo guarda.
# esta funcion Guarda los lugares vistados

def recorrido(row, col,
              m,
              f,
              visitado,
              caminoactual,
              caminosposibles) -> None:
    # Analiza si el punto de partida este correcto
    if row == -1 or row == f or col == -1 or col == f or visitado[row][col] or m[row][col] == 1:
        return

    # Analaiza si cada pazo se en cuentra en la salida. Si es asi lo guarda.
    if row == incfin[1] and col == f - 1:  # salida
        caminosposibles.append(caminoactual.copy())
        return

    # Guarda el paso actual visitado dentro de la matriz.
    visitado[row][col] = True

    # verifica si se puede avanzar para abajo para luego avanzar y guardar su recorrido actual.
    if row + 1 != -1 or row + 1 != f or col != -1 or col != f or visitado[row + 1][col] is False or m[row + 1][
        col] != 1:
        caminoactual.append([row + 1, col])
        recorrido(row + 1, col, m, f, visitado, caminoactual, caminosposibles)
        caminoactual.pop()

    # verifica si se puede avanzar para la izquierda para luego avanzar y guardar su recorrido actual.
    if row != -1 or row != f or col - 1 != -1 or col - 1 != f or visitado[row][col - 1] is False or m[row][
        col - 1] != 1:
        caminoactual.append([row, col - 1])
        recorrido(row, col - 1, m, f, visitado, caminoactual, caminosposibles)
        caminoactual.pop()

    # #verifica si se puede avanzar para la derecha para luego avanzar y guardar su recorrido actual.
    if row != -1 or row != f or col + 1 != -1 or col + 1 != f or visitado[row][col + 1] is False or m[row][
        col + 1] != 1:
        caminoactual.append([row, col + 1])
        recorrido(row, col + 1, m, f, visitado, caminoactual, caminosposibles)
        caminoactual.pop()

    # verifica si se puede avanzar para arriba para luego avanzar y guardar su recorrido actual.
    if row - 1 != -1 or row - 1 != f or col != -1 or col != f or visitado[row - 1][col] is False or m[row - 1][
        col] != 1:
        caminoactual.append([row - 1, col])
        recorrido(row - 1, col, m, f, visitado, caminoactual, caminosposibles)
        caminoactual.pop()

    # Si se llega a este punto, es porque no se pudo seguir avanzando por lo que retrocedio y se marca como no visitado el paso retrocedido.
    visitado[row][col] = False


# funcion para crear el output.txt
def printcamino(m, f):
    # listas para almacenar cordenadas
    caminosposibles = []
    caminoactual = [[incfin[0], 0]]
    # matriz para marcar los puntos actualmente recorridos.
    visitado = [[False for _ in range(f)]
                for _ in range(f)]

    # LLama la funcion para emepzar el recorrido
    recorrido(incfin[0], 0, m, f, visitado, caminoactual, caminosposibles)  # Inicio

    # Imprime las posible soluciones
    print(caminosposibles)
    texto = open("output.txt", "w+")
    texto.write(str(caminosposibles))
    texto.close()


# Ejecutable del Codigo
if __name__ == "__main__":
    matriz = get_matriz('input.txt')
    m = np.matrix(matriz)
    m = m.tolist()
    incfin = []
    busqueda(m, incfin)
    printcamino(m, len(m))
