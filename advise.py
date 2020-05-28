import pandas as pd
import matplotlib.pyplot as pl
import requests
import datetime
import time
import numpy as np
from sklearn import linear_model
from sklearn import preprocessing, model_selection

def fetchCryptoData(symbol, frequency):
    #Parameters:
    #String symbol
    #int frequency (of data points) = 300,900,1800,7200,14400,86400
    #Returns: dataframe from first available date
    fetchString = 'USDT_' + symbol
    url ='https://poloniex.com/public?command=returnChartData&currencyPair='+fetchString+'&end=9999999999&period='+str(frequency)+'&start=0'
    df = pd.read_json(url)
    df.set_index('date',inplace=True)
    return df

def predictValue(symbol,days): #int days (how far to forecast)
    coin = fetchCryptoData(symbol,86400)
    coin = coin[['close']]
    forecast_dist = days
    coin['prediction'] = coin.shift(-forecast_dist)
    x = np.array(coin.drop(['prediction'],1))
    x = preprocessing.scale(x)
    xforecast = x[-forecast_dist:]
    x = x[:-forecast_dist]
    y = np.array(coin['prediction'])
    y = y[:-forecast_dist]
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x,y,test_size = 0.2)
    clf = linear_model.LinearRegression() #classifier
    clf.fit(x_train,y_train)
    confidence = clf.score(x_test, y_test)
    forecast_prediction = clf.predict(xforecast)    
    return forecast_prediction

def movAvgGraph(symbol):
    coin = fetchCryptoData(symbol, 86400)
    coin["20d"] = np.round(coin["close"].rolling(20).mean().fillna(0),2)
    coin["50d"] = np.round_(coin["close"].rolling(50).mean().fillna(0), 2)
    coin["200d"] = np.round(coin["close"].rolling(200).mean().fillna(0), 2)
    movAvg = pd.DataFrame({"price": coin["close"],
                           "20d avg": coin["20d"],
                           "50d avg": coin["50d"],
                           "200d avg": coin["200d"]})
    ax = movAvg.plot(grid = True)
    pl.title(symbol)
    pl.ylabel("price (USD)")
    pl.tight_layout()
    pl.show()
    #fig = ax.get_figure()
    #fig.savefig('movAvg.png',bbox_inches='tight')


def dayPercentChange(symbol):
    #Parameters:
    #String symbol
    #int frequency (of data points) = 300,900,1800,7200,14400,86400
    #Returns: dataframe from first available date
    fetchString = 'USDT_' + symbol
    frequency = 86400
    now = str(int(time.time())-86400*3)
    url ='https://poloniex.com/public?command=returnChartData&currencyPair='+fetchString+'&end=9999999999&period='+str(frequency)+'&start=' + now
    df = pd.read_json(url)
    df.set_index('date',inplace=True)
    df = df[['close']]
    change = (df['close'].iloc[-1]/df['close'].iloc[-2])-1
    return change


def profileSim(days): #DOGE to USDT not available on poloniex
    BTC = fetchCryptoData('BTC',14400)
    BTC = BTC[["close"]].tail(6*days)
    BTC.rename(columns={'close': 'BTC'}, inplace=True)
    ETH = fetchCryptoData('ETH',14400)
    ETH = ETH[["close"]].tail(6*days)
    ETH.rename(columns={'close': 'ETH'}, inplace=True)
    LTC = fetchCryptoData('LTC',14400)
    LTC = LTC[["close"]].tail(6*days)
    LTC.rename(columns={'close': 'LTC'}, inplace=True)
    BCH = fetchCryptoData('BCH',14400)
    BCH = BCH[["close"]].tail(6*days)
    BCH.rename(columns={'close': 'BCH'}, inplace=True)
    XRP = fetchCryptoData('XRP',14400)
    XRP = XRP[["close"]].tail(6*days)
    XRP.rename(columns={'close': 'XRP'}, inplace=True)
    prof = BTC.join(ETH).join(LTC).join(BCH).join(XRP)
    coins = ['BTC','ETH','LTC','BCH','XRP']
    returns = prof.pct_change()
    mean_daily_returns = returns.mean()
    cov_mat = returns.cov()
    numsims = 50000 # number of portfolios to simulate
    results = np.zeros((3+len(coins),numsims))
    #print results
    for i in range(numsims):
        weights = np.array(np.random.random(5))
        weights /= np.sum(weights)
        portfolio_return = np.sum(mean_daily_returns*weights)*6*days
        test = np.cov(cov_mat, weights)
        portfolio_std_dev = np.sqrt(np.dot(weights.T,np.dot(cov_mat, weights)))*np.sqrt(6*days)
        results[0,i] = portfolio_return
        results[1,i] = portfolio_std_dev
        results[2,i] = results[0,i]/results[1,i]
        for j in range(len(weights)):
            results[j+3,i] = weights[j]
    return results #result is  return, std dev(volatility), sharpe ratio, followed by 4 weights

# #movAvgGraph('XRP')
# test = profileSim(300) #simulate Sharpe ratio for previous 300 trading days
# max_sharpe_index = np.argmax(test, axis=1)
# max_sharpe_values = test[:,max_sharpe_index[2]] # return column with highest sharpe ratio
# print "The maximum Sharpe ratio was: {0:.2f} with a std dev of {1:.2f} and {2:.2f}% BTC {3:.2f}% ETH {4:.2f}% LTC {5:.2f}% BCH {6:.2f}% XRP".format(max_sharpe_values[2],max_sharpe_values[1],max_sharpe_values[3]*100,max_sharpe_values[4]*100,max_sharpe_values[5]*100,max_sharpe_values[6]*100,max_sharpe_values[7]*100)
# min_var_index = np.argmin(test, axis=1)
# min_var_values = test[:,min_var_index[1]] #return column with lowest std dev
# print "The minimum variance portfolio had Sharpe ratio: {0:.2f} with a std dev of {1:.2f} and {2:.2f}% BTC {3:.2f}% ETH {4:.2f}% LTC {5:.2f}% BCH {6:.2f}% XRP".format(min_var_values[2],min_var_values[1],min_var_values[3]*100,min_var_values[4]*100,min_var_values[5]*100,min_var_values[6]*100,max_sharpe_values[7]*100)

# #print predictValue('BTC',10)

