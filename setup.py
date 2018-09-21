from setuptools import setup, find_packages

setup(
    name='tiny-tf',
    version='0.0.1',
    description='Shameless reimplementation of extremely limited API from Tully Foote\'s TF library',
    author='Jariullah Safi',
    author_email='safijari@isu.edu',
    packages=find_packages(),
    install_requires=['numpy'],  # Optional
)
