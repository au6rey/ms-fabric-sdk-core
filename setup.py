from setuptools import setup, find_packages

setup(
    name='msfabricpysdkcore',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.30.0',
        'azure-identity>=1.15.0',
    ]
)