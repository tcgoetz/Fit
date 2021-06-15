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


module_name = 'fit'
module_version = get_version(module_name + os.sep + 'version_info.py')

setup(name=module_name, version=module_version, author='Tom Goetz', packages=[module_name, f'{module_name}.conversions', f'{module_name}.exceptions', f'{module_name}.field_enums'],
      license=open('LICENSE').read(), description='Decode FIT format files',
      url="https://github.com/tcgoetz/Fit", python_requires=">=3.0")
