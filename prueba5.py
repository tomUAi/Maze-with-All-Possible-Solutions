import numpy as np

res = []

def get_matriz(archivo):
    matrix = np.loadtxt(archivo, dtype=int)
    return matrix

def busqueda(m, incfin):
    incfin.append(([item[0] for item in m]).index(0))
    incfin.append(([item[len(m) - 1] for item in m]).index(0))

    return False

def findPathHelper(m, n, x, y, dx, dy, path):
    global res

    if (x == incfin[1] and y == n - 1): #salida
        res.append(path.copy())
        return

    #dir = "DLRU"
    for i in range(4):
        row = x + dx[i]
        col = y + dy[i]
        if (row >= 0 and row < n and col >= 0 and col < n and m[row][col] == 0):
            m[row][col] = 2  # used to track visited cells of matrix
            path.append(([row,col]).copy())
            findPathHelper(m, n, row, col, dx, dy, path)
            path.pop()
            m[row][col] = 0  # mark it unvisited yet explorable
def printtext (ans):
    texto = open("output.txt", "w+")
    texto.write(str(ans))
    texto.close()

def findPath(m, n, incfin):
    global res

    res.clear()
    # dx, dy will be used to follow `DLRU` exploring approach
    # which is lexicographically sorted order
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    m[incfin[0]][0] = 2
    findPathHelper(m, n, incfin[0], 0, dx, dy, [[incfin[0], 0]])  #inicio

    return res


# driver code

matriz = get_matriz('input.txt')
m = np.matrix(matriz)
m = m.tolist()
incfin = []
busqueda(m, incfin)
ans = findPath(m, len(m), incfin)
printtext(ans)
print(ans)
