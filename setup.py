'''
Part of packaging and distributing Python Projects. Used by setuptools 
to define configuration of your project,like its metadata, dependencies and more
'''

from setuptools import find_packages,setup
#find_packages file basically go through all the folders and look for __init__.py file and consider them as packages
# The setup() function from the setuptools library acts as the instruction manual for your project. Without it, Python doesn't know how to treat your folder as a "package".
from typing import List

#install all requirements
def get_requirements()->List[str]:
    """
    return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements file not found")

    return requirement_lst

print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="kriti",
    author_email="kriti.gupta1905@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

#-e . refers to the setup.py file like if i write command pip install -r requirements.txt 
# #it will automatically triggers setup.py file for execution
