from setuptools import setup, find_packages

from dfgraph import __version__

setup(
    dname='dfgraph',
    version=__version__,

    url='https://github.com/willi-z/dfgraph',
    author='Willi Zschiebsch',
    author_email='willi.w.zschiebsch@web.de',

    packages = find_packages(),
    
)