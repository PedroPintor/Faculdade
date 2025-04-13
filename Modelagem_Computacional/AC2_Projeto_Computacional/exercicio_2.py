import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Metodos import metodo_gauss_seidel as mdgs

# padrao da matriz do exercicio
def gerar_matriz_padrao(n_linhas, n_colunas):
    A = np.zeros((n_linhas, n_colunas), dtype=int)
    tamanho_ciclo = np.sqrt(n_linhas)
    for i in range(n_linhas):
        # diagonal
        A[i][i] = 4        
        # inicio do ciclo
        if i % tamanho_ciclo == 0:
            A[i][i+1] = -1
        # fim do cliclo
        elif i % tamanho_ciclo == tamanho_ciclo - 1:
            A[i][i-1] = -1
        # meio do ciclo
        else:
            A[i][i-1] = -1
            A[i][i+1] = -1
        # 4 casas atras da diagonal
        if i > 3:
            A[i][i-4] = -1
        # 4 casas a frente da diagonal
        if i + 4 < n_linhas:
            A[i][i+4] = -1
        
    return A

def dist_temperatura_seaboarn(matriz):
    df = pd.DataFrame(matriz)
    # plot
    sns.heatmap(df, cmap='hot', annot=True, cbar=True)
    plt.xlabel('Colunas')
    plt.ylabel('Linhas')
    plt.title('Distribuição de Temperatura')
    plt.show()

def dist_temperatura_matplot(matriz):
    array = np.array(matriz)
    # plot
    plt.contourf(array,cmap='hot')
    plt.colorbar(label='Temperatura (°C)')
    plt.xlabel('Colunas')
    plt.ylabel('Linhas')
    plt.title('Distribuição de Temperatura')
    plt.show()

def main():
    # Matriz A
    A = gerar_matriz_padrao(16,16)
    x = np.zeros(16)
    b = [60,40,40,60,20,0,0,20,20,0,0,20,60,40,40,60]
    resultado, i = mdgs.metodo_gauss_seidel(A,x,b)
    reshape_resultado = resultado.reshape(4,4)
    dist_temperatura_matplot(reshape_resultado)
    dist_temperatura_seaboarn(reshape_resultado)

main()