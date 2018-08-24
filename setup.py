from distutils.core import setup

setup(
    name='pycoingecko',
    version='0.0.1',
    packages=['pycoingecko',],
    license='MIT',
    description = 'Python wrapper around the CoinGecko API.',
    long_description=open('README.md').read(),
    author = 'Christoforou Manolis',
    author_email = 'emchristoforou@gmail.com',
    install_requires=['requests'],
    url = 'https://github.com/man-c/pycoingecko',
    )
