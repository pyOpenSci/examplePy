# pdm basic build examplePy 

* [PDM documentation](https://pdm.fming.dev/latest/)
* [Health:](https://snyk.io/advisor/python/pdm)

## Notes:

* PDM has all of the pieces of a potentially great front end
    * it can handle, versioning, build, push to pypi, has a nice init setup (with a few minor fixes it would be even better), dependencies and environments
* It handles environments in a super flexible way where ou can select the envt manager that you want to use 
* Because it supports PEP 517 - it allows you to swap out build back ends and aslo use pdm-build with other front ends that support 517 (in theory)
* ISSUE: there are so many settings an options for PDM and they are all presented up front. It would be more widely used I think if it had a get started page with 
    1) simple install instructions (it suggests curl?? why?)
    2) a simple get started - a flit like basic setup with basic options beginning to end. 
* There is no way a beginner would be able to digest the PDM documentation. i found myself bouncing around. at the same time is seems like a really great tool. 
* Docs say PDM can be used with any backend. If it worked with meson or scikit backends it could be perfect?? in terms of flexibility for extensions and more complex builds (but i need to ask folks who know more about complex builds)
* PDM has a healthy community that contributes but i'm not sure that there is more than a single real maintainer. 


## PDM would be easier to use if ...

* modify the landing page to have `pip` and `conda` installs in a get started. 
    * Specify why you might prefer installing using curl? 

* PDM really needs a simple get started to showcase the project. Right now the manage project section skips over using `pdm init`
Every tool should have a get started page that demonstrates basic functionality like flit does.

`pdm init` 
* Whats the diff between pdm-pep517 and pdm-backend when you select your desired back end build tool
* Could we have a list of license options like flit has in the `init` command?

* Suggested installation instructions are:
`curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -`


## Other features

* PEP 582 (opt in) `__pypackages__` dir with local envt
* Dependency management 
* Manages environments if you want it to 
* Pep 517 build backend so you can swap out other pep 517 compliant back ends
* Lots of plugins - https://github.com/pdm-project/awesome-pdm ! wow. 



## What is nice 

1. 
```
pdm init 
pdm  install # todo look at how it installs - it seems to install the entire envt
pdm build 
pdm publish
pdm publish -r  https://test.pypi.org/examplePy
```


## Install PDM

The suggested installation using `curl` is confusing.

`$ pip install pdm`

or  

`$ conda install -c conda-forge pdm`

### PDM install package deps

The install for pdm is heavier than flit but still speedy.

