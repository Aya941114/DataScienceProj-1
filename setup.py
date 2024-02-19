## This setup.py helps to make our machine leaning model a package that can be used in other applications later
## This will look for any folder which has __init__.py and build that as a package, meaning that our machine learning model must be in a folder with a __init__.py file
## When we install the packages by running the requirements.txt file we want this setup.py file to be triggered so we put the '-e .' in the requirements.txt file

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
  # this function will return the list of requiremnts #

  requirements=[]
  with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.replace("\n","") for req in requirements]

    if HYPHEN_E_DOT in requirements:
      requirements.remove(HYPHEN_E_DOT) # this will remove the -e . from the list of packages #

  return requirements

setup(
  name='DSproject-1',
  version='0.0.1',
  author='Ayavuya',
  author_email='ayagenu@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt') ## we want to return all the packages in requirements.txt in list form and this function does that
)
    