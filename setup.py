from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='Gardisto',
    version='0.2.1',
    author='Patrick M. Covert',
    author_email='pmcovert@buffaloist.com',
    description='A basic systems monitor utility',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://173.64.3.56:65524/gitlab/patrick/gardisto',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'gardisto=sentry.cli:main'
        ],
    }
)
