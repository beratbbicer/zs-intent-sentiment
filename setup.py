from setuptools import setup, find_packages

setup(
    name='zs_intent_sentiment',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'transformers',
        'configparser',
    ],
    description='NLP Intent, Emotion, and Sentiment Analysis with Zero-Shot Learning',
    url='https://github.com/beratbbicer/zs-intent-sentiment/',
    author='Berat Biçer',
    author_email='beratbbicer@gmail.com',
    license='MIT',
    include_package_data=True,
)
