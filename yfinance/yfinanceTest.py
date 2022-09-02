#!pip install yfinance
import yfinance as yf

#Lista de Ativos da Bolsa para Teste
ativos = ['ITSA4.SA','USIM5.SA','BBAS3.SA','HASH11.SA','MXRF11.SA','TRIS3.SA']

# Loop de geração de arquivos
for ativo in ativos:
    data = yf.download(ativo, group_by="Ticker", period='2022-08-31')
    data['ticker'] = ativo
    data.to_csv(f'ativo_{ativo}.csv')
    print(data)
#print(msft.info)

#data = yf.download("ITSA4.SA", start="2022-07-01", end="2022-09-02")
#data.to_csv("ticker.csv")
#print(data)