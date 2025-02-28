

# Variaveis
max_iter = 100
erro = 0.00000001

def funcao(x):
    return x**2 + 3*x + 2
def derivada_funcao(x):
    return 2*x + 3

def metodo_newton(valor_inicial):
    valor = valor_inicial
    iterador = 0 
    while iterador < max_iter:
        f_valor = funcao(valor)
        derf_valor = derivada_funcao(valor)
        
        if abs(derf_valor) < erro:
            print(" derivada proxima de zero ")
            return valor, iterador
        
        temp = valor - ( f_valor / derf_valor)
        valor = temp
        if abs(funcao(valor)) < erro:
            return valor, iterador
        iterador += 1
    print (" nao convergiu")
    return None
    

valor_inicial = 510
resultado = metodo_newton(valor_inicial)
if resultado is not None:
    print ( f" valor da raiz: {resultado[0]} \n numero de iteracoes: {resultado[1]}")
    print(f" teste da raiz :{funcao(resultado[0]):.8f}")
