ezhc
~~~~

**ezhc** stands for easy Highcharts.
`Highcharts <http://www.highcharts.com/>`__ is a popular, flexible,
versatile, user friendly visualisation javascript library. Currently
only `Highcharts <http://www.highcharts.com/demo>`__ and
`Highstock <http://www.highcharts.com/stock/demo>`__, not
`Highmap <http://www.highcharts.com/maps/demo>`__.

**ezhc** is a wrapper that lets you transparently access the full
configuration options of the library as described in their APIs,
directly from the `Jupyter notebook <http://jupyter.org/>`__: +
`Highcharts <http://api.highcharts.com/highcharts>`__ +
`Highstock <http://api.highcharts.com/highstock>`__

You just need to store the data in a
`pandas <http://pandas.pydata.org/>`__ dataframe. See the examples in
the
`notebook <http://nbviewer.ipython.org/github/oscar6echo/ezhc/blob/master/demo_ezhc.ipynb>`__.

To install run from command line:

::

    pip install ezhc

| There are exceptions to the transparent wrapping approach:
| I added 2 datatables (`datatables.net <http://datatables.net/>`__)
  linked to the Highstock call.
| A footer (described in HTML) can be added below a plot. If the footer
  contains an image, it will be burned into the standalone file upon
  save.
| Cf. examples in the notebook.
