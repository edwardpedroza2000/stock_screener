from flask import Flask
import yfinance as yf
import pandas as pd
import os

dir_path = os.getcwd()
print(dir_path)
columns = ['Symbol']
tickers = pd.read_csv(dir_path + '\Backend\sptickers.csv', usecols=columns)
stocks = []
for tick in tickers['Symbol']:
    curr_tick = yf.Ticker(tick)
    curr_tick_info  = curr_tick.info
    if("trailingPE" in curr_tick_info and float(curr_tick_info['trailingPE']) < 5.0):
        print(tick + ' | ' + curr_tick_info['longName'] + ' | ' + str(curr_tick_info['trailingPE']))
