import os
import re
import setuptools

def get_version(package):
    '''
    Return package version as listed in `__version__` in `init.py`.
    '''
    with open(os.path.join(package, '__init__.py')) as f:
        return re.search('__version__ = [\'"]([^\'"]+)[\'"]', f.read()).group(1)


with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='rpspy', # Replace with your own username
    version=get_version('rpspy'),
    author='RPS Team',
    author_email='info@remedyproduct.com',
    description='Remedy Product python library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/remedyproduct/rpspy',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'sqlalchemy>=1.3.5',
    ],
    python_requires='>=3.7',
)
