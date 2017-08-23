from setuptools import setup, find_packages

setup(
    name='alcomems',
    version='0.0.1',
    description='',
    author='',
    license='',
    url='',
    packages=find_packages(),
    dependency_links=[],
    install_requires=[
        'django==1.11.4',
        'djangorestframework==3.6.4',
        'mysqlclient==1.3.9',
    ],
    include_package_data=True,
    zip_safe=False,
)

