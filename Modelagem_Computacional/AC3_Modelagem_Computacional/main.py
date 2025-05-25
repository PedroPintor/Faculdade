import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

condicoes_iniciais = [9990, 10, 0] # S[0] I[1] R[2]
dias =  [0, 160]
passos = np.arange(dias[0], dias[1] + 1, 1)
B = 0.25
Y = 0.05
variacoes = [0.1,20] # B V

def dtdy(t, y, Y, B):
    n = 10000
    ds = -B*y[0]*y[1] / n 
    di = B*y[0]*y[1]/n - Y*y[1]
    dr = Y*y[1]
    
    return [ds, di, dr]

def dtdy_varicacoes(t, y, Y, B, variacoes):
    v = 0
    if t >= 30:
        B = variacoes[0]
    if t >= 90:
        v = variacoes[1]

    n = 10000
    ds = -B*y[0]*y[1] / n - v
    di = B*y[0]*y[1]/n - Y*y[1]
    dr = Y*y[1] + v
    
    return [ds, di, dr]
    

## SEM VARIACOES
resultados_1 = solve_ivp(dtdy, 
                       dias, 
                       condicoes_iniciais, 
                       method='RK45', 
                       t_eval=passos, 
                       args=(Y, B))

dados_sem_variacoes = {
    'dia_max_infectados': resultados_1.t[np.argmax(resultados_1.y[1])],
    'max_infectados': max(resultados_1.y[1]),
    'taxa_infeccao': B,
    'taxa_recuperacao': Y,
    'numero_reproducao': B/Y,
    'periodo_infeccioso': 1/Y,
}

## COM VARIACOES
resultados_2 = solve_ivp(dtdy_varicacoes,
                       dias, 
                       condicoes_iniciais, 
                       method='RK45', 
                       t_eval=passos, 
                       args=(Y, B, variacoes))

dados_com_variacoes = {
    'dia_max_infectados': resultados_2.t[np.argmax(resultados_2.y[1])],
    'max_infectados': max(resultados_2.y[1]),
    'taxa_infeccao_inicial': B,
    'taxa_infeccao_final': variacoes[0],
    'taxa_recuperacao': Y,
    'numero_reproducao_inicial': B/Y,
    'numero_reproducao_final': variacoes[0]/Y,
    'periodo_infeccioso': 1/Y,
}

dados_analises = {
    'comparacao_max_infectados': abs(dados_sem_variacoes['max_infectados'] - dados_com_variacoes['max_infectados']),
    'relativo_max_infectados': dados_com_variacoes['max_infectados'] / dados_sem_variacoes['max_infectados'],
    'comparacao_dia_max_infectados': abs(dados_sem_variacoes['dia_max_infectados'] - dados_com_variacoes['dia_max_infectados']),
}

# Exibir resultados
print("Analises:")
for k, v in dados_analises.items():
    print(f"{k}: {v:.2f}")
print("\nDados sem variações:")
for k, v in dados_sem_variacoes.items():
    print(f"{k}: {v:.2f}")
print("\nDados com variações:")
for k, v in dados_com_variacoes.items():
    print(f"{k}: {v:.2f}")

# Criar figura com 2 subplots lado a lado
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico sem variações
axs[0].plot(resultados_1.t, resultados_1.y[0], label='Suscetíveis')
axs[0].plot(resultados_1.t, resultados_1.y[1], label='Infectados')
axs[0].plot(resultados_1.t, resultados_1.y[2], label='Recuperados')
axs[0].set_title('Modelo SIR - Sem Medidas Preventivas') 
axs[0].set_xlabel('Dias')
axs[0].set_ylabel('População')
axs[0].legend()
axs[0].grid(True)


# Gráfico com variações
axs[1].plot(resultados_2.t, resultados_2.y[0], label='Suscetíveis')
axs[1].plot(resultados_2.t, resultados_2.y[1], label='Infectados')
axs[1].plot(resultados_2.t, resultados_2.y[2], label='Recuperados')
axs[1].axvline(x=30, color='red', linestyle='--', label='Medida 1', alpha=0.5)
axs[1].axvline(x=90, color='orange', linestyle='--', label='Mudida 2', alpha=0.5)
axs[1].set_title('Modelo SIR - Com Medidas Preventivas')
axs[1].set_xlabel('Dias')
axs[1].set_ylabel('População')
axs[1].legend()
axs[1].grid(True)


plt.tight_layout()
plt.show()