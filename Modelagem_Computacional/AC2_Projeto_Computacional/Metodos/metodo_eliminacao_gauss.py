

def eliminacao_gauss(matriz, igualdade):
    # iniciar variavel com o tamanho da altura da matriz
    n = len(igualdade)
    # n - 1: para iterar uma linha da matriz a menos
    for k in range(n-1):
        for i in range(k+1,n):
            m = -matriz[i][k]/matriz[k][k]
            igualdade[i] = igualdade[i] + m*igualdade[k]
            for j in range(k,n):
                matriz[i][j] = matriz[i][j] + m*matriz[k][j]
    return matriz, igualdade

matriz = [
        [2 , 1, -1], 
        [1, -3, 2],
        [3, 2, -1]
    ]
b =     [ 1, 4, 2]

matriz_resposta = eliminacao_gauss(matriz, b)
print(f" {matriz_resposta[0][0]} \n {matriz_resposta[0][1]} \n {matriz_resposta[0][2]} ")
print(f" \n {matriz_resposta[1]} ")