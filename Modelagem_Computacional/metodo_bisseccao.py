import math
import numpy as np

# a: valor inicial do intervalo
# b: valor final do intervalo
# erro: tamanho do erro desejado
# max_iter: máximo de iterações desejado

a = 0.1
b = 1
erro = 0.001  # 10e-3
max_iter = 100

# valores da função dada no exercício
p = 50000
m = 1200
n = 60

# função do exercício
def funcao(i):
   return ( ( m* (1 + i)**n - 1) / ( i* (1 + i)**n ) ) - p

print(funcao(a))
print(funcao(b))

# método da bisseção
def metodo_bisseccao(a, b):
    # Verificar se o intervalo é válido
    if funcao(a) * funcao(b) > 0:
        print("Intervalo inválido: f(a) e f(b) têm o mesmo sinal.")
        return None
    else:
        # Inicializar variáveis
        iterador = 0
        c = (a + b) / 2
        
        # Loop até que o erro seja pequeno o suficiente ou o número máximo de iterações seja alcançado
        while abs(funcao(c)) > erro and iterador < max_iter:
            # Verificar em qual subintervalo a raiz está
            if funcao(a) * funcao(c) < 0:
                b = c
            else:
                a = c
                
            # Recalcular o meio
            c = (a + b) / 2
            iterador += 1
        
        # Verificar se atingiu a precisão ou o número máximo de iterações
        if iterador >= max_iter:
            print("Número máximo de iterações alcançado.")
        
        # Retornar o valor de c, que é a raiz aproximada
        return c

# Executar o método de bisseção
resultado = metodo_bisseccao(a, b)
if resultado is not None:
    print(f"O valor aproximado da raiz é: {resultado}")
