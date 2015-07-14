# necessary to push to PyPI
# cf. http://peterdowns.com/posts/first-time-with-pypi.html
# cf. https://tom-christie.github.io/articles/pypi/


from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
  name = 'ezhc',
  packages = ['ezhc'],
  version = '0.4.6',
  description = 'easy Highcharts, dynamic plots from pandas dataframes in the IPython notebook',
  long_description = long_description,
  author = 'oscar6echo',
  author_email = 'olivier.borderies@gmail.com',
  url = 'https://github.com/oscar6echo/ezhc', # use the URL to the github repo
  download_url = 'https://github.com/oscar6echo/ezhc/tarball/0.4.6', # tag number at the end
  keywords = ['Highcharts', 'pandas', 'notebook', 'javascript'], # arbitrary keywords
  license='MIT',
  classifiers = [ 'Development Status :: 4 - Beta',
                  'License :: OSI Approved :: MIT License',
                  'Programming Language :: Python :: 2.7'
  ],
  include_package_data=True,
  package_data={
    'api':
         ['api/hc_object.json',
          'api/hc_option.json',
          'api/hs_object.json',
          'api/hs_option.json'
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
         'samples/df_two_idx_one_col.csv'
        ]
    },
)