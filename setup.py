# necessary to push to PyPI
# cf. http://peterdowns.com/posts/first-time-with-pypi.html
# cf. https://tom-christie.github.io/articles/pypi/

from distutils.core import setup
from setuptools import find_packages

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'ezhc',
  packages = ['ezhc'],
  version = '0.4.5',
  description = 'easy Highcharts, dynamic plots from pandas dataframes in the IPython notebook',
  long_description = long_description,
  author = 'oscar6echo',
  author_email = 'olivier.borderies@gmail.com',
  url = 'https://github.com/oscar6echo/ezhc', # use the URL to the github repo
  download_url = 'https://github.com/oscar6echo/ezhc/tarball/0.4.5', # tag number at the end
  keywords = ['Highcharts', 'pandas', 'notebook', 'javascript'], # arbitrary keywords
  license='MIT',
  classifiers = [ 'Development Status :: 4 - Beta',
                  'License :: OSI Approved :: MIT License',
                  'Programming Language :: Python :: 2.7'
  ],
)