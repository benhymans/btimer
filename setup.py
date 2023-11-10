from setuptools import setup, find_packages

setup(
    name='btimer',
    version='1.0.0',
    description='A simple and useful code timer for python',
    long_description='This package provides a simple way to measure execution time with minimal code.',
    author='Ben Hymans',
    author_email='ben@hytreks.digital',
    url='https://github.com/benhymans/mycodetimer',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    install_requires=[],
)