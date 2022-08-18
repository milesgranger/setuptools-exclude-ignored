# setuptools-exclude-ignored

Example of setuptools adding back a package, even though it's part of `find_packages(..., exclude=[...])`

This is intended to exlude the `package.tests` package.

Result:
```
python setup.py bdist
running bdist
running bdist_dumb
running build
running build_py
creating build
creating build/lib
creating build/lib/package
copying package/__init__.py -> build/lib/package
creating build/lib/package/packagea
copying package/packagea/__init__.py -> build/lib/package/packagea
running egg_info
creating package.egg-info
writing package.egg-info/PKG-INFO
writing dependency_links to package.egg-info/dependency_links.txt
writing top-level names to package.egg-info/top_level.txt
writing manifest file 'package.egg-info/SOURCES.txt'
writing manifest file 'package.egg-info/SOURCES.txt'
/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages/setuptools/command/build_py.py:202: SetuptoolsDeprecationWarning:     Installing 'package.tests' as data is deprecated, please list it in `packages`.
    !!


    ############################
    # Package would be ignored #
    ############################
    Python recognizes 'package.tests' as an importable package,
    but it is not listed in the `packages` configuration of setuptools.

    'package.tests' has been automatically added to the distribution only
    because it may contain data files, but this behavior is likely to change
    in future versions of setuptools (and therefore is considered deprecated).

    Please make sure that 'package.tests' is included as a package by using
    the `packages` configuration field or the proper discovery methods
    (for example by using `find_namespace_packages(...)`/`find_namespace:`
    instead of `find_packages(...)`/`find:`).

    You can read more about "package discovery" and "data files" on setuptools
    documentation page.


!!

  check.warn(importable)
creating build/lib/package/tests
copying package/tests/__init__.py -> build/lib/package/tests
copying package/tests/file.pyx -> build/lib/package/tests
/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
installing to build/bdist.linux-x86_64/dumb
running install
running install_lib
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/dumb
creating build/bdist.linux-x86_64/dumb/home
creating build/bdist.linux-x86_64/dumb/home/milesg
creating build/bdist.linux-x86_64/dumb/home/milesg/miniconda3
creating build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs
creating build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev
creating build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib
creating build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9
creating build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages
creating build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages/package
creating build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages/package/tests
copying build/lib/package/tests/__init__.py -> build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages/package/tests
copying build/lib/package/tests/file.pyx -> build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages/package/tests
creating build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages/package/packagea
copying build/lib/package/packagea/__init__.py -> build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages/package/packagea
copying build/lib/package/__init__.py -> build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages/package
byte-compiling build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages/package/tests/__init__.py to __init__.cpython-39.pyc
byte-compiling build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages/package/packagea/__init__.py to __init__.cpython-39.pyc
byte-compiling build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages/package/__init__.py to __init__.cpython-39.pyc
running install_egg_info
Copying package.egg-info to build/bdist.linux-x86_64/dumb/home/milesg/miniconda3/envs/pyarrow-dev/lib/python3.9/site-packages/package-0.0.0-py3.9.egg-info
running install_scripts
creating /home/milesg/Projects/setuptools-exclude-ignored/dist
Creating tar archive
removing 'build/bdist.linux-x86_64/dumb' (and everything under it)
```
