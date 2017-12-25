# ezhc

## 1 - Introduction

**ezhc** stands for easy Highcharts.
[Highcharts](http://www.highcharts.com/) is a popular, flexible, versatile, user friendly visualisation javascript library.
Currently only [Highcharts](http://www.highcharts.com/demo) and [Highstock](http://www.highcharts.com/stock/demo), not [Highmap](http://www.highcharts.com/maps/demo).

**ezhc** is a wrapper that lets you transparently access the full configuration options of the library as described in their APIs, directly from the [Jupyter notebook](http://jupyter.org/):
+ [Highcharts](http://api.highcharts.com/highcharts)
+ [Highstock](http://api.highcharts.com/highstock)

You need bring the data in a [pandas](http://pandas.pydata.org/) dataframe as shown in the many examples in the [demo notebook](http://nbviewer.ipython.org/github/oscar6echo/ezhc/blob/master/demo_ezhc.ipynb).

To update global options and apply themes see the [demo notebook for global options and styles](http://nbviewer.ipython.org/github/oscar6echo/ezhc/blob/master/demo_ezhc_themes_and_global_options.ipynb).  
The highcharts [official themes](https://github.com/highcharts/highcharts/tree/master/js/themes) are available in **ezhc**.

## 2 - Install

To install run from command line:
```
pip install ezhc
```

## 3 - Exceptions

There are exceptions to the transparent wrapping approach:  
I added 2 datatables ([datatables.net](http://datatables.net/)) linked to the Highstock call.  
A footer (described in HTML) can be added below a plot. If the footer contains an image, it will be burned into the standalone file upon save.  
Cf. examples in the [demo notebook](http://nbviewer.ipython.org/github/oscar6echo/ezhc/blob/master/demo_ezhc.ipynb).  

<!-- pandoc --from=markdown --to=rst --output=README.rst README.md -->
