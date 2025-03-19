from setuptools import setup, find_packages
import nerdfont

# Read the contents of your README.md file
with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REL_VERSION = '3'

setup(
    name='nerdfont',
    version=nerdfont.VERSION + '.post' + REL_VERSION,
    description='The Nerd Font icon set for python',
    long_description=long_description,
    long_description_content_type="text/markdown", 
    license='Code: Apache License, Version 2.0, Icons: Nerd Fonts Licensing',
    author='Larspolo',
    maintainer='Larspolo',
    packages=find_packages(),
    url='https://github.com/Larspolo/nerdfont-python',
    install_requires=[
        'pypandoc>=1.15',  
    ],
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
    ],
)
