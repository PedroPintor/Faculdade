# Metodos/

def metodo_newton(valor_inicial, funcao, derivada_funcao, erro=0.001, max_iter=100):
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
            print ( f" valor da raiz: {valor} \n numero de iteracoes: {iterador}")
            return valor, iterador
        iterador += 1
    print (" nao convergiu")
    return None
    

