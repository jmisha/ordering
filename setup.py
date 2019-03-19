from setuptools import setup, find_packages

setup(
    name='ordering',
    version='0.1',
    packages=find_packages(exclude=['test*']),
    license='MIT',
    description='EDSA python package project',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/jmisha/order',
    author='jmisha',
    author_email='jmisha.adams@gmail.com'
)