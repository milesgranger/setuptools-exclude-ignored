from setuptools import setup, find_namespace_packages, find_packages

setup(
    name='package',
    packages=find_namespace_packages(
        include=['package*'], exclude=["package.tests*"]
    ),
    zip_safe=False,
    package_data={"package": ["*.pyx"]},
    include_package_data=True,
    test_suite="package.tests"
)

