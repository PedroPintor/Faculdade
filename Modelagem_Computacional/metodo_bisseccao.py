
# valores da função dada no exercício
p = 50000
m = 1200
n = 60
# função do exercício
def funcao(i):
   return  ( m* ((1 + i)**n) - 1) / ( i* ((1 + i)**n) )  - p

# método da bisseção
def metodo_bisseccao(inicio_intervalo, fim_intervalo, erro, max_iter):
    
    inicio = funcao(inicio_intervalo)
    fim = funcao(fim_intervalo)

    if inicio * fim > 0:
        print(f"Intervalo inválido: {inicio} e {fim} têm o mesmo sinal.")
        return None
    
    else:
        iterador = 0
        meio_intervalo = (inicio_intervalo + fim_intervalo) / 2
        # abs(): absolute value
        while abs(funcao(meio_intervalo)) > erro and iterador < max_iter:
            if funcao(inicio_intervalo) * funcao(meio_intervalo) < 0:
                fim_intervalo = meio_intervalo
            else:
                inicio_intervalo = meio_intervalo

            meio_intervalo = (inicio_intervalo + fim_intervalo) / 2
            iterador += 1
        
        if iterador >= max_iter:
            print("Número máximo de iterações alcançado.")
        
        return meio_intervalo , iterador

# Executar o método de bisseção
inicio_intervalo = 0.00001
fim_intervalo = 0.5
erro = 0.0000001  # 10e-3
max_iter = 100
resultado = metodo_bisseccao(inicio_intervalo, fim_intervalo, erro, max_iter)
if resultado is not None:
    print(f"O valor aproximado da raiz é: {resultado[0]} \n numero de interacoes {resultado[1]}")
    print(f" teste da raiz: {funcao(resultado[0])}")
