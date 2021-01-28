from setuptools import find_packages, setup

setup(
    name="calculator",
    packages=find_packages(include=["calculator"]),
    version="0.2.0",
    author="Ruboon Dej-Udom",
    license="MIT",
    test_suite="tests",
)