import streamlit as st
import pandas as pd
import yfinance as yf

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Meta!

""")

#define the ticker
tickerSymbol = 'META'

#get data on the ticker
tickerData = yf.Ticker(tickerSymbol)

#get historical prices
tickerDf = tickerData.history(period='1d', start='2012-5-31', end='2022-5-31')
on_bad_lines="skip"

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)