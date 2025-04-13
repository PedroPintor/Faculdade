
def metodo_LU(matriz_L, matriz_U):
    n_linhas = len(matriz_U)
    for k in range( 0, n_linhas -2):
        for i in range( k + 1, n_linhas):
            matriz_L[i][k] = matriz_U[i][k] / matriz_U[k][k]
            for j in range( k, n_linhas - 1):
                matriz_U[i][i] = matriz_U[i][j] - (matriz_L[i][j]*matriz_U[k][j])
        
    return matriz_L,matriz_U
