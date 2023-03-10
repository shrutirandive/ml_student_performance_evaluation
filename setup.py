'''The setup.py is a Python script typically included with Python-written libraries or apps. 
Its objective is to ensure that the program is installed correctly.

The setup.py file may be the most significant file that should be placed at 
the root of the Python project directory. 
It primarily serves two purposes:
1. It includes choices and metadata about the program, such as the package name, version, author, 
license, minimal dependencies, entry points, data files, and so on.
2. Secondly, it serves as the command line interface via which packaging commands may be executed.

'''

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Shruti',
author_email='shrutirandive4@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)