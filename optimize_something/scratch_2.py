import datetime as dt
import pandas as pd
import numpy as np
from util import get_data
import matplotlib.pyplot as plt
from optimization import plot_data

sd = dt.datetime(2008, 1, 1)
ed = dt.datetime(2014, 1, 1)
syms=["GOOG", "AAPL", "GLD", "XOM"]
#gen_plot=False,

"""  		  	   		  	  		  		  		    	 		 		   		 		  
This function should find the optimal allocations for a given set of stocks. You should optimize for maximum Sharpe  		  	   		  	  		  		  		    	 		 		   		 		  
Ratio. The function should accept as input a list of symbols as well as start and end dates and return a list of  		  	   		  	  		  		  		    	 		 		   		 		  
floats (as a one-dimensional numpy array) that represents the allocations to each of the equities. You can take  		  	   		  	  		  		  		    	 		 		   		 		  
advantage of routines developed in the optional assess portfolio project to compute daily portfolio value and  		  	   		  	  		  		  		    	 		 		   		 		  
statistics.  		  	   		  	  		  		  		    	 		 		   		 		  

:param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  	  		  		  		    	 		 		   		 		  
:type sd: datetime  		  	   		  	  		  		  		    	 		 		   		 		  
:param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  	  		  		  		    	 		 		   		 		  
:type ed: datetime  		  	   		  	  		  		  		    	 		 		   		 		  
:param syms: A list of symbols that make up the portfolio (note that your code should support any  		  	   		  	  		  		  		    	 		 		   		 		  
    symbol in the data directory)  		  	   		  	  		  		  		    	 		 		   		 		  
:type syms: list  		  	   		  	  		  		  		    	 		 		   		 		  
:param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your  		  	   		  	  		  		  		    	 		 		   		 		  
    code with gen_plot = False.  		  	   		  	  		  		  		    	 		 		   		 		  
:type gen_plot: bool  		  	   		  	  		  		  		    	 		 		   		 		  
:return: A tuple containing the portfolio allocations, cumulative return, average daily returns,  		  	   		  	  		  		  		    	 		 		   		 		  
    standard deviation of daily returns, and Sharpe ratio  		  	   		  	  		  		  		    	 		 		   		 		  
:rtype: tuple  		  	   		  	  		  		  		    	 		 		   		 		  
"""

# Read in adjusted closing prices for given symbols, date range
#dates = pd.date_range(sd, ed)
# prices_all = get_data(syms, dates)  # automatically adds SPY
# prices = prices_all[syms]  # only portfolio symbols
# prices_SPY = prices_all["SPY"]  # only SPY, for comparison later
#
# # find the allocations for the optimal portfolio
# # note that the values here ARE NOT meant to be correct for a test case
# allocs = np.full((len(syms), 1 / len(syms)))
# # add code here to find the allocations
# cr, adr, sddr, sr = [
#     0.25,
#     0.001,
#     0.0005,
#     2.1,
# ]  # add code here to compute stats
#
# # Get daily portfolio value
# port_val = prices_SPY  # add code here to compute daily portfolio values
#
# # Compare daily portfolio value with SPY using a normalized plot
# if gen_plot:
#     # add code to plot here
#     df_temp = pd.concat(
#         [port_val, prices_SPY], keys=["Portfolio", "SPY"], axis=1
#     )
#     plot_data(df_temp)
#
#
dates = pd.date_range(start = sd, end = ed)

prices_all = get_data(syms, dates)  # automatically adds SPY
prices = prices_all[syms]  # only portfolio symbols
prices_SPY = prices_all["SPY"]  # only SPY, for comparison late
allocs = np.full((len(syms)), 1 / len(syms))

normed = prices/prices.iloc[0]
alloced = normed*allocs
port_val = alloced.sum(axis = 1)

daily_ret =  (port_val/port_val.shift(1))-1


cr, adr, sddr, sr = [ #cr is cumulative returs, adr is average daily returns, sddr is standard daily returns
                        #
    0.25,
    0.001,
    0.0005,
    2.1,
]  # add code here to compute stats
cr = (port_val[-1]/port_val[0])-1
adr = np.mean(daily_ret)
sddr = np.std(daily_ret)
sr = adr/sddr*np.sqrt(252)

prices_SPY = prices_SPY/prices_SPY[0]
df_temp = pd.concat(
            [port_val, prices_SPY], keys=["Portfolio", "SPY"], axis=1
        )
plot_data(df_temp)
plt.show()






