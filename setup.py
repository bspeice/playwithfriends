from setuptools import setup, find_packages

from playwithfriends import __version__

print(find_packages())

setup(
    name='Playwithfriends',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'requests >= 2.10.0',
        'bottle >= 0.12.7'
    ],
    author='Bradlee Speice',
    author_email='bradlee.speice@gmail.com',
    description='Figure out what games you and your friends should play'
)
