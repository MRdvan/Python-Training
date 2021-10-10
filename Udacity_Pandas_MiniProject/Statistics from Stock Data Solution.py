# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# We import pandas into Python
import pandas as pd
import os

# We read in a stock data data file into a data frame and see what it looks like
google_data=pd.read_csv(os.path.dirname(__file__)+"\GOOG.csv")
apple_data=pd.read_csv(os.path.dirname(__file__)+"\AAPL.csv")
amazon_data=pd.read_csv(os.path.dirname(__file__)+"\AMZN.csv")

# We display the first 5 rows of the DataFrame
print(google_data.head())

#%%

# We load the Google stock data into a DataFrame
google_stock = google_data[["Date", "Adj Close"]]
google_stock['Date'] = pd.to_datetime(google_stock['Date'] , format="%Y-%m-%d")
google_stock = google_stock.set_index(["Date"])

# We load the Apple stock data into a DataFrame
apple_stock = apple_data[["Date", "Adj Close"]]
apple_stock['Date'] = pd.to_datetime(apple_stock['Date'] , format="%Y-%m-%d")
apple_stock = apple_stock.set_index("Date")

# We load the Amazon stock data into a DataFrame
amazon_stock = amazon_data[["Date", "Adj Close"]]
amazon_stock['Date'] = pd.to_datetime(amazon_stock['Date'] , format="%Y-%m-%d")
amazon_stock = amazon_stock.set_index("Date")

# We display the google_stock DataFrame
print(google_stock)

#%%

# We create calendar dates between '2000-01-01' and '2016-12-31'
dates = pd.date_range('2000-01-01', '2016-12-31')

# We create and empty DataFrame that uses the above dates as indices
all_stocks = pd.DataFrame(index = dates)

# Change the Adj Close column label to Google
google_stock = google_stock.rename(columns={"Adj Close":"Google"})
# Change the Adj Close column label to Apple
apple_stock = apple_stock.rename(columns={"Adj Close":"Apple"})
# # Change the Adj Close column label to Amazon
amazon_stock = amazon_stock.rename(columns={"Adj Close":"Amazon"})

# We display the google_stock DataFrame
print("GOOGLE STOCK DATA: \n", google_stock)
# We display the apple_stock DataFrame
print("APPLE STOCK DATA: \n", apple_stock)
# We display the amazon_stock DataFrame
print("AMAZON STOCK DATA: \n", amazon_stock)

#%%

# We join the Google stock to all_stocks
all_stocks = all_stocks.join(google_stock)

# We join the Apple stock to all_stocks
all_stocks = all_stocks.join(apple_stock)

# We join the Amazon stock to all_stocks
all_stocks = all_stocks.join(amazon_stock)

# We display the all_stocks DataFrame
print("ALL STOCKS: \n", all_stocks)
#%%

# Check if there are any NaN values in the all_stocks dataframe
# Remove any rows that contain NaN values
all_stocks = all_stocks[all_stocks["Google"].notna() & all_stocks["Apple"].notna() & all_stocks["Amazon"].notna()]

# We display the all_stocks DataFrame
print("ALL STOCK WITHOUT NaN VALUES", all_stocks)

#%%

# Print the average stock price for each stock
# Print the median stock price for each stock
# Print the standard deviation of the stock price for each stock
print(all_stocks.agg(
    {
        "Google": ["mean", "std", "median"],
        "Apple": ["mean", "std", "median"],
        "Amazon": ["mean", "std", "median"],
    }
))

# Print the correlation between stocks
print("correlation:\n",all_stocks.corr())

#%%

# We compute the rolling mean using a 150-Day window for Google stock
# First 150 rows of rollingMean is NaN because we are calculating it per 150rows
rollingMean = all_stocks['Google'].rolling(150).mean()

%matplotlib inline
# We import matplotlib into Python
import matplotlib.pyplot as plt
# We plot the Google stock data
plt.plot(all_stocks['Google'])
# We plot the rolling mean ontop of our Google stock data
plt.plot(rollingMean)
plt.legend(['Google Stock Price', 'Rolling Mean'])
plt.show()




