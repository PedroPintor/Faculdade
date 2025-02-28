import pandas as pd
import yfinance as yf
import os
import json

def get_historico_dados( ticker='AAPl', period='1mo',interval='1d'):
    dados = yf.Ticker(ticker)
    if dados:
       df = dados.history(period=period, interval=interval) 
       print(df)
       return df
    else: 
        return None

def salvar_json(dados, filename=None, caminho=None):
    if filename is None:
        filename = "dados.json"
    
    if caminho is None:
        caminho = os.getcwd()

    try:
        json_str = dados.to_json(orient='records', date_format='iso')
        json_obj = json.loads(json_str)   
    except Exception as e:
        print("Erro ao converter os dados para JSON:", e)
        return None

    caminho_arquivo = os.path.join(caminho, filename)
    
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(json_obj, arquivo, ensure_ascii=False, indent=4)
        print("Arquivo salvo em:", caminho_arquivo)
        return caminho_arquivo
    except Exception as e:
        print("Erro ao salvar o arquivo:", e)
        return None

if __name__ == '__main__':
    info = get_historico_dados()
    if not info.empty:
        salvar_json(info)
    else:
        print('sem informaçoes ;(')
