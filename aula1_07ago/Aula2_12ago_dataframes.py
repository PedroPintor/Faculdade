# -*- coding: utf-8 -*-
"""
extração e preparação de dados
Aula1 - dataframes
12 ago 25
"""

"""

Lendo arquivo csv com/sem o index ja existente nos dados
Aprendendo duas formas de criar um DataFrame dependendo de como vem os dados
Evitar complexidade de leitura ao salvar o index da forma correta
Renomear as variaveis/colunas com uma variavel temporaria

"""


#%% importando bibliotecas
import pandas as pd # manipulação de dataframes

#%% carregar tabelas aula passada
### com o index_col() conseguimos tirar uma coluna (geralmente o index)
dfTurma1 = pd.read_csv("turma1.csv", index_col=(0))
dfTurma2 = pd.read_csv("turma2.csv", index_col=(0))

#%% 1: criando dados 
nomes = ["Pedro", "Garcia", "Pintor"]
idades = [ 20, 21, 24]
locais_nasc = ['SP', 'RJ', 'SP']

#%% criando a list ade tuplas
new_data = list(zip(nomes,idades,locais_nasc))

#%% criando o DataFrame ja com nome de colunas
dfTurma3 = pd.DataFrame(new_data, columns=['nome', 'idade', 'local_nascimento'])

#%% criando um novo DataFrame de outra maneira
"""
temos que analisar como os dados estao vindo
# 1: a primeira vez foi criado a partir de vetores que representam o nome 
# com os seus valores
# 2: agora a segunda vez, é criado um vetor de nomes de colunas, um vetor dos
# dos valores dos index, e um vetor dos dados
"""

#%% 2: criando um novo DataFrame
colunas = ['nome','idade','local_nascimento']
linhas = [100,101,102,150]
dados = [('beatriz', 31, 'SP'),
         ('joaquin', 21, 'SP'),
         ('Marco', 16, 'SP'),
         ('Pedro', 24, 'SP')]
#%% criando o dataFrame
dfTurma4 = pd.DataFrame(data = dados, columns = colunas, index= linhas)

#%% adicionando novas colunas ao DataFrame
# dfTurma1['colunaNova1'] = 'novo valor' # adicionado na mesma coluna
# dfTurma1['colunaNova1'] = 'novo valor' # adicionado na mesma coluna
# dfTurma1['colunaNova2'] = 'novo valor' # adicionado em uma nova coluna

### fazendo dessa forma, eu ja consigo adicionar uma nova coluna ja com o valor
# correto que eu quero passar

#%%
dfTurma1['curso'] = 'Eco'
dfTurma2['curso'] = 'Bio'
dfTurma3['curso'] = 'Adm'
dfTurma4['curso'] = 'CDIA'

#%% criando um novo DataFrame com tudo junto
turma_completa = pd.concat([dfTurma1, dfTurma2, dfTurma3, dfTurma4], ignore_index=True)
#%%
turma_completa['campus'] = 'Faria Lima'
turma_completa['codigo'] = 56775
#%% 
turma_completa.to_csv('turma_completa.csv', index=False)
### turma_completa.to_excel('turma_completa.xlsx', index=False)
# a grande diferença é que o arquivo de execel é 6 vezes maior, pesando mt o arquivo

#%% reorganizar a tabela completa
turma_ordenada = turma_completa.sort_values(by='nome')
"""
 MUITO IMPORTANTE: dessa maneira o index esta ficando todo zuando, sem ordem.
 isso aumenta a complexidade de leitura 
"""
#%% para evitar a complexidade podemos fazer de duas formas
## 1: 
# turma_ordenada = turma_completa.sort_values(by='nome', ignore_index=True)
## 2:
turma_ordenada = turma_ordenada.reset_index(drop=True)

#%% excluir uma linha
turma_ordenada = turma_ordenada.drop(index=4)
#%% excluir duas linhas linhas
turma_ordenada = turma_ordenada.drop(index=[10,12])
#%% excluir um conjunto de linhas do 7 ao 8
turma_ordenada = turma_ordenada.drop(turma_ordenada.index[7:9])

#%% manter os valores com uma condiçao
turma_ordenada = turma_ordenada[ turma_ordenada['idade'] > 18 ] ##.reset_index(drop=True)
#%% temos que resetar o index de novo, evitando aumentar a complexidade
turma_ordenada = turma_ordenada.reset_index(drop=True)

#%% detectar valores duplicados
duplicatas = turma_ordenada[turma_ordenada.duplicated(keep=False)]

#%% ja detecta e exclui as duplitada
turma_ordenada = turma_ordenada.drop_duplicates()
#%% sempre evitando o problema de complexidade
turma_ordenada = turma_ordenada.reset_index(drop=True)

#%%
"""
 renomeando as colunas 
"""
tmp = {
    'nome': 'aluno',
    'local_nascimento' : 'nascimento'       
}

turma_ordenada = turma_ordenada.rename(columns=tmp)
#%%
turma_ordenada = turma_ordenada.drop(columns=['codigo'])
#%% de novo , resetar o index para evitar complexidade
turma_ordenada = turma_ordenada.reset_index(drop=True)

#%% Salvar os dados apos as mudanças
turma_ordenada.to_csv('turma_ordenada.csv', index=False)