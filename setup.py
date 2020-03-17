import os
import re
from setuptools import setup, find_packages

requires = [
    "datacoco-core==0.1.1",
    "datacoco-db==0.1.7",
    "datacoco-batch==0.1.0",
    "datacoco-secretsmanager==0.1.3",
]


def get_version():
    version_file = open(os.path.join("scripty", "__version__.py"))
    version_contents = version_file.read()
    return re.search('__version__ = "(.*?)"', version_contents).group(1)


setup(
    name="scripty",
    packages=find_packages(exclude=["tests*"]),
    version=get_version(),
    license="MIT",
    description="Script runner to execute ELT and load tasks by Equinox",
    long_description=open("README.rst").read(),
    author="Equinox Fitness",
    install_requires=requires,
    scripts=['bin/scripty'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)
