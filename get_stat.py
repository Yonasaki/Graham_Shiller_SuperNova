import yfinance as yf
import con_stat as con
import pandas as pd
import os

def Close_1w(x):
    inter = yf.Ticker(x)
    close = inter.history(period='7d').Close
    return close
def Close_1y(x):
    inter = yf.Ticker(x)
    close = inter.history(period='1y').Close
    return close
def Close_1m(x):
    inter = yf.Ticker(x)
    close = inter.history(period='30d').Close
    return close

def Auto_indices_1y():
    indices = ["^GSPC","^DJI","^IXIC","^NYA","^XAX","^BUK100P","^RUT","^FTSE","^GDAXI","^FCHI","^STOXX50E","^N100","^BFX","IMOEX.ME","^N225","^HSI","000001.SS","399001.SZ","^STI","^AXJO","^AORD","^BSESN","^JKSE","^KLSE","^NZ50","^KS11","^TWII","^GSPTSE","^BVSP","^MXX","^MERV","^TA125.TA","^JN0U.JO"]
    k = Close_1y(indices[0])
    for i in range(1,len(indices),1):
        k = con.concat(k,Close_1y(indices[i]))
    k.columns = indices
    return k

def Auto_gold():
    data = pd.read_excel('XAU_USD_History.xlsx')
    ud = data["涨跌幅"]
    return ud

def Auto_oil():
    data = pd.read_excel('WTI_USD_History.xlsx')
    ud = data["涨跌幅"]
    return ud

def Auto_US_bond():
    data = pd.read_csv("10-year-treasury-bond-rate-yield-chart.csv", header = 8, parse_dates = True, na_values="null")
    data = data.dropna()
    return data

def Auto_FR_bond():
    data = pd.read_csv("Rendement de l'Obligation France 10 ans - Données Historiques.csv", header = 0, parse_dates = True, na_values="null")
    data = data[["Date","Dernier"]]
    data = data.dropna()
    return data