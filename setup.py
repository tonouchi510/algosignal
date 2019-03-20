from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='algosignal',
    version='0.1.0',
    description='algorithmic trading signal generator',
    long_description=readme,
    author='tonouchi510',
    author_email='tonouchi27@gmail.com',
    url='https://github.com/tonouchi510/algosignal',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
