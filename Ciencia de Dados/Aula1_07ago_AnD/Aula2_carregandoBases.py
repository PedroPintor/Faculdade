# -*- coding: utf-8 -*-
"""

programação para analise de dados
Aula 1 - carregando bases de dados de vários tipos
12 ago 25

"""

"""
    conexao com o banco de dados
    salvar as tabelas em uma variavel
    DESLIGAR A CONEXAO COM O BANCO DE DADOS
    juntar dois DataFrame
    Fazer o MERGE entre duas tabelas
    Bons habitos para nomes de Colunas
    Verificar variedade de variaveis CATEGORICAS
    Renomear valores das LINHAS
"""



#%% 
import pandas as pd
import sqlite3 

#%% CRIAR UMA CONEXAO COM UM BANCO DE DADOS
conexao1 = sqlite3.connect('B8_escola.db')
conexao2 = sqlite3.connect('b8_turma.db')
#%%  Criar um ponteiro para poder acessar os nomes das tabelas
db1 = conexao1.cursor()
db1.execute("SELECT name FROM sqlite_master WHERE type='table'; ")

#%% visualizar os nomes das tabelas
print(db1.fetchall())
#%% carregar a tabela 'alunos' do banco de dados em um DataFrame
dfAlunos = pd.read_sql("SELECT * FROM alunos", conexao1)

#%% head da tabela
dfAlunos.head()
#%% criando uma conexao com outro banco de dados
db2 = conexao2.cursor()
db2.execute("SELECT name FROM sqlite_master WHERE type='table'; ")
#%% visualizar os noms das tabelas
print(db2.fetchall())
#%% carregar as tabelas e salvar em um DataFrame
dfAlunos2 = pd.read_sql("SELECT * FROM alunos;" , conexao2)
dfNotas2 = pd.read_sql("SELECT * FROM notas; ", conexao2)

#%% DESLIGAR A CONEXAO
conexao1.close()
conexao2.close()
#%% Criar novos dados
tmp = {
       'id_aluno': [ 4, 5],
       'nome' : ['beatriz', 'Giovana'],
       'idade': [ 17, 15],
       'serie': ['2° ano EM', '9° ano']
}

novos_alunos = pd.DataFrame(tmp)
#%% juntar dois DataFrame
dfAlunos2 = pd.concat([dfAlunos2, novos_alunos], ignore_index=True)

#%%
"""
    Ao fazer o MERGE precisamos pensar em como os dados estao relacionados
    precismos pensar o lado que os dados estao e como vao ser juntados

"""
#%% MERGE inner
turma1 = pd.merge(dfAlunos2, dfNotas2,
                  left_on='id_aluno',   # coluna da tabela esquerda
                  right_on='id_aluno',  # coluna da tabela direita
                  how='inner')          # como vai ser juntado

#%% MERFE left 
turma2 = pd.merge(dfAlunos2,dfNotas2,
                  left_on='id_aluno',
                  right_on='id_aluno',
                  how='left')

#%% MERGE right 
turma3 = pd.merge(dfAlunos2,dfNotas2,
                  left_on='id_aluno',
                  right_on='id_aluno',
                  how='right')
#%% MERGE outer
turma4 = pd.merge(dfAlunos2,dfNotas2,
                  left_on='id_aluno',
                  right_on='id_aluno',
                  how='outer')

#%%
notas = pd.read_csv("B3_notas_alunos.csv", encoding='iso-8859-1' ,sep=";")
notas.head()
#%% Verificar os Nomes das Colunas
notas.columns
#%% Alterar nome de colunas - MELHORES HABITOS COLUNAS
tmp = {
       'codigo interno':'codigo_interno',
       'nome da mae': 'mae',
       'nome do aluno': 'aluno'
       }
### COMANDO rename() é sobre o Coluna/DataFrame
notas = notas.rename(columns=tmp)

#%% Verificar Variedades de CATEGORIAS
notas.Curso.unique()

#%% Alteracao de valores nas colunas
tmp = {
       'Adm': 'Administração',
       'Dir': 'Direito',
       'Eco': 'Economia',
       'RI': 'Relações Internacionais'
       }
### COMANDO replace() é sobre a Linha
notas.Curso = notas.Curso.replace(tmp)

#%% 
notas.to_csv('notas_atual.csv', index=False)

#%%