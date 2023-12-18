# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:40:07 2023

@author: Ulrich
"""

import requests
import pandas as pd
import streamlit as st

TF = st.number_input('Insert range', min_value=(96),max_value=(2000))
parameters = {
    "step":900,
    "limit":TF,
}

btc = ()
req = requests.get(f"https://www.bitstamp.net/api/v2/ohlc/{'btcusd'}/",
                  params = parameters)
req = req.json()["data"]["ohlc"]
btc = pd.DataFrame(req)
btc['time'] = pd.to_datetime(btc['timestamp'], unit='s')
btc.set_index('time', inplace=True)
for i in range(1):                     
    btc['ticker'] = 'btcusd'
btc = btc[['ticker','close']]

eth = ()
req = requests.get(f"https://www.bitstamp.net/api/v2/ohlc/{'ethusd'}/",
                  params = parameters)
req = req.json()["data"]["ohlc"]
eth = pd.DataFrame(req)
eth['time'] = pd.to_datetime(eth['timestamp'], unit='s')
eth.set_index('time', inplace=True)
for i in range(1):                     
    eth['ticker'] = 'ethusd'
eth = eth[['ticker','close']]

sol = ()
req = requests.get(f"https://www.bitstamp.net/api/v2/ohlc/{'solusd'}/",
                  params = parameters)
req = req.json()["data"]["ohlc"]
sol = pd.DataFrame(req)
sol['time'] = pd.to_datetime(sol['timestamp'], unit='s')
sol.set_index('time', inplace=True)
for i in range(1):                     
    sol['ticker'] = 'solusd'
sol = sol[['ticker','close']]

df = pd.concat([btc, eth, sol]) 

df1 = df.pivot_table(index=['time'],columns='ticker', values=['close'])
df1.columns = [col[1] for col in df1.columns.values]

df_daily_returns = df1.pct_change()
# skip first row with NA 
df_daily_returns = df_daily_returns[1:]

df_cum_daily_returns = (1 + df_daily_returns).cumprod() - 1

st.title('Crypto Returns Tracker')

Chart = df_cum_daily_returns[['btcusd','ethusd','solusd']]
st.line_chart(Chart)

#Chart1 = df_cum_daily_returns[['BTCUSDT','ETHUSDT','SOLUSDT','AVAXUSDT','MATICUSDT','APTUSDT','INJUSDT']]
#Chart2 = df_cum_daily_returns[['BTCUSDT','ETHUSDT','IMXUSDT','GALAUSDT','SANDUSDT','ENJUSDT','OCEANUSDT']]
#Chart3 = df_cum_daily_returns[['BTCUSDT','ETHUSDT','RNDRUSDT','TIAUSDT','FETUSDT','AGIXUSDT','AAVEUSDT']]

#st.line_chart(Chart1)
#st.line_chart(Chart2)
#st.line_chart(Chart3)

