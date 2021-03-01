from setuptools import find_packages, setup

setup(
    name='Gardisto',
    version='0.2.2',
    author='Patrick M. Covert',
    author_email='pmcovert@buffaloist.com',
    description='A basic linux systems monitor utility',
    long_description=open('README.md').read()
    long_description_content_type='text/markdown',
    url='https://gardisto.org',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'gardisto=sentry.cli:main'
        ],
    }
)
