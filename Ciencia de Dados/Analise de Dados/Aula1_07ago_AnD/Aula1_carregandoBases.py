# -*- coding: utf-8 -*-
"""
programação para analise de dados
Aula 1 - carregando bases de dados de vários tipos
07ago25
"""
#%% carregar as bibliotecas
import pandas as pd
#%%
base1=pd.read_csv('B1_UF_regioes.csv')
#%%
base1.info()
#%%
base2=pd.read_csv('B2_renda.csv',sep=';',decimal=',')
#%%
base2.info()
#%%
base2.to_csv('B2_renda_atual.csv',index=False)
#%%
base3=pd.read_csv('B3_notas_alunos.csv', encoding='iso-8859-1',sep=';')
#%% 
'''
#ISO 8859-1, também conhecido como Latin-1, 
é um padrão de codificação de caracteres 
do alfabeto latino
Aceita acentos e alguns caracteres especiais 
É usado na nomenclatura da América Latina, 
considerando particularidades de idiomas latinos, 
como a ç 
'''
#%%
base3.info()
#%%
base4=pd.read_csv('B4_dados_vendas.csv',sep=';',decimal=',')
#%%
base4['Data_venda'] = pd.to_datetime(base4['Data_venda'], 
                                     format='%d/%m/%Y').dt.date
#%% carregando  arquivo do excel
base5=pd.read_excel('B5_alturas_campeonato.xlsx')
#%%
base5['nascimento']=base5['nascimento'].dt.date
#%%
#%% carregando JSON direto (estrutura de lista de dicionários)
base6 = pd.read_json('B6_alunos.json')

#%% carregando XML direto 
base7 = pd.read_xml('B7_alunos.xml')

#%%


#%%













#%%









