from setuptools import setup, find_packages

setup(
    name='pod2rssd',
    version='0.1.0',
    url='https://github.com/pfnsec/pod2rssd',
    author='Peter Sherman',
    author_email='pfnsec@gmail.com',
    description='Description of my package',
    packages=find_packages(),    
    install_requires = [
        'uvicorn >= 0.17.6',
        'feedgen >= 1.0.0',
        'jinja2 >= 3.1.3',
    ],
)