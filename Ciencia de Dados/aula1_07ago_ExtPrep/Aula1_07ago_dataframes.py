# -*- coding: utf-8 -*-
"""
extração e preparação de dados
Aula1 - dataframes
07 ago 25
"""
#%% importando bibliotecas
import pandas as pd # manipulação de dataframes
#%%
turma1=pd.DataFrame(columns=['nome','idade','local_nascimento'])

#%%
len(turma1)

#%% Inserindo observações (linhas) no dataframe
pessoa=[]
pessoa.append('Rafael')
pessoa.append(26)
pessoa.append('SP')
indice=len(turma1)
turma1.loc[indice]=pessoa
#%%
pessoa=[]
pessoa.append('Gabriel')
pessoa.append(22)
pessoa.append('SP')
indice=len(turma1)
turma1.loc[indice]=pessoa
#%%
pessoa=[]
pessoa.append('Caio')
pessoa.append(32)
pessoa.append('MG')
indice=len(turma1)
turma1.loc[indice]=pessoa
#%%
pessoa=[]
pessoa.append('Beatriz')
pessoa.append(20)
pessoa.append('RJ')
indice=len(turma1)
turma1.loc[indice]=pessoa
#%% exibir a estrutura do dataframe
turma1.info()
#%%
turma1.shape[0] #linhas
turma1.shape[1] #colunas
#%%
#%% entrada de dados de 3 alunos (via teclado)
# adicionando-os no dataframe
for i in range(3):
    print("--------------------------")
    nome=input("Digite seu nome: ")
    idade=int(input("Digite sua idade: "))
    local_nascimento=input("Digite o local de nascimento: ")
    pessoa=[]
    pessoa.append(nome)
    pessoa.append(idade)
    pessoa.append(local_nascimento)
    indice=len(turma1)
    turma1.loc[indice]=pessoa
print(turma1)

#%%
#outra forma de criar um dataframe - dicionarios
#%%
# Primeira parte do dataframe
novos = {
    'nome': ['João Paulo', 'Maria José', 'Antonio', 'Paula'],
    'idade': [35, 40, 54, 39],
    'local_nascimento': ['SP', 'RJ', 'RJ', 'SP'],
}
turma2 = pd.DataFrame(novos)
#%% Novas linhas a serem inseridas
novos = {
    'nome': ['Beatriz', 'Giovanni','Antonio' ],
    'idade': [31, 27,54],
    'local_nascimento': ['SP', 'RJ', 'RJ'],
}
novos_df = pd.DataFrame(novos)
#%%
# Junta os dois dataframes
turma2 = pd.concat([turma2, novos_df], ignore_index=True)

# Exibe o resultado
print(turma2)

#%% gravar os dataframes em csv
turma1.to_csv("turma1.csv")
turma2.to_csv("turma2.csv")
### caso nao queria salvar junto com o index
# turma1.to_cvs("turma1.csv", index=False)

#%%
turma1.to_excel("turma1_excel.xlsx")
#%%
turma2.info()

