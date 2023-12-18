# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 15:23:22 2023

@author: Ulrich
"""

import json
import requests
import pandas as pd
import streamlit as st

st.title('Dashboard')

tickers = ["btcusd","ethusd"]
dropdown = st.selectbox("Choose your Token",tickers)

req = requests.get(f"https://www.bitstamp.net/api/v2/ohlc/{dropdown}/?step=3600&limit=10")
req = req.json()["data"]["ohlc"]
df = pd.DataFrame(req)
df
