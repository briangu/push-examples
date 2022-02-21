#from setuptools import setup
import pushpy_examples
import setuptools
from distutils.core import setup

description = 'Push examples'
try:
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError, RuntimeError):
    long_description = description

setup(
    name='pushpy_examples',
    packages=['pushpy_examples'],
    version=pushpy_examples.__version__,
    description=description,
    long_description=long_description,
    author='Brian Guarraci',
    author_email='brian@ops5.com',
    license='MIT',
    url='https://github.com/briangu/push-examples',
    keywords=['network', 'replication', 'raft', 'synchronization', 'application'],
    setup_requires=['wheel'],
    classifiers=[
        'Topic :: System :: Networking',
        'Topic :: System :: Distributed Computing',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'License :: OSI Approved :: MIT License',
    ]
)
