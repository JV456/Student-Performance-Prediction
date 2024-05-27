# from typing import List
# from setuptools import find_packages, setup

# HYPEN_E_DOT = '-e .'

# def get_requirements(file_path: str) -> List[str]:
#     """Get the list of requirements from a file"""
#     requirements = []
#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [req.replace("\n", "") for req in requirements]
        
#         if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)
            
#     return requirements

# setup(
#     name='Student-Performance-Prediction',
#     version='0.0.1',
#     author='Jai',
#     author_email='jaivadula@gmail.com',
#     packages=find_packages(),
#     install_requires=get_requirements('requirements.txt')
# )

from typing import List

from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Get the list of requirements from a file"""
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            print("Raw requirements from file:", requirements)  # Debugging line
            requirements = [req.replace("\n", "") for req in requirements]
            print("Processed requirements:", requirements)  # Debugging line
            
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
                print("Removed '-e .', final requirements:", requirements)  # Debugging line
    except Exception as e:
        print(f"Error reading {file_path}: {e}")  # Error handling line
        
    return requirements

setup(
    name='Student-Performance-Prediction',
    version='0.0.1',
    author='Jai',
    author_email='jaivadula@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
