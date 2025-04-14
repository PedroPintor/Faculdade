import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Metodos import metodo_gauss_seidel as mdgs

# padrao da matriz do exercicio
def gerar_matriz_padrao(n_linhas, n_colunas):
    A = np.zeros((n_linhas, n_colunas), dtype=int)
    tamanho_ciclo = int(np.sqrt(n_linhas))
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
    # plot
    plt.contourf(matriz,cmap='hot')
    plt.colorbar(label='Temperatura (°C)')
    plt.xlabel('Colunas')
    plt.ylabel('Linhas')
    plt.title('Distribuição de Temperatura')
    plt.show()

def montar_matriz_b(tamanho):
    b = []
    tamanho_ciclo = int(np.sqrt(tamanho))
    # valores_inicio
    b.append(60)
    for i in range(1, tamanho_ciclo - 1):
        b.append(40)
    b.append(60)
    # valores_meio
    for k in range(1, tamanho_ciclo - 1):
        b.append(20)
        for j in range(1, tamanho_ciclo - 1):
            b.append(0)
        b.append(20)
    # valores_fim
    b.append(30)
    for n in range(1, tamanho_ciclo - 1):
        b.append(10)
    b.append(30)
    
    return b

def main():
    # Matriz A
    A = gerar_matriz_padrao(16,16)
    x = np.zeros(16)
    b = montar_matriz_b(16)
    resultado, i = mdgs.metodo_gauss_seidel(A,x,b)
    reshape_resultado = resultado.reshape(4,4)
    dist_temperatura_matplot(reshape_resultado)
    dist_temperatura_seaboarn(reshape_resultado)

    # Matriz B
    B = gerar_matriz_padrao(49,49)
    y = np.zeros(49)
    d = montar_matriz_b(49)
    result, j = mdgs.metodo_gauss_seidel(B,y,d)
    reshape_result = result.reshape(7,7)
    dist_temperatura_matplot(reshape_result)
    dist_temperatura_seaboarn(reshape_result)



main()