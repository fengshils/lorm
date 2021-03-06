#coding: utf-8
from setuptools import setup, find_packages

__version__ = '0.3.23'

setup(
    name         = "lorm",
    version      = __version__,
    keywords     = ['orm'],
    author       = "zii",
    author_email = "gamcat@gmail.com",
    url          = "https://github.com/zii/lorm",
    description  = "A light weight mysql client library.",
    long_description = open('README.rst').read(),
    license      = "MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires = [],
    #py_modules = ['lorm'],
    packages = find_packages(),
)
