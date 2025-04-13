import metodo_bisseccao as mb
import numpy as np

valor_inicio = 0.1
valor_final = 1
def funcao_a(x):
    return x**3 + 3*x - 1

def funcao_b(x):
    return x**2 - np.sin(x)

def main(funcao):
    resultado = mb.metodo_bisseccao(funcao,valor_inicio,valor_final)
    if resultado is not None:
        print(f" raiz :{resultado[0]} \n num iteracoes: {resultado[1]}")
        print(f" testa da raiz: {funcao(resultado[0])}")

main(funcao_a)
# intevalo valido para a:
# -1 / 1 , pois o resultado da multiplicaçao entre a f(1)*f(-1) < 0, 
# assim provando que existe uma raiz nesse intervalo pois cruzam o eixo x
main(funcao_b)
# intervalo valido para b:
# 0.1 / 1