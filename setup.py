from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path:str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    :param file_path: str - path to the requirements file
    :return: list - list of requirements
    """

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove any whitespace characters like `\n` at the end of each line
        requirements=[req.replace('\n', '') for req in requirements]

    # If '-e .' is in the requirements, remove it
        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name="ml_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt '),
    author="Arpita",
    author_email="arpitanarkhede@gmail.com",
    description="A machine learning project.",
    url="https://github.com/arpita-narkhede/ml_project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)