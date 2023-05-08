# import yfinance as yf
#
# # Define the stock symbol
# symbol = 'TCS.NS'
#
# # Get the stock price data
# stock = yf.Ticker(symbol)
# price = stock.history(period='1d')['Close'][0]
#
# # Display the results
# print(f"The current stock price of {symbol} is {price}")

# import yfinance as yf
# import matplotlib.pyplot as pt
#
# # Define the stock symbol
# symbol = 'TCS.NS'
#
# # Get the stock price data for today
# stock = yf.Ticker(symbol)
# ## today_data = stock.history(period='1d',interval='1m')
# stock_info = stock.info
# print(stock_info)
#
# ## Extract the closing prices for today
# ## prices = today_data['Close']
# ## table = prices.reset_index()
# ##
# ## pt.plot(table.Datetime,table.Close)
# #
# # # Display the results
# # # print(f"The stock prices for {symbol} today are:\n{prices}")


import yfinance as yf
import pandas as pd

# Define the stock symbol
symbol = 'TCS.NS'

# Get the stock info
stock = yf.Ticker(symbol)
stock_info = stock.info

# Get the stock price data for today
today_data = stock.history(period='1d', interval='30m')

print(today_data)
print(today_data.info())
# Create a dictionary of the relevant information
data = {'Name': [stock_info['shortName']],
        'Symbol': [symbol],
        'Price': [stock_info['currentPrice']],
        'Currency': [stock_info['currency']],
        'Exchange': [stock_info['exchange']],
        'Market Cap': [stock_info['marketCap']],
        'P/E Ratio': [stock_info['trailingPE']],
        'Dividend Yield': [stock_info['trailingAnnualDividendYield']]}

print(data['Price'])
# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(today_data)


# Display the results as a table
print(df.to_string(index=False))

