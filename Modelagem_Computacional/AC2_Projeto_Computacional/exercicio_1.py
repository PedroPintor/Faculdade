# AC2_Projeto_Computacional/

# Exercicio
# 1. Utilize o metodo da bissecao
# 2. Utileze o metodo de Newton

#  Tabela de dados 
# Estacao   D       S       E       Q
# (A)       20.0    0.0001  0.030   133.0
# (B)       21.5    0.0001  0.030   122.3

# Descricao 
# Q : é o fluxo em m3/seg;
# E : é o coeficiente de atrito determinado experimentalmente, cujo valor tipico varia entre 0.025 e 0.035 para a maioria dos canais e rios;
# A : é a area da seccao transversal do canal;
# R : é o raio hidraulico, definido como a razao entre a area A e o perımetro 2C + D;
# α : é a inclinacao do canal, com S = sin α.

# Funcao 
# [ (1.49/E)³ * D^5*S^(3/2) ] * y^5 - 4Q^3*y^2 - 4*Q^3*D*y - Q^3*D^2 = 0
# onde:
# y = profundidade do canal
# D = largura do canal (m) 
# S = inclinacao do canal
# E = coeficiente de atrito
# Q = vazão (m³/s)

from Metodos import metodo_bissecao as bs, metodo_newton_rasthon as nw
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#funcao 
def funcao(D, S, E, Q, y):
    return ((1.49/E)**3) * (D**5) * (S**(3/2)) * (y**5) - 4*(Q**3)*y*(y + D) - (Q**3)*(D**2)

def derivada_funcao(D, S, E, Q, y):
    return 5*((1.49/E)**3)*(D**5)*(S**(3/2))*(y**4) - 8*(Q**3)*y - 4*(Q**3)*D

def pegar_valores(Estacao):
    print(f' Valores da Estacao {Estacao}')
    D = bs.pegar_numero(" Valor D: ")
    S = bs.pegar_numero(" Valor S: ")
    E = bs.pegar_numero(" Valor E: ")
    Q = bs.pegar_numero(" Valor Q: ")
    
    return D, S, E, Q

def bissecao():
    print('-'*20 + ' METODO DE BISSECAO' + '-'*20)

    print('\n' + '='*50)
    print(' ESTACAO A ')
    print('='*50)

    aD, aS, aE, aQ = pegar_valores('A')
    # necessario para usar os metodos bs
    def funcao_auxiliar_a(y):
        return funcao(aD,aS,aE,aQ, y)
    # encontrar o intervalo valido
    intervalo = bs.encontrar_intervalo(funcao_auxiliar_a)
    inicio = intervalo[0]
    final = intervalo[1]
    # aplicar o metodo
    raiz_a, iteracoes_a = bs.metodo_bissecao(funcao_auxiliar_a,inicio,final)
    
    print('\nResultados Estação A:')
    print(f'Profundidade (y): {raiz_a:.6f} metros')
    print(f'Número de iterações: {iteracoes_a}')
    print(f'Teste do valor da Raiz: {funcao_auxiliar_a(raiz_a):.10f}')

    print('\n' + '='*50)
    print(' ESTACAO B ')
    print('='*50)
    bD, bS, bE, bQ = pegar_valores('B')
    
    def funcao_auxiliar_b(y):
        return funcao(bD,bS,bE,bQ, y)
    # encontrar o intervalor
    intervalo_b = bs.encontrar_intervalo(funcao_auxiliar_b)
    inicio_b = intervalo_b[0]
    final_b = intervalo_b[1]
    raiz_b, iteracoes_b = bs.metodo_bissecao(funcao_auxiliar_b,inicio_b,final_b)

    print('\nResultados Estação B:')
    print(f'Profundidade (y): {raiz_b:.6f} metros')
    print(f'Número de iterações: {iteracoes_b}')
    print(f'Teste do valor da Raiz: {funcao_auxiliar_b(raiz_b):.10f}')
    print('\n' + '='*50)
    print('Comparação entre as estações:')
    print(f'Diferença de profundidade: {abs(raiz_a - raiz_b):.6f} metros')
    print(f'Profundidade A (y): {raiz_a:.6f} metros')
    print(f'Profundidade B (y): {raiz_b:.6f} metros')
    print('='*50 + '\n')

    return [raiz_a, iteracoes_a], [raiz_b, iteracoes_b]

def newton():
    print('-'*20 + ' METODO DE NEWTON' + '-'*20)

    print('\n' + '='*50)
    print(' ESTACAO A ')
    print('='*50)

    aD, aS, aE, aQ = pegar_valores('A')
    # necessario para usar os metodos nw 
    def funcao_auxiliar_a(y):
        return funcao(aD,aS,aE,aQ, y)
    def derivada_auxiliar_a(y):
        return derivada_funcao(aD,aS,aE,aQ, y)
    chute_inicial = float(input(' Digite um chute inicial: '))
    # aplicar o metodo
    raiz_a, iteracoes_a = nw.metodo_newton(chute_inicial, funcao_auxiliar_a, derivada_auxiliar_a)
    print('\nResultados Estação A:')
    print(f'Profundidade (y): {raiz_a:.6f} metros')
    print(f'Número de iterações: {iteracoes_a}')
    print(f'Teste do valor da Raiz: {funcao_auxiliar_a(raiz_a):.10f}')
    
    print('\n' + '='*50)
    print(' ESTACAO B ')
    print('='*50)
    bD, bS, bE, bQ = pegar_valores('B')
    
    def funcao_auxiliar_b(y):
        return funcao(bD,bS,bE,bQ, y)
    def derivada_auxiliar_b(y):
        return derivada_funcao(bD,bS,bE,bQ, y)
    chute_inicial = float(input(' Digite um chute inicial: '))
    # aplicar o metodo
    raiz_b, iteracoes_b = nw.metodo_newton(chute_inicial, funcao_auxiliar_b, derivada_auxiliar_b)
    
    print('\nResultados Estação B:')
    print(f'Profundidade (y): {raiz_b:.6f} metros')
    print(f'Número de iterações: {iteracoes_b}')
    print(f'Teste do valor da Raiz: {funcao_auxiliar_b(raiz_b):.10f}')
    
    print('\n' + '='*50)
    print('Comparação entre as estações:')
    print(f'Diferença de profundidade: {abs(raiz_a - raiz_b):.6f} metros')
    print(f'Profundidade A (y): {raiz_a:.6f} metros')
    print(f'Profundidade B (y): {raiz_b:.6f} metros')
    print('='*50 + '\n')

    return [raiz_a, iteracoes_a], [raiz_b, iteracoes_b]

def main():
    
    [raiz_a_bis, iter_a_bis], [raiz_b_bis, iter_b_bis] = bissecao()
    [raiz_a_new, iter_a_new], [raiz_b_new, iter_b_new] = newton()

    dados = {
        'Método': ['Bissecção', 'Bissecção', 'Newton', 'Newton'],
        'Estação': ['A', 'B', 'A', 'B'],
        'Profundidade (m)': [raiz_a_bis, raiz_b_bis, raiz_a_new, raiz_b_new],
        'Iterações': [iter_a_bis, iter_b_bis, iter_a_new, iter_b_new]
    }
    
    df = pd.DataFrame(dados)
    
    # criar area para o plot com o matplotlib
    fig, (grafico_1, grafico_2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # grafico de barras com o seaborn
    sns.barplot(data=df, 
                x='Estação', 
                y='Profundidade (m)', 
                hue='Método', 
                ax=grafico_1)
    grafico_1.set_title('Comparação de Profundidade')
    
    sns.barplot(data=df, 
                x='Estação', 
                y='Iterações', 
                hue='Método', 
                ax=grafico_2)
    grafico_2.set_title('Comparação de Iterações')
    
    # ajustar o tamanho da figura 
    plt.tight_layout()
    # mostrar os graficos 
    plt.show()
    
    # print da tabela 
    print("\nTabela Comparativa:")
    print(df.to_string(index=False))

main()