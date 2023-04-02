from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(fileName:str)->List[str]:
    '''
        input a file name with all libraries name
        return list of requirements
    '''
    
    requirements=[]
    with open(fileName) as file_name:
        requirements = file_name.readlines()
        requirements = [i.replace("\n" , "") for i in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='Machine Learning End To End Projects',
    version='0.0.1',
    author='soumalla',
    author_email='soumallatarafder@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')


)