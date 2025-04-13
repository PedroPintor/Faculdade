import numpy as np
from Metodos import metodo_gauss_seidel as mdgs

def gerar_matriz_padrao(n_linhas, n_colunas):
    tamanho = n_linhas * n_colunas
    A = np.zeros((tamanho, tamanho), dtype=int)

    for i in range(tamanho):
        A[i][i] = 4

        # Vizinho à esquerda (mesma linha)
        if i % n_colunas != 0:
            A[i][i - 1] = -1
        
        # Vizinho à direita (mesma linha)
        if (i + 1) % n_colunas != 0:
            A[i][i + 1] = -1

        # Vizinho acima (mesma coluna, linha anterior)
        if i - n_colunas >= 0:
            A[i][i - n_colunas] = -1

        if i + n_colunas < tamanho:
        # Vizinho abaixo (mesma coluna, linha seguinte)
            A[i][i + n_colunas] = -1

    return A

# Matriz A
A = gerar_matriz_padrao(16,16)
x = [0,0,0]
b = []
resultado, i = mdgs.metodo_gauss_seidel(A,)