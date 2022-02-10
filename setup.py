from  setuptools import setup, find_packages
from json_tools.json_search import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="json_search",
    version='0.1.0',
    author="gpwork4u",
    author_email="gpwork4u@gmail.com",
    description="A tool for analysis json content with some key",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gpwork4u/json_tools",
    packages = ['json_tools'],
    package_dir={'json_tools': 'json_tools'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.6',
)
