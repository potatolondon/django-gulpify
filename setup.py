import os
from setuptools import setup, find_packages


NAME = 'gulpify'
PACKAGES = find_packages()
DESCRIPTION = 'Django integration with Gulp'
URL = "https://github.com/potatolondon/django-gulpify"
LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
AUTHOR = 'Potato London Ltd.'

setup(
    name=NAME,
    version='0.1',
    packages=PACKAGES,

    # metadata for upload to PyPI
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    keywords=["django", "Gulp", "Javascript"],
    url=URL,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],

    include_package_data=True
)
