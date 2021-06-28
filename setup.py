"""Library for parsing FIT files and returning them as lists of messages dictionaries."""

import re
import os
from setuptools import setup


def get_version(version_file):
    """Extract version fron module source."""
    with open(version_file, 'r') as file:
        data = file.read()
        match = re.search(r'version_info = \((\d), (\d), (\d)\)', data, re.M)
        if match:
            return f'{match.group(1)}.{match.group(2)}.{match.group(3)}'


def get_long_description(readme_file):
    """Extract long description fron the module readme."""
    with open(readme_file, "r", encoding="utf-8") as file:
        return file.read()


def get_requirements(requirements_file):
    """Extract long requirements fron the module requirements.txt."""
    print(f"Loading requirements from {requirements_file} in {os.getcwd()}")
    with open(requirements_file, "r", encoding="utf-8") as file:
        return file.readlines()


module_name = 'fitfile'
module_version = get_version(module_name + os.sep + 'version_info.py')
module_long_description = get_long_description('README.rst')
install_requires = get_requirements('requirements.txt')

print(f"Building {module_name} {module_version}")

setup(name=module_name, version=module_version, author='Tom Goetz', packages=[module_name, f'{module_name}.conversions', f'{module_name}.exceptions', f'{module_name}.field_enums'],
      description='Decode FIT format files.',
      long_description=module_long_description,
      long_description_content_type='text/x-rst',
      url="https://github.com/tcgoetz/Fit",
      install_requires=install_requires,
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          "Programming Language :: Python :: 3",
          "Operating System :: OS Independent"],
      python_requires=">=3.0")
