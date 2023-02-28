# Pure python meson example using PDM


## Requirements 
When combining `pdm` and `meson-python` install requirements become 
important. This is not clearly documented as far as I can tell.

## Build dependencies 

You will need to install the following dependencies to use these tools together. 

Build is needed if you want to run `python3 -m build` to build your project.
Ninja is needed for meson-python to run. 

# TODO create envt file for this?
```bash
conda install -c conda-forge pdm build meson-python ninja
```

NOTE: You can use pip to install all of these tools if you are a pip user! 

NOTE: PEP 517?? doesn't specify whether the front end of the back end need to be aware of the dist/ directory where your build outputs will bestored. As such there is a bug using meson-python and PDM. 
PDM by default cleans / deletes any dist/ directory and tries to place your 
SDist and wheel files in that directory. 

`Meson-Python` by default does not create that directory for you. 

An easy work around for this is: 

```bash
# Create a dist directory 
$ mkdir dist
# Now build your package  - by invoking the -no-clean flag, pdm will not remove 
# the directory that you created above. 
$ pdm build --no-clean
```

To build with meson run:
`python -m build`

## Build and install package in editable mode 

You can also install/build using pip. This creates a build using meson.

`pip install --no-build-isolation .`


Install the package from the whl. 
```bash
python -m pip install --no-deps dist/*.whl
```

## Environments 

PDM has several options for managing environments. 
One is following pep xxx it will create a __pypackgages__ directory. it will 
assume that the packages needed to build and install your package are in that 
local directory. However, you can also set the environment that you wish to 
use.

Below yo uuse pdm info to see what environment pdm is using. Notice that it is 
using the `__pypackages__` directory
```
➜ pdm info
PDM version:
  2.4.0
Python Interpreter:
  ../miniconda3/envs/pdm/bin/python3.9 (3.9)
Project Root:
  ../examplePy/example6_pdm_meson
Project Packages:
  ../examplePy/example6_pdm_meson/__pypackages__/3.9
```

```
➜ which python
../miniconda3/envs/pdm_meson/bin/python

➜ pdm use ../miniconda3/envs/pdm_meson/bin/python
Using Python interpreter: ../miniconda3/envs/pdm_meson/bin/python (3.9)
(pdm_meson) 

➜ pdm info
PDM version:
  2.4.0
Python Interpreter:
  .../miniconda3/envs/pdm_meson/bin/python (3.9)
Project Root:
  ../examplePy/example6_pdm_meson
Project Packages:
  None
```
## __pypackages__ PEP 582 

So i somehow told pdm to use pypackages and it definitely is getting confused 
bewteen using conda vs that directory. 

questions about pypackages 

* how does it interact (or not interact) with conda envts? (and pip)

## Managing deps 

When you add a dependency it also installed your package in editable mode. 
```bash 
❯ pdm add requests
Adding packages to default dependencies: requests
Inside an active virtualenv ../miniconda3/envs/pdm_meson, reusing it.
🔒 Lock successful
Changes are written to pdm.lock.
Changes are written to pyproject.toml.
All packages are synced to date, nothing to do.
Installing the project as an editable package...
  ✔ Install examplePy 0.1.00 successful

🎉 All complete!
```

Weird - it says it installed examplepy but it's not available via conda-list
```
UNKNOWN                       0.0.0       ../examplePy/example6_pdm_meson
```
unknown                   0.0.0                    pypi_0    pypi

It's definitely installing the package as "unknown". 
```python
>>> import pkg_resources
>>> installed_packages = pkg_resources.working_set
>>> installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
...    for i in installed_packages])
>>> print(installed_packages_list)
['blinker==1.5', 'brotlipy==0.7.0', 'build==0.7.0', 'cachecontrol==0.12.11', 'cached-property==1.5.2', 'certifi==2022.12.7', 'cffi==1.15.1', 'charset-normalizer==3.0.1', 'click==8.1.3', 'colorama==0.4.6', 'cryptography==38.0.4', 'distlib==0.3.6', 'filelock==3.9.0', 'findpython==0.2.2', 'idna==3.4', 'importlib-metadata==6.0.0', 'installer==0.6.0', 'lockfile==0.12.2', 'markdown-it-py==2.1.0', 'mdurl==0.1.0', 'meson-python==0.12.0', 'meson==1.0.0', 'msgpack==1.0.3', 'packaging==23.0', 'pdm-pep517==1.0.6', 'pdm==2.4.0', 'pep517==0.13.0', 'pip==22.3.1', 'platformdirs==2.6.2', 'pycparser==2.21', 'pygments==2.14.0', 'pyopenssl==23.0.0', 'pyproject-hooks==1.0.0', 'pyproject-metadata==0.6.1', 'pysocks==1.7.1', 'python-dotenv==0.21.1', 'requests-toolbelt==0.10.1', 'requests==2.28.2', 'resolvelib==0.9.0', 'rich==13.3.0', 'setuptools==65.6.3', 'shellingham==1.5.0.post1', 'tomli==2.0.1', 'tomlkit==0.11.6', 'typing-extensions==4.4.0', 'unearth==0.7.2', 'unknown==0.0.0', 'urllib3==1.26.14', 'virtualenv==20.17.1', 'wheel==0.37.1', 'zipp==3.11.0']

```
## Conda 

# remove envt 
conda remove --name pdm_meson --all

# Create envt 
conda create -n myenv python=3.9

# View packages in your python console
>>> import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
   for i in installed_packages])
print(installed_packages_list)


import os
print(os.environ['CONDA_DEFAULT_ENV'])