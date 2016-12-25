# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

install_requires = [
    'sqlalchemy==1.0.12',
    'psycopg2==2.6.1'
]

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    install_requires = install_requires,
    entry_points = {'scrapy': ['settings = hemnet.settings']},
)
