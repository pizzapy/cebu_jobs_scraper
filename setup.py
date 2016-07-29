#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='cebu_jobs_scraper',
    version='0.0.1',
    description="CLI for scraping Cebu jobs sites.",
    long_description=readme + '\n\n' + history,
    author="PizzaPy",
    author_email='dyu@fastmail.com',
    url='https://github.com/pizzapy/cebu_jobs_scraper',
    packages=[
        'cebu_jobs_scraper',
    ],
    package_dir={'cebu_jobs_scraper':
                 'cebu_jobs_scraper'},
    entry_points={
        'console_scripts': [
            'cebu_jobs_scraper=cebu_jobs_scraper.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='cebu_jobs_scraper',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
