from setuptools import setup,find_packages
setup(
    name='DOPE',
    version='2.0.3',
    description='Python implementation of DOPE Protocol',
    author='Anubhav Mattoo , Shubham Patil , Nikhil Samleti',
    author_email='anubhavmattoo@outlook.com, shubhampatil428@gmail.com, nikhilsamleti99@gmail.com',
    pakages=find_packages(),
    install_requires=[
        'pycryptodome>=3.9',
        'dill',
        'bchlib',
        'pickle5'
    ]
)
