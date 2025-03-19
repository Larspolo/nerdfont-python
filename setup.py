from setuptools import setup
import pypandoc
import nerdfont

REL_VERSION = '1'

setup(
    name='nerdfont',
    packages=['nerdfont'],
    version=nerdfont.VERSION + '-' + REL_VERSION,
    description='The Nerd Font icon set for python',
    long_description=pypandoc.convert_file('readme.md', 'rst'),
    license='Code: Apache License, Version 2.0, Icons: SIL OFL 1.1',
    author='Larspolo',
    maintainer='Larspolo',
    url='https://github.com/Larspolo/nerdfont-python',
    install_requires=[
        'pyyaml>=5.0,<=6',  
    ],
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
    ],
    test_suite='nose.collector',
    tests_require=['nose', 'coverage'],
)
