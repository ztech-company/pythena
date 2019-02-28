import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyathena_simple',
    version='v0.1.0',
    license='Mozilla Public License Version 2.0',
    author='chris.pruitt',
    url='https://github.com/chrispruitt/pyathena_simple',
    author_email='chris.pruitt15@gmail.com',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas>=0.22.0',
        'boto3>=1.9.90',
        'botocore>=1.12.90',
        'retrying>=1.3.3'
    ],
    description='A simple athena wrapper leveraging boto3 to '
                'execute queries and return results while only requiring a database and a query string.'
)