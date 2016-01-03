###ezhc

**ezhc** stands for easy Highcharts.
[Highcharts](http://www.highcharts.com/) is a popular, flexible, versatile, user friendly visualisation javascript library.
Currently only [Highcharts](http://www.highcharts.com/demo) and [Highstock](http://www.highcharts.com/stock/demo), not [Highmap](http://www.highcharts.com/maps/demo).

**ezhc** is a wrapper that lets you transparently access the full configuration options of the library as described in their APIs, directly from the [Jupyter notebook](http://jupyter.org/):
+ [Highcharts](http://api.highcharts.com/highcharts)
+ [Highstock](http://api.highcharts.com/highstock)

You just need to store the data in a [pandas](http://pandas.pydata.org/) dataframe.
See the examples in the [notebook](http://nbviewer.ipython.org/github/oscar6echo/ezhc/blob/master/demo_ezhc.ipynb).

To install run from command line:
```
pip install ezhc
```

There is an exception to the transparent wrapping approach:  
I added a datatable ([datatables.net](http://datatables.net/)) linked to the Highstock. It shows the performance / IRR / Volatility / Sharpe Ration / Max Drawdown over a modifiable time window (for financial data).  
Note: Due to CSS collisions between the datatables lib and the jupyter notebook, there is a slight visual difference between the notebook embedded plot and the standalone saved html file.  
See the example in the notebook.
