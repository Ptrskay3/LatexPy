import sys

if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()



MAJOR = 0
MINOR = 0
MICRO = 1
VERSION = f'{MAJOR}.{MINOR}.{MICRO}'

setup(
    name="LatexPy",
    version=VERSION,
    author="DevTeam",
    author_email="leeh123peter@gmail.com",
    description="Latex ...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ptrskay3/LatexPy",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",     
    ],
    install_requires=[]

)
