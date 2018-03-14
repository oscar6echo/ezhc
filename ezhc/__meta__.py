
__name__ = 'ezhc'
name_url = __name__.replace('_', '-')

__packages__ = [__name__]
__version__ = '0.7.2'
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
                   'Programming Language :: Python :: 3.6'
                   ]
__include_package_data__ = True
__package_data__ = {
    'api':
    ['api/hc_object.json',
     'api/hc_option.json',
     'api/hs_object.json',
     'api/hs_option.json'
     ],
    'script':
        ['script/financial_time_series_0.js',
         'script/financial_time_series_table_1.js',
         'script/financial_time_series_table_2.js',
         'script/financial_time_series_table_options_1.js',
         'script/financial_time_series_table_options_2.js',
         'script/financial_time_series_table.html',
         'script/formatter_basic.js',
         'script/formatter_percent.js',
         'script/formatter_quantile.js',
         'script/json_parse.js',
         'script/Jupyter_logo.png',
         'script/SG_logo.png',
         'script/template_disclaimer.html',
         'script/tooltip_positioner_center_top.js',
         'script/tooltip_positioner_left_top.js',
         'script/tooltip_positioner_right_top.js',
         'script/themes/build_theme_json.ipynb',
         'script/themes/avocado.js',
         'script/themes/avocado.json',
         'script/themes/dark-blue.js',
         'script/themes/dark-blue.json',
         'script/themes/dark-green.js',
         'script/themes/dark-green.json',
         'script/themes/dark-unica.js',
         'script/themes/dark-unica.json',
         'script/themes/gray.js',
         'script/themes/gray.json',
         'script/themes/grid-light.js',
         'script/themes/grid-light.json',
         'script/themes/grid.js',
         'script/themes/grid.json',
         'script/themes/sand-signika.js',
         'script/themes/sand-signika.json',
         'script/themes/skies.js',
         'script/themes/skies.json',
         'script/themes/sunset.js',
         'script/themes/sunset.json'
         ],
    'samples':
        ['samples/df_bubble.csv',
         'samples/df_heatmap.csv',
         'samples/df_one_idx_one_col.csv',
         'samples/df_one_idx_several_col_2.csv',
         'samples/df_one_idx_several_col.csv',
         'samples/df_one_idx_two_col.csv',
         'samples/df_scatter.csv',
         'samples/df_several_idx_one_col.csv',
         'samples/df_several_idx_one_col_2.csv',
         'samples/df_two_idx_one_col.csv',
         'samples/df_two_idx_several_col.csv'
         ]
}

__zip_safe__ = False
__entry_points__ = {}
