import numpy as np

def funcao(x):
    return np.cos( np.pi*(x + 1)/ 8) + 0.148*x - 0.9062

def funcao_b(x):
    return 4*x - np.e**x

def main(funcao,inicio,fim,erro,max_iter):
    # verificar intervalor
    a = funcao(inicio)
    b = funcao(fim)
    if a * b < 0:
        print(f'intervalo valido \n \
                inicio:{inicio} fim: {fim} \n \
                f(inicio): {a} f(fim): {b} \n ')
    else: 
        print('intervalo invalido \n \
                inicio:{inicio} fim: {fim} \n \
                f(a): {a} f(b): {b} \n ')
        return None

    # aplicar o metodo
    meio = ( inicio + fim ) / 2
    iterador = 0
    while abs(funcao(meio)) < erro and iterador < max_iter:
        # achar o novo meio
        if funcao(a)*funcao(meio) < 0:
            b = meio
        else: 
            a = meio
        meio = (a + b) / 2
        iterador += 1
    return meio , iterador

inicio = 2
fim = 3
resultado = main( funcao_b, inicio , fim, 0.001, 200)
print(f" raiz: {resultado[0]}")