from setuptools import setup, find_packages
import os
import xml.etree.ElementTree as ET
import os
path = (os.path.dirname(os.path.realpath(__file__)))

tree = ET.parse(os.path.join(path, 'package.xml'))

def _t(key):
    return tree.find(key).text

version = _t('version')
if 'VERSION' in os.environ:
    version = os.environ['VERSION']

setup(
    name=_t('name'),
    version=version,
    description=_t('description'),
    author=_t('maintainer'),
    author_email='safijari@isu.edu',
    packages=find_packages(),
    install_requires=['numpy'],  # Optional
)
