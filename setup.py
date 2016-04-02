import os
import sys
from setuptools import setup, find_packages
from fase import __version__, __author__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload -r pypi')
    sys.exit()

dist = setup(
    name='pyfase',
    version=__version__,
    author=__author__,
    author_email='joaci.morais@gmail.com',
    packages=find_packages(),
    platforms='any',
    url='https://github.com/jomorais/pyfase',
    license='GPLv3',
    description='A Fast-Asynchronous-microService-Environment based on ZeroMQ.',
    install_requires=['zmq'],
    classifiers=['Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: Implementation',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: System :: Distributed Computing',
                 'Topic :: System :: Networking']
)
