"""Setup script for package."""
import pathlib
from setuptools import find_namespace_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="unlockGNN",
    version="2.0.0",
    description="Uncertainty quantification for graph neural network models of chemical systems.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/a-ws-m/unlockGNN",
    author="Alexander Moriarty",
    author_email="amoriarty14@gmail.com",
    license="MIT",
    keywords=[
        "keras",
        "tensorflow",
        "megnet",
        "machine learning",
        "uncertainty quantification",
    ],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    packages=find_namespace_packages(include=["unlockgnn.*"]),
    include_package_data=False,
    install_requires=[
        "numpy<=1.19.5",
        "pymatgen<=2021.2.8",
        "megnet>=1.1.4",
        "requests",
        "pyarrow",
        "tensorflow>=2.2",
        "tensorflow-probability>=0.10.1",
        "typish; python_version < '3.8'",
    ],
    python_requires=">=3.6, <3.9",
    extras_require={
        "Compatibility with Python < 3.8": ["typish"],
        "Compatible matminer version": ["matminer==0.6.5"],
    },
)
