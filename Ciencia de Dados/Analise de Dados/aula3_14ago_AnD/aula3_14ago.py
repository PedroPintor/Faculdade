# -*- coding: utf-8 -*-
"""

programação para analise de dados
Aula 3 - 
14 ago 25

"""

"""

    Verificar Valores Nulos
    Como tratar valores Nulos
    Adicionando mais valores/colunas com condiçoes 
    Frequencia Absoluta e Relativa entre variaveis qualitativas
    
"""

#%% 
import pandas as pd
#%% lendo o arquivo csv
notas = pd.read_csv('notas_atual.csv')
#%% informaçoes gerais do DataFrame
notas.info()
#%% verificar valores nulos
notas.isnull().sum()
#%%
"""
    Como tratar os valores nulos?
    temos que pensar em como vamos usar esses valores no futur0,
    temos que pensar a possivel falta de entendimento do dado no futuro
    
    Opcoes de oq fazer com os dados nulos
    1. copiar a coluna que tem os valores nulos e manter duas colunas, 
    uma com o valor real e uma com o valor alterado.
"""
#%% Copiar as colunas 
# pegamos esses valores, pois essas colunas que tem valores nulos
notas['AP1_copia'] = notas['AP1']
notas['AP2_copia'] = notas['AP2']
notas['AC_copia'] = notas['AC']

#%% Alterando os valores NULOS nas colunas certas
notas['AP1'] = notas['AP1'].fillna(0)
notas['AP2'] = notas['AP2'].fillna(0)
notas['AC'] = notas['AC'].fillna(0)

#%% Adicionar novos colunas/valores
notas['media'] = notas['AP1']*0.4 + notas['AP2']*0.4 + notas['AC']*0.2
#%%
"""
    ATENÇÃO: sempre que adicionarmos novos valores/colunas temos que 
    verificar o numero para garantir boa qualidade do dado
"""
#%% Arredondando os valores da media
notas['media'] = notas.media.round(1)

#%% Adicionando status de aprovaçao
notas['situacao'] = ''
#%% PRIMEIRA FORMA DE ADICIONAR VALORES CONDICIONAIS
#%% Adicionando status de 'Aprovado'
notas.loc[notas.media >= 7, 'situacao'] = 'Aprovado'
#%% Adicionando status de 'Reprovado'
notas.loc[notas.media < 3, 'situacao'] = 'Reprovado'
#%% Adicionando status de 'Substitutiva'
notas.loc[(notas.media >= 3) & (notas.media < 7), 'situacao'] = 'Substitutiva'

#%% SEGUNDA FORMA DE ADICIONAR VALORES CONDICIONAIS
def classificar(media):
    if media >= 7:
        return  'Aprovado'
    elif media >= 3:
        return 'Substitutiva'
    else:
        return 'Reprovado'
    
notas['situacao2'] = notas.media.apply(classificar)


#%% Tabela de frequencia da Coluna
# Frequencia Absoluta
freqSituacaoA = notas.situacao.value_counts()

# Frequencia Relativa ( pode colocar qualquer string no parametro )
freSituacaoR = notas.situacao.value_counts("relativa")

#%% Frequencia de mais de uma coluna

# TABELA CRUZADA - quando queremos cruzar informaçoes das SERIES do DATAFRAME
# para variaveis QUALITATIVAS CATEGORICAS

cursos_situacao = pd.crosstab(index=notas['Curso'], 
                              columns=notas['situacao'],
                              margins=True, margins_name='Total')

#%% ATIVIDADE


renda = pd.read_csv("../Aula1_07ago_AnD/B2_renda_atual.csv")
#%%
dfRenda = pd.DataFrame(renda)
#%%
del renda
#%%
# 1. Tabela de Frequencia com todas as tabelas Categoricas
# 2. fazer tabelas cruzadas
# 3. fazer um merge da tabela B1_UF com a tabela RENDA com base no salario
# minimo atual 
# 4. renda 2025/2012 com base no salario minimo
# 5. criar coluna com 'nivel de escolaridade' com base no ano de estudo
# 6. criar coluna de faixa etaria dividida em categorias

#%% 
dfRenda.info()

#%% Verificando valores nulos
dfRenda.isnull().sum()

#%% Adicionando uma COLUNA com o SALARIO MINIMO atual
dfRenda['Renda em 2025'] = 1000






