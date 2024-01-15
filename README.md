# Pytfvars

![PyPI](https://img.shields.io/pypi/v/pytfvars?style=plastic)  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytfvars)
![GitHub](https://img.shields.io/github/license/hohoonsong/pytfvars) ![GitHub Workflow Status (branch)](https://github.com/hohoonsong/pytfvars/actions/workflows/publish.yaml/badge.svg)

![PyPI - Downloads](https://img.shields.io/pypi/dm/pytfvars)

Convert python dictionary object to hcl syntax string.  
This is useful for manipulate with tfvars values with python.  
Use `python-hcl2` to load tfvars file and do something in your code then use this package to convert dictionary object to generate hcl syntax string.  
You can do write result string to tfvars file to trigger terraform plan.

## Document

[pytfvars](https://hohoonsong.github.io/pytfvars/docs/source/index.html)

## Install

`python3 -m pip install pytfvars -U`

OR

`pip3 install pytfvars`

## Usage

```python3
import hcl2
from pytfvars import tfvars

# use hcl2 to load tfvars file(or string)
def load(file_path: str):
    with open(file_path, 'r') as fp:
        dict_tf_values = hcl2.load(fp)
        
    return dict_tf_values

# convert dictionary to tfvars string
def convert(dict_tf_values: dict):
    return tfvars.convert(dict_tf_values)

# do some business logic
def do_something(dict_tf_values: dict):
    del dict_tf_values["key_to_delete"]
    dict_tf_values["add_something"] = "do_something"
    return dict_tf_values


if __name__ == '__main__':
    file_path = 'YOUR_FILE_PATH/sample.tfvars'
    
    # read file
    contents = load(file_path)
    # business logic
    contents_mod = do_something(contents)
    # convert
    contents_mod_str = convert(contents_mod)
    
    # write to tfvars file
    w_file_path = 'YOUR_FILE_PATH_TO/result.tfvars'
    with open(w_file_path, 'w') as fp:
        fp.write(contents_mod_str)
```
## Core Concept
I wanted to make a web page which get input form and generate terraform resource with the values.  
I found some packages which load values from hcl file but none of this which do write hcl(tfvars) with python.  

## Release

### v1.0.0
initial release

### v1.0.1
fix README

### v1.0.2
add indent to result string

## Contribute



