# flit basic build examplePy 

* For pure Python projects only 
* Great option if you are just building a small module locally for use with no
 intentions of longer term maintenance. Or if you just want to publish to pypi quickly. 

* [Flit documentation](https://flit.pypa.io/en/stable/)

## What is nice 

1. Light weight install w simple deps
1. Streamlined, no nonsense  UI  
```
flit init 
flit install 
flit build 
flit publish
```
2. Simple quick startup
init and build check for things like 
* correct imports of your package 
* TOML format, url format etc 
* catches a lot of simple but common mistakes you might make 


## What is less nice  
* Wish that install editable was straight forward like `pip install -e` . symlink is something that would need explanation while `pip install -e` is something i'm used to using. I think symlink is the same as `install -e` but wish the syntax was the same for consistency. (cognitive load issue for beginners) <NOTE: there is an open issue about this on github>
* Doesn't support versioning - eg `flit bump major`


## Install flit

`$ pip install flit`

or  

`$ conda install -c conda-forge flit`

### Flit install package deps

The install for flit is light weight and fast. 
```bash
Collecting flit
  Using cached flit-3.8.0-py3-none-any.whl (49 kB)
Requirement already satisfied: requests in /Users/leahawasser/opt/miniconda3/lib/python3.9/site-packages (from flit) (2.27.1)
Collecting tomli-w
  Using cached tomli_w-1.0.0-py3-none-any.whl (6.0 kB)
Collecting flit_core>=3.8.0
  Using cached flit_core-3.8.0-py3-none-any.whl (62 kB)
Requirement already satisfied: docutils in /Users/leahawasser/opt/miniconda3/lib/python3.9/site-packages (from flit) (0.17.1)
Requirement already satisfied: idna<4,>=2.5 in /Users/leahawasser/opt/miniconda3/lib/python3.9/site-packages (from requests->flit) (3.3)
Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/leahawasser/opt/miniconda3/lib/python3.9/site-packages (from requests->flit) (2.0.4)
Requirement already satisfied: certifi>=2017.4.17 in /Users/leahawasser/opt/miniconda3/lib/python3.9/site-packages (from requests->flit) (2022.12.7)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/leahawasser/opt/miniconda3/lib/python3.9/site-packages (from requests->flit) (1.26.9)
Installing collected packages: tomli-w, flit-core, flit
Successfully installed flit-3.8.0 flit-core-3.8.0 tomli-w-1.0.0
```

## Steps to build 

When you run flit init, it creates a clean pyproject.toml file with all of the 
basic metadata (and a license if you chose)

```bash 
> flit init
Module name: examplePy
Author [law]: me myself and i
Author email [law@example.com]: me@email.com
Home page: pyopensci.org
Should start with http:// or https:// - try again.
Home page: https://pyopensci.org
Choose a license (see http://choosealicense.com/ for more info)
1. MIT - simple and permissive
2. Apache - explicitly grants patent rights
3. GPL - ensures that code based on this is shared with the same terms
4. Skip - choose a license later
Enter 1-4 [1]: 1

Written pyproject.toml; edit that file to add optional extra info.
```


## Upload to pypI 

`flit publish`

local install - i find these directions confusing as what is [--symlink]
I don't understand how to install in interactive mode based on the docs. 
```
flit install [--symlink] [--python path/to/python]
```


## Versioning 

Flit doesn't have any command support for versions. 

You update it yourself, manually. You can either manage it in the pyproject toml 
or set it to be "dynamic" (see below) if you want to update the __version__ 
file.

`If you want Flit to get the version from a __version__ attribute,`

```
[project]
name = "astcheck"
authors = [
    {name = "Thomas Kluyver", email = "thomas@kluyver.me.uk"},
]
readme = "README.rst"
classifiers = [
    "License :: OSI Approved :: MIT License",
]
requires-python = ">=3.5"
dynamic = ["version", "description"]
```

## User adds dependencies manually

```
dependencies = [
    "requests >=2.6",
    "configparser; python_version == '2.7'",
]
```


Flit supports entry points (TODO: don't fully understand what this would look like in a package)

https://flit.pypa.io/en/stable/pyproject_toml.html#scripts-section

## to build

`flit build` 


[you can customize what's in the sdist ](https://flit.pypa.io/en/stable/pyproject_toml.html#sdist-section)

```
[tool.flit.sdist]
include = ["doc/"]
exclude = ["doc/*.html"]
```

## Use with other back ends?

I'm not sure - if it is that simple and you need a diff back end i wonder why use it at all. might be best for small local modules or times when you just want to get something published but aren't invested in longer term maintenance?