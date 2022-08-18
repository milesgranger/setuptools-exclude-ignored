from setuptools import setup, find_namespace_packages

setup(
    name='package',
    packages=find_namespace_packages(
        include=['package*'], exclude=["package.tests*"]
    ),
    include_package_data=True,
)

