from flask import Flask
import yfinance as yf
import pandas as pd
app = Flask(__name__)

dir_path = os.getcwd()
sp500data = pd.read_csv(dir_path + '\Backend\sptickers.csv')
tickers = [row['Ticker'] for row in sp500data]

@app.route('/')

def main():
    
    wiki_data=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies') # Open the link and download S&P company details in a table
    data = wiki_data[0] # All data is stored in first cell
    return print(data)
    # drop columns 'SEC filings' Since we are dropping columns we have axis = 1 and inplace = True as we are removing these columns in original dataframe
    # data.drop(['SEC filings'], axis=1, inplace=True)
    # sorted_data = data.sort_values(by=['Symbol'], ascending=True) # Sort the dataframe on ticker in alphabetical ascending order
    # # Convert the dataframe to csv file
    # sorted_data.to_csv('S&P500Tickers.csv', mode='w', index=False) #index is False as we don't want to write index in csv file
    # NTR = yf.Ticker("NTR")
    return NTR.info

app.run(port=5000)