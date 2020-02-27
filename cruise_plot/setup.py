
"""Setup for the chocobo package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Tulay Çokacar",
    author_email="tulay.cokacar@gmail.com",
    name='cruise_plot',
    license="MIT",
    description='Read Depth,Temp,Saln,Dens of cruise data from CSV, having 1 line header',
    version='v0.0.3',
    long_description=README,
    url='https://github.com/.......',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['requests'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],

