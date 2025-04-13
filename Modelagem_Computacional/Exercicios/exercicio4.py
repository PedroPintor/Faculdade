
import numpy as np

def funcao(x):
    return 4*np.cos(x) - np.e**x
def derivada(x):
    return -4*np.sin(x) - np.e**x

def metodo_newton(valor_inicial, funcao, derivada, erro, max_iter=100):
    iterador  = 0
    while  iterador < max_iter:
        f_result = funcao(valor_inicial)
        d_result = derivada(valor_inicial)
        #verificar possivel falha do resultado da derivada
        if abs(d_result) < erro:
            print(f" derivada proxima de zero :{d_result}")
            return valor_inicial
        
        # aplicar metodo
        valor_inicial = valor_inicial - (f_result / d_result)
        iterador += 1
    return valor_inicial, iterador


chute = 0.1
def main():
    resultado = metodo_newton(chute, funcao, derivada, 0.001, 3)  
    if resultado is not None:
        print( f" valor da raiz: {resultado[0]} \n numero de iteracoes: {resultado[1]}")
        print(f" teste da raiz :{funcao(resultado[0]):.8f}")

main()
# resposta exercicio:
# com duas interaçoes nao converte para a raiz, a partir da terceira interaçao ja converte para a raiz
