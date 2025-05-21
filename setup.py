from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="capacitance",
    version="0.1.0",
    author="Dagmawi Tadesse, Drew Parsons",
    author_email="daggbt@gmail.com",
    description="A package for calculating differential capacitance of electrochemical systems using the semi-analytical Carnahan-Starling steric models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daggbt/pycapapacitance",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Electro-Chemistry, Physics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "pandas>=1.3.0",
    ],
)