# necessary to push to PyPI
# cf. http://peterdowns.com/posts/first-time-with-pypi.html
# cf. https://tom-christie.github.io/articles/pypi/
# cf. https://pythonhosted.org/setuptools/setuptools.html

# commands:
# python setup.py sdist upload -r testpypi
# python setup.py sdist upload -r pypi


from os import path
from codecs import open
from setuptools import setup, find_packages
from distutils.util import convert_path
from pip.req import parse_requirements

module = 'ezhc'

here = path.abspath(path.dirname(__file__))

meta_ns = {}
ver_path = convert_path(module + '/__meta__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), meta_ns)

name = meta_ns['__name__']
packages = meta_ns['__packages__']
version = meta_ns['__version__']
description = meta_ns['__description__']
author = meta_ns['__author__']
author_email = meta_ns['__author_email__']
url = meta_ns['__url__']
download_url = meta_ns['__download_url__']
keywords = meta_ns['__keywords__']
license = meta_ns['__license__']
classifiers = meta_ns['__classifiers__']
include_package_data = meta_ns['__include_package_data__']
package_data = meta_ns['__package_data__']

install_requires = parse_requirements('requirements.txt', session=False)
install_requires = [str(ir.req) for ir in install_requires]

# with open('README.rst') as f:
#     long_description = f.read()

setup(
    name=name,
    version=version,
    description=description,
    # long_description=long_description,
    author=author,
    author_email=author_email,
    url=url,
    download_url=download_url,
    keywords=keywords,
    license=license,
    classifiers=classifiers,
    packages=packages,
    install_requires=install_requires,
    include_package_data=include_package_data,
    package_data=package_data
)
