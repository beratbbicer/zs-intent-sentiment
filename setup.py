from setuptools import setup, find_packages

setup(
    name='zs-intent-sentiment',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'transformers',
        'os'
        'configparser'
        'json'
    ],
    entry_points={
        'console_scripts': [
            'predict=src.source:main',
        ],
    },
)
