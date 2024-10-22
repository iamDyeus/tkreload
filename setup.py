from setuptools import setup, find_packages
import pathlib

# Get the long description from the README file
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='tkreload',
    version='1.0.0',
    description='A library that auto reloads your tkinter app whenever file changes are detected.',
    long_description=long_description,  
    long_description_content_type='text/markdown',
    author='iamDyeus',
    author_email='dyeusyt@gmail.com',
    url='https://github.com/iamDyeus/tkreload',
    project_urls={
        'Documentation': 'https://github.com/iamDyeus/tkreload/blob/main/README.md',
        'Bug Tracker': 'https://github.com/iamDyeus/tkreload/issues',
        'Source Code': 'https://github.com/iamDyeus/tkreload',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
    keywords='tkinter auto reload python developer tool file-watcher development',
    license='Apache Software License',
    license_file='LICENSE',
    packages=find_packages(),
    install_requires=[
        'watchdog',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'tkreload=tkreload.main:main',
        ],
    },
)
