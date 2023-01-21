from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'Generating random numbers faster than numpy'
LONG_DESCRIPTION = 'A package that allows to generate random numbers for machine learning tasks based on C++ library random123'

# Setting up
setup(
    name="igenerator",
    version=VERSION,
    author="Mahimai Raja J ( iKurious )",
    author_email="<info@mahimairaja.in>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['jax', 'jaxlib', 'numpyro'],
    keywords=['python', 'random generator', 'numbers', 'machine learning', 'database', 'data generator'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)