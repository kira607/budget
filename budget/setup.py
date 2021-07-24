# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='budget',
    version='0.1',
    description='budget',
    long_description=readme,
    author='kira607',
    url='',
    # packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    dependency_links=[],
    install_requires=[
        # google sheets requirements
        'cachetools==3.1.1',
        'google-api-python-client==1.7.11',
        'google-auth==1.6.3',
        'google-auth-httplib2==0.0.3',
        'httplib2==0.13.1',
        'oauth2client==4.1.3',
        'pyasn1==0.4.6',
        'pyasn1-modules==0.2.6',
        'rsa==4.0',
        'six==1.12.0',
        'uritemplate==3.0.0',
    ],
)