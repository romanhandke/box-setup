from setuptools import setup, find_packages


def read_requirements():
    '''Read requirements from requirements.txt'''
    with open('requirements.txt', 'r') as req:
        contents = req.read()
        requirements = contents.split('\n')

    return requirements


with open('LICENSE') as f:
    project_license = f.read()

with open('README.md') as f:
    readme = f.read()

setup(
    name='box-setup',
    version='0.1',
    author='Roman Handke',
    author_email='roman.handke@online.de',
    description='Brings a new box up to speed',
    install_requires=read_requirements(),
    long_description=readme,
    license=project_license,
    packages=find_packages(exclude=[]),
    entry_points={
        'console_scripts': [
            'box-setup=box_setup.main:cli'
        ]
    })
