# Example Python Package
This repository is an example package for Python. 
You can use it as a starting point if you want to distribute your software.

# Installation

## Instal from Remote Repository with pip and git
You can install the package using pip and git path (assuming you have git installed)

`pip install git+https://github.com/JakubSido/example_package.git`

## Install from Local Folder 
You can clone the repository (or download as zip and extract) and install this package from the package folder using

`pip install .`

note: You can also use -e (editable)
`pip install -e .`
for installing in editable mode. It means that if you pull the repo the local installation will update too. And that is great for the continuous development of software. You can use the package from other projects and stay up to date. 

Older Python than required (declared in example_package\pyproject.toml) leads to ERROR during installation. For example: 
`> ERROR: Package 'example-package' requires a different Python: 3.10.10 not in '>=3.12'`

# Using the package from python codes
If you want to use the package from your other projects, you have to follow some basics rules. Start with importing the package. If you want to expose some functionality, the standard way is to do so in `__init__.py` file.
See `example_package\src\example_package\__init__.py`

```python
import example_package

# Next line is ok because module counts is imported in __init__.py
print(example_package.counts.add_two(1))

# Following line is also ok, because add_one is imported from counts.py in __init__.py 
# Despite the fact that it is implemented in counts module. It is exposed in __init__.py 
print(example_package.add_two(1))

# Following line is not possible, because internal_counts is not in __init__.py
# print(example_package.internal_counts.add_two(1))


# Following line is ok, because internal_counts are imported explicitly here although not in __init__.py

import example_package.internal_counts
print(example_package.internal_counts.add_one(1))
```



# CLI - Command-line interface
Thanks to a simple mechanism, you can use your software from the command line on your machine after the installation. 

You can specify scripts to be accessible after the installation in 'pyproject.toml' 


```toml
[project.scripts]
expac = "example_package.cli:main"
```

This leads to the command 'expac' being accessible from the command line. In this project, it is mapped to the function main() defined in module cli.py in our package. This is great, we can use our software easily from everywhere :-) 

If we run 'expac' without any parameters, it prints help.

# Tests
Ensuring the reliability and functionality of your software is crucial. This package comes with a set of tests that you can run to validate its behavior. To execute the tests, use command `pytest` in the following command in the package folder (with pytest installed):

You should see similar output as follows 
``` 
D:\example_package>pytest
============================================================================================ test session starts ============================================================================================ 
platform win32 -- Python 3.12.2, pytest-8.1.1, pluggy-1.4.0
rootdir: D:\example_package
configfile: pyproject.toml
plugins: json-report-1.5.0, metadata-3.1.1, timeout-2.3.1
collected 2 items                                                                                                                                                                                             

tests\test_counts.py ..                                                                                                                                                                                [100%] 

============================================================================================= 2 passed in 0.02s =============================================================================================
```

