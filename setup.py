# necessary to push to PyPI
# cf. http://peterdowns.com/posts/first-time-with-pypi.html
# cf. https://tom-christie.github.io/articles/pypi/
# cf. https://pythonhosted.org/setuptools/setuptools.html


from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()


setup(
  name = 'ezhc',
  packages = ['ezhc'],
  version = '0.6.4',
  description = 'easy Highcharts & Highstock, dynamic plots from pandas dataframes in the Jupyter notebook',
  long_description = long_description,
  author = 'oscar6echo',
  author_email = 'olivier.borderies@gmail.com',
  url = 'https://github.com/oscar6echo/ezhc', # use the URL to the github repo
  download_url = 'https://github.com/oscar6echo/ezhc/tarball/0.6.4', # tag number at the end
  keywords = ['Highcharts', 'Highstock', 'pandas', 'notebook', 'javascript'], # arbitrary keywords
  license='MIT',
  classifiers = [ 'Development Status :: 4 - Beta',
                  'License :: OSI Approved :: MIT License',
                  'Programming Language :: Python :: 2.7',
                  'Programming Language :: Python :: 3.5'
  ],
  install_requires = [
    'pandas>=0.17',
    'jinja2>=2.8',
    'ipython>=3.0',
    'requests>=2.9'
  ],
  include_package_data=True,
  package_data={
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
         'financial_time_series_table.html',
         'script/formatter_basic.js',
         'script/formatter_percent.js',
         'script/formatter_quantile.js',
         'script/json_parse.js',
         'script/Jupyter_logo.png',
         'script/SG_logo.png',
         'script/template_disclaimer.html',
         'script/tooltip_positioner_center_top.js',
         'script/tooltip_positioner_left_top.js',
         'script/tooltip_positioner_right_top.js'
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
         'samples/df_two_idx_one_col.csv',
         'samples/df_two_idx_several_col.csv'
        ]
    },
)

