# Pytfvars

![PyPI](https://img.shields.io/pypi/v/pytfvars?style=plastic)  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytfvars)
![GitHub](https://img.shields.io/github/license/hohoonsong/pytfvars) ![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/hohoonsong/pytfvars/Publish%20Python%20%F0%9F%90%8D%20distributions%20%F0%9F%93%A6%20to%20PyPI/release)

![PyPI - Downloads](https://img.shields.io/pypi/dm/pytfvars)

Convert python dictionary object to hcl syntax string.  
This is useful for manipulate with tfvars values with python.  
Use `python-hcl2` to load tfvars file and do something in your code then use this package to convert dictionary object to generate hcl syntax string.  
You can do write result string to tfvars file to trigger terraform plan.

## Document

https://hohoonsong.github.io/pytfvars/

## Install

`python3 -m pip install pytfvars -U`

OR

`pip3 install pytfvars`

## Usage

```python3
import hcl2
from pytfvars import tfvars

def load(file_path: str):
    with open(file_path, 'r') as fp:
        dict_tf_values = hcl2.load(fp)
        
    return dict_tf_values

def convert(dict_tf_values: dict):
    return tfvars.convert(dict_tf_values)


def do_something(dict_tf_values: dict):
    del dict_tf_values["key_to_delete"]
    dict_tf_values["add_something"] = "do_something"
    return dict_tf_values

```
## Core Concept
I wanted to make a web page which get input form and generate terraform resource with the values.  
I found some packages which load values from hcl file but none of this which do write hcl(tfvars) with python.  

## Release

### v1.0.0
initial release

### v1.0.1
fix README

## Contribute