```bash
➜ conda create -n pdm-envt python=3.9
➜ conda activate pdm-envt
➜ pip install pdm
Collecting pdm
  Using cached pdm-2.4.0-py3-none-any.whl (205 kB)
Collecting unearth>=0.7
  Using cached unearth-0.7.2-py3-none-any.whl (39 kB)
Requirement already satisfied: certifi in /Users/leahawasser/opt/miniconda3/envs/pdm/lib/python3.9/site-packages (from pdm) (2022.12.7)
Collecting pyproject-hooks
  Using cached pyproject_hooks-1.0.0-py3-none-any.whl (9.3 kB)
Collecting shellingham>=1.3.2
  Using cached shellingham-1.5.0.post1-py2.py3-none-any.whl (9.4 kB)
Collecting tomlkit<1,>=0.11.1
  Using cached tomlkit-0.11.6-py3-none-any.whl (35 kB)
Collecting cachecontrol[filecache]>=0.12.11
  Using cached CacheControl-0.12.11-py2.py3-none-any.whl (21 kB)
Collecting resolvelib<0.10,>=0.9
  Using cached resolvelib-0.9.0-py2.py3-none-any.whl (16 kB)
Collecting requests-toolbelt
  Using cached requests_toolbelt-0.10.1-py2.py3-none-any.whl (54 kB)
Collecting importlib-metadata>=3.6
  Using cached importlib_metadata-6.0.0-py3-none-any.whl (21 kB)
Collecting packaging!=22.0,>=20.9
  Using cached packaging-23.0-py3-none-any.whl (42 kB)
Collecting findpython>=0.2.2
  Using cached findpython-0.2.3-py3-none-any.whl (18 kB)
Collecting installer<0.7,>=0.6
  Using cached installer-0.6.0-py3-none-any.whl (452 kB)
Collecting tomli>=1.1.0
  Using cached tomli-2.0.1-py3-none-any.whl (12 kB)
Collecting virtualenv>=20
  Using cached virtualenv-20.17.1-py3-none-any.whl (8.8 MB)
Collecting rich>=12.3.0
  Using cached rich-13.2.0-py3-none-any.whl (238 kB)
Collecting blinker
  Using cached blinker-1.5-py2.py3-none-any.whl (12 kB)
Collecting python-dotenv>=0.15
  Using cached python_dotenv-0.21.0-py3-none-any.whl (18 kB)
Collecting platformdirs
  Using cached platformdirs-2.6.2-py3-none-any.whl (14 kB)
Collecting requests
  Using cached requests-2.28.2-py3-none-any.whl (62 kB)
Collecting msgpack>=0.5.2
  Using cached msgpack-1.0.4-cp39-cp39-macosx_11_0_arm64.whl (69 kB)
Collecting lockfile>=0.9
  Using cached lockfile-0.12.2-py2.py3-none-any.whl (13 kB)
Collecting zipp>=0.5
  Using cached zipp-3.11.0-py3-none-any.whl (6.6 kB)
Collecting markdown-it-py<3.0.0,>=2.1.0
  Using cached markdown_it_py-2.1.0-py3-none-any.whl (84 kB)
Collecting pygments<3.0.0,>=2.6.0
  Using cached Pygments-2.14.0-py3-none-any.whl (1.1 MB)
Collecting filelock<4,>=3.4.1
  Using cached filelock-3.9.0-py3-none-any.whl (9.7 kB)
Collecting distlib<1,>=0.3.6
  Using cached distlib-0.3.6-py2.py3-none-any.whl (468 kB)
Collecting mdurl~=0.1
  Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Collecting idna<4,>=2.5
  Using cached idna-3.4-py3-none-any.whl (61 kB)
Collecting urllib3<1.27,>=1.21.1
  Using cached urllib3-1.26.14-py2.py3-none-any.whl (140 kB)
Collecting charset-normalizer<4,>=2
  Using cached charset_normalizer-3.0.1-cp39-cp39-macosx_11_0_arm64.whl (122 kB)
Installing collected packages: resolvelib, msgpack, lockfile, distlib, charset-normalizer, zipp, urllib3, tomlkit, tomli, shellingham, python-dotenv, pygments, platformdirs, packaging, mdurl, installer, idna, filelock, blinker, virtualenv, requests, pyproject-hooks, markdown-it-py, importlib-metadata, findpython, unearth, rich, requests-toolbelt, cachecontrol, pdm
Successfully installed blinker-1.5 cachecontrol-0.12.11 charset-normalizer-3.0.1 distlib-0.3.6 filelock-3.9.0 findpython-0.2.3 idna-3.4 importlib-metadata-6.0.0 installer-0.6.0 lockfile-0.12.2 markdown-it-py-2.1.0 mdurl-0.1.2 msgpack-1.0.4 packaging-23.0 pdm-2.4.0 platformdirs-2.6.2 pygments-2.14.0 pyproject-hooks-1.0.0 python-dotenv-0.21.0 requests-2.28.2 requests-toolbelt-0.10.1 resolvelib-0.9.0 rich-13.2.0 shellingham-1.5.0.post1 tomli-2.0.1 tomlkit-0.11.6 unearth-0.7.2 urllib3-1.26.14 virtualenv-20.17.1 zipp-3.11.0
(pdm) 
```

## Steps to build 

When you run `pdm init`, it creates a clean **pyproject.toml** file with all of the 
basic metadata (and a license if you chose).

I wish that pdm provided a list of license options like flit does. that seems like an easy add. PDM expects a 
user to know what option they want to use for license. 

PDM did ask me what envt I wanted to use which was nice! it found my pdm conda envt. 

```bash 
> pdm init
Creating a pyproject.toml for PDM...
Please enter the Python interpreter to use
0. /Users/leahawasser/opt/miniconda3/envs/pdm/bin/python (3.9)
1. /opt/homebrew/bin/python3.11 (3.11)
2. /opt/homebrew/bin/python3.10 (3.10)
3. /Users/leahawasser/opt/miniconda3/envs/pdm/bin/python3.9 (3.9)
4. /usr/bin/python3 (3.8)
Please select (0): 3
Using Python interpreter: /Users/leahawasser/opt/miniconda3/envs/pdm/bin/python3.9 (3.9)
Is the project a library that will be uploaded to PyPI [y/n] (n): y
Project name (example4_pdm): examplePy
Project version (0.1.0): 0.1.00
Project description (): The best package ever made.
Which build backend to use?
0. pdm-pep517
1. setuptools
2. flit
3. hatchling
4. pdm-backend
# Here i want to know the diff between pdm-pep517 and pdm-backend
Please select (0): 0     
# Here i wish there was a list of options like the backend options had and flit has for license   
License(SPDX name) (MIT): MIT
Author name (Leah Wasser): pyOpenSci
Author email (leah@pyopensci.org): email@email.com
Python requires('*' to allow any) (>=3.9): >=3.7
Changes are written to pyproject.toml.
Found following files from other formats that you may import:
0. /Users/leahawasser/Documents/GitHub/pyos/examplePy/example4_pdm/requirements.txt (requirements)
1. don't do anything, I will import later.
Please select: 0
Changes are written to pyproject.toml.
(pdm) 
```

## Project config 

pdm allows you to look at the project config at any time. This would be nice for 
a more advanced user. You can also change config settings both with the 
`pdm config` command and via the .toml config file 

NOTE: i'm confused about the `.pdm.toml` file - when i use that vs the pyproject.toml file. 

```
➜ pdm config
Site/default configuration (/Library/Preferences/pdm/config.toml):
build_isolation = True
cache_dir = /Users/leahawasser/Library/Caches/pdm
check_update = True
global_project.fallback = False
global_project.fallback_verbose = True
global_project.path = /Users/leahawasser/Library/Preferences/pdm/global-project
global_project.user_site = False
install.cache = False
install.cache_method = symlink
install.parallel = True
project_max_depth = 5
pypi.ignore_stored_index = False
pypi.json_api = False
pypi.url = https://pypi.org/simple
pypi.verify_ssl = True
python.use_pyenv = True
python.use_venv = True
strategy.resolve_max_rounds = 10000
strategy.save = minimum
strategy.update = reuse
theme.error = red
theme.info = blue
theme.primary = cyan
theme.req = bold green
theme.success = green
theme.warning = yellow
venv.backend = virtualenv
venv.in_project = True
venv.location = /Users/leahawasser/Library/Application Support/pdm/venvs
venv.prompt = {project_name}-{python_version}
venv.with_pip = False

Home configuration (/Users/leahawasser/Library/Preferences/pdm/config.toml):

Project configuration (/Users/leahawasser/Documents/GitHub/pyos/examplePy/example4_pdm/.pdm.toml):
python.path = /Users/leahawasser/opt/miniconda3/envs/pdm/bin/python3.9
```

```
➜ pdm info
PDM version:
  2.4.0
Python Interpreter:
  /Users/leahawasser/opt/miniconda3/envs/pdm/bin/python3.9 (3.9)
Project Root:
  /Users/leahawasser/Documents/GitHub/pyos/examplePy/example4_pdm
Project Packages: # this is the __pypackages__ dir if you have one
  None
```

```
➜ pdm info --env
{
  "implementation_name": "cpython",
  "implementation_version": "3.9.16",
  "os_name": "posix",
  "platform_machine": "arm64",
  "platform_release": "21.6.0",
  "platform_system": "Darwin",
  "platform_version": "Darwin Kernel Version 21.6.0: Sun Nov  6 23:31:13 PST 2022; 
root:xnu-8020.240.14~1/RELEASE_ARM64_T6000",
  "python_full_version": "3.9.16",
  "platform_python_implementation": "CPython",
  "python_version": "3.9",
  "sys_platform": "darwin"
}
```

## Install locally

To install locally, you'd use pdm install. it will install the entire environment 
I think it does install editable mode but it's not clear in the docs. 
There is an option to turn off editable mode which is why i suspect it by 
default installs in editable mode.  
```
pdm install
```


## Upload to PyPI 

`pdm publish`



`pdm list` works like `conda list`. 

## To build

`pdm build` 

```
➜ pdm build
Building sdist...
Built sdist at /Users/leahawasser/Documents/GitHub/pyos/examplePy/example4_pdm/dist/examplePy-0.1.0.tar.gz
Building wheel...
Built wheel at /Users/leahawasser/Documents/GitHub/pyos/examplePy/example4_pdm/dist/examplePy-0.1.0-py3-none-any.whl
(pdm) 
```

`pdm install`
i'm not sure if it's editable or not. 
 
`pdm publish`

## Versioning 

PDM has excellent support for multiple ways of managing versions. I think 
it covers all use cases that i've seen so far: 

* [it supports a setuptools_scm VCS based versioning](https://pdm.fming.dev/latest/pyproject/build/#dynamic-version-from-scm)
* but also supports a basic manual version 
* finally it has a plugin that operates like bumpversion that you could use 


## Dependency management 

PDM supports dependency mgt. you can tell it to use your reqruirements.txt as a 
base for expected dependencies. As you add deps it locks (without 
an upper bound).

```
➜ pdm add requests
Adding packages to default dependencies: requests
🔒 Lock successful
Changes are written to pdm.lock.
Changes are written to pyproject.toml.
Synchronizing working set with lock file: 60 to add, 0 to update, 0 to remove

  ✔ Install cycler 0.11.0 successful
  ✔ Install alabaster 0.7.13 successful
  ✔ Install defusedxml 0.7.1 successful
```

Output - notice requests is `>=`.

```bash
dependencies = [
    "nbsphinx",
    "pandoc",
    "sphinx-gallery",
    "pillow",
    "seaborn",
    "myst-parser",
    "furo",
    "requests>=2.28.2",
]
```

PDM then creates a lock file that you are supposed to add to your VCS.

```
# This file is @generated by PDM.
# It is not intended for manual editing.

[[package]]
name = "alabaster"
version = "0.7.13"
requires_python = ">=3.6"
summary = "A configurable sidebar-enabled Sphinx theme"
```
* deps can be updated with `pdm update`

Dependency management is highly configurable. 

## take aways 
The problem is that there are too many options and not clear 
get started docs. I think the options are excellent. So really it just needs 
a very very clear get started page so a user is't forced to make decisions 
early on that they are not ready to make. 

Experts will have no issues I think. It took me a while to nagivate around the 
docs to find what i needed. 

I bet documentation is why many don't use pdm. 


