from setuptools import setup, find_packages
import os

version = '0.0.1-dev'
if 'VERSION' in os.environ:
    version = os.environ['VERSION']

setup(
    name='tiny-tf',
    version=version,
    description='Shameless reimplementation of extremely limited API from Tully Foote\'s TF library',
    author='Jariullah Safi',
    author_email='safijari@isu.edu',
    packages=find_packages(),
    install_requires=['numpy==1.16.4'],  # Optional
)
