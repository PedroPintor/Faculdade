# -*- coding: utf-8 -*-
"""

extração e preparação de dados
Aula1 - dataframes
07 ago 25

"""

"""
    Declarando Novos valores
    Deletando Variaveis desnecessarias
    Trabalhando com o MERGE
    
    
"""

#%% importando bibliotecas
import pandas as pd
#%% exemplo 1 - iniciando valores 
alunos = {    
  "aluno": ["Antonio", "João", "Maria","Ana Paula","Pedro", "Joana","Gabriel", "Raquel","Carlos"],
  "idade": [20, 22, 21,19,22,20,19,21,16],
  "RA":['1A','1B','1C','1D','1E','1F','1G','1H','1J']
}
calculo = {
  "RA":['1A','1B','1C','1D']
}
estatistica = {
  "RA":['1C','1D','1E','1F','1J']
}

#%% criando os DataFrame
dfAlunos = pd.DataFrame(alunos)
dfCalulo = pd.DataFrame(calculo)
dfEstatistica = pd.DataFrame(estatistica)

#%% remover variaveis desnecessarias
del alunos
del calculo
del estatistica
#%% MERGE - juntar um DataFrame
"""
    how = 'inner': intercecao
    how = 'outer': uniao
    how = 'left' : esquerda
    how = 'right': direira
    how = 'cross': cruzamento      
"""
#%% Criar tabela com todos os alunos de CALCULO - MERGE INNER
turma_calculo = pd.merge(dfAlunos, dfCalulo,
                             left_on='RA',
                             right_on='RA',
                             how='inner')
#%% Outra forma de MERGE
# para casos particulares onde ja existem uma coluna igual e a tabela do merge
# so tem uma coluna
turma_calculo1 = dfAlunos.merge(dfCalulo, how='inner')
#%%
del turma_calculo1
#%% Criar tabela com todos os alunos de ESTATISTICA - MERGE INNER
turma_estatistica = pd.merge(dfAlunos, dfEstatistica,
                             left_on='RA',
                             right_on='RA',
                             how='inner')
#%% Criar tabela com os alunos de Calculo E Estatistica - MERGE 
calculo_e_estatistica = pd.merge(turma_calculo, turma_estatistica,
                                     left_on='RA',
                                     right_on='RA',
                                     how='inner')
"""
    quando usamos o comando 'left_on' ou 'rigth_on' faz ter um comportamento 
    diferente
    
    O comando PEGA TODAS as COLUNAS comum entre as tabelas
"""

#%%
calculo_e_estatistica_2 = pd.merge(turma_calculo, turma_estatistica,
                                   how='inner')
"""
    quando nao usamos o comando, pegamos a linha inteira que se repete,  
    SEM pegar valores de TODAS as COLUNAS
"""
#%% Criar tabela com os alunos de Calculo OU Estatistica - MERGE 
calculo_ou_estatistica = pd.merge(turma_calculo, turma_estatistica,
                                     how='outer')

#%% Criar tabela com os alunos de Calculo - MERGE 
calc = pd.merge(turma_calculo, turma_estatistica,
                how='left')
#%% Criar tabela com os alunos de Estatistica - MERGE 
estat = pd.merge(turma_estatistica, turma_calculo,
                 how='left')
#%% Criar tabela com os alunos que nao faz nenhuma Aula - MERGE
nenhuma_aula = pd.concat([dfAlunos, calculo_ou_estatistica]).drop_duplicates(keep=False).reset_index(drop=True)
"""
    para pegar os valores fora do conjunto, nos pegamos todos os valores
    e aqueles valores que eu sei que estao em PELO MENOS um conjnto
    nos temos que tirar. Pois, o conjunto/DataFrame que contem os valores
    que estao em um OU outro conjunto vai estar duplicado os valores.
"""

#%%
# tabela de preços produtos
produtos = {
    'codigo': ['1a', '2b', '3c', '4d','5a','6b','7c'],
    'Produto': ['macarrão', 'arroz', 'feijão', 'óleo','sal','café','açucar'],
    'Preco': [6, 25.5, 7.5, 9,2,22,5.5]
}

dfProdutos = pd.DataFrame(produtos)
#%%
# Criando um dicionário com detalhes das vendas
vendas = {
    'codigo':[10,11,12,13,14,15,16,17,18],
    'cliente':['A','B','C','D','E','F','G','F','G'],
    'codigo_produto': ['1a', '2b', '2b','3c', '3c','4d','5a','6b','6b'],
    'Quantidade': [2, 5, 4, 6, 7, 3, 1,4,8]
}
dfVendas = pd.DataFrame(vendas)
#%%
del produtos
del vendas
#%% Criar tabela com a venda total 
# vai conter: tudo de venda, preço
totalVendas = pd.merge(dfProdutos, dfVendas,
                       left_on='codigo',
                       right_on='codigo_produto',
                       how='inner')
#%%
