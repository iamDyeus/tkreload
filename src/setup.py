# /src/setup.py

from setuptools import setup, find_packages

setup(
    name='tkreload',
    version='0.1.0',
    description='A library that auto reloads your tkinter app whenever file changes are detected.',
    author='iamDyeus',
    author_email='dyeusyt@gmail.com',
    packages=find_packages(),
    install_requires=[
        'watchdog',
        'keyboard',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'tkreload=tkreload.main:main',
        ],
    },
)
