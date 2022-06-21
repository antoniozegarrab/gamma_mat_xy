
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='gamma_mat_xy',
    version='0.0.1',
    description='From classical to quantum machine learning with tensor networks',
    long_description=readme,
    author='Antonio Zegarra',
    author_email='antonio.zegarra@fri.uni-lj.si',
    url='https://github.com/antoniozegarrab/gamma_mat_xy',
    license=license,
    packages=["gamma_mat_xy"],
)
