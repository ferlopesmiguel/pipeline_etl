import yfinance as yf
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

commodities = ['CL=F', 'GC=F', 'SI=F']

def search_commodities(simbolo, period='5d', interval='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=period, interval=interval)['Close']
    dados['ticker'] = simbolo
    return dados

def search_all_data_commodities(commodities):
    all_data = []
    for commodity in commodities:
        dados = search_commodities(commodity)
        all_data.append(dados)
    return pd.concat(all_data)

if __name__ == "__main__":
    data_concat = search_all_data_commodities(commodities=commodities)
    print(data_concat)