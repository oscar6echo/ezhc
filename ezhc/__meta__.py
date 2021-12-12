
__name__ = 'ezhc'
name_url = __name__.replace('_', '-')

__packages__ = [__name__]
__version__ = '0.7.9'
__description__ = 'easy Highcharts & Highstock, dynamic plots from pandas dataframes in the Jupyter notebook'
__author__ = 'oscar6echo'
__author_email__ = 'olivier.borderies@gmail.com'
__url__ = 'https://github.com/{}/{}'.format(__author__,
                                            name_url)
__download_url__ = 'https://github.com/{}/{}/tarball/{}'.format(__author__,
                                                                name_url,
                                                                __version__)
__keywords__ = ['Highcharts', 'Highstock', 'pandas', 'notebook', 'javascript']
__license__ = 'MIT'
__classifiers__ = ['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   ]
__include_package_data__ = True
__package_data__ = {}

__zip_safe__ = False
__entry_points__ = {}
