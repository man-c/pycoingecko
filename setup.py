#from distutils.core import setup
import setuptools

setuptools.setup(
    name='pycoingecko',
    version='0.2.0',
    packages=['pycoingecko',],
    license='MIT',
    description = 'Python wrapper around the CoinGecko API',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'Christoforou Manolis',
    author_email = 'emchristoforou@gmail.com',
    install_requires=['requests'],
    url = 'https://github.com/man-c/pycoingecko',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    )
