from setuptools import setup, find_packages

# python setup.py sdist

setup(
    name='zsins',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'transformers',
        'configparser',
        'tqdm',
    ],
    description='NLP Intent, Emotion, and Sentiment Analysis with Zero-Shot Learning',
    url='https://github.com/beratbbicer/zs-intent-sentiment/',
    author='Berat Biçer',
    author_email='beratbbicer@gmail.com',
    license='MIT',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            "zsins-infer = zsins:main",
        ]
    },
)