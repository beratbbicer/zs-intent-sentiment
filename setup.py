from setuptools import setup, find_packages

setup(
    name='zs-intent-sentiment',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'transformers',
        'configparser',
        'json',
        'os'
    ],

    entry_points={
        'console_scripts': [
            'predict=src.source:main',
        ],
    },
    
    description='NLP Intent, Emotion, and Sentiment Analysis with Zero-Shot Learning',
    url='https://github.com/beratbbicer/zs-intent-sentiment/',
    author='Berat Biçer',
    author_email='beratbbicer@gmail.com',
    license='MIT',
    include_package_data=True,
)
