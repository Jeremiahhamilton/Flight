"""Setup configuration for the flight_math library."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="flight_math",
    version="0.1.0",
    author="Jeremiah Hamilton",
    description="Math that will help us fly! A library for flight calculations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jeremiahhamilton/Flight",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    keywords="flight aerodynamics aviation aerospace dynamics atmosphere",
    project_urls={
        "Bug Reports": "https://github.com/Jeremiahhamilton/Flight/issues",
        "Source": "https://github.com/Jeremiahhamilton/Flight",
    },
)
