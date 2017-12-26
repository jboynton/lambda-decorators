from setuptools import setup

import lambda_decorators

long_description = lambda_decorators.__doc__

setup(
    name='lambda-decorators',

    version=lambda_decorators.__version__,

    description='A collection of useful decorators for making AWS Lambda handlers',
    long_description=long_description,

    url='http://lambda-decorators.readthedocs.io',

    author='Daniel Schep',
    author_email='dschep@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Environment :: Other Environment',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='serverless lambda decorator aws',

    py_modules=['lambda_decorators'],
)
