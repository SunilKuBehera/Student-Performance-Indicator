from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> list[str] :
    """
    This function reads a requirements file and returns a list of packages.
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        [req.replace("\n","") for req in requirements] 
    
        if "-e." in requirements:
            requirements.remove("-e.")
    return requirements
setup(
    name="Data-Science-Projects",
    version="0.0.1",
    author="SunilKuBehera",
    author_email="sunil050@example.com",
    packages=find_packages(),
    install_requires=get_requirements("Requirements.txt")
)