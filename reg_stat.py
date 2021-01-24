import pandas as pd
import numpy as np
import scipy as sp
import pandas_datareader.data as web
import matplotlib.pyplot as plt

def annu_var(x):
    data = np.var(x, ddof=0)
    a_d = data * ( 252 ** 0.5 )
    return a_d

def opti(x):
    for i in range(100,200):
        _opt = -1
        for n in range(25000):
            if (results[0,n] * i / 100) - 0.15 > 0:
                opt = (i * x[0,n] / 100 - 0.15) - 3*0.5*x[1,n]
            else:
                opt = (i * x[0,n] / 100 - 0.15) - 9*0.5*x[1,n]
            if _opt < opt:
                _opt = opt
            
    return _opt

#list of stocks in portfolio
stocks = ['AAPL','AMZN','MSFT','YHOO']
#calculate mean daily return and covariance of daily returns
mean_daily_returns = returns.mean()
cov_matrix = returns.cov()
#set number of runs of random portfolio weights
num_portfolios = 25000
#set up array to hold results
results = np.zeros((3,num_portfolios))
for i in xrange(num_portfolios):
    #select random weights for portfolio holdings
    weights = np.random.random(4)
    #rebalance weights to sum to 1
    weights /= np.sum(weights)
    
    #calculate portfolio return and volatility
    portfolio_return = np.sum(mean_daily_returns * weights) * 252
    portfolio_std_dev = np.sqrt(np.dot(weights.T,np.dot(cov_matrix, weights))) * np.sqrt(252)
    
    #store results in results array
    results[0,i] = portfolio_return
    results[1,i] = portfolio_std_dev
    #store Sharpe Ratio (return / volatility) - risk free rate element excluded for simplicity
    results[2,i] = results[0,i] / results[1,i]
#convert results array to Pandas DataFrame
results_frame = pd.DataFrame(results.T,columns=['ret','stdev','sharpe'])
#create scatter plot coloured by Sharpe Ratio
plt.scatter(results_frame.stdev,results_frame.ret,c=results_frame.sharpe,cmap='RdYlBu')
plt.colorbar()