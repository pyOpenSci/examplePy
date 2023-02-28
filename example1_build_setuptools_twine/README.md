# examplePy - setuptools example

This directory illustrates how to create a Python package using setuptools.

Optionally you can use `setuptools_scm` for versioning which shown in the 1b
directory of this GitHub repository.

Your build requirements for this setup should include:

```
# Build is your front end to build your package with the setuptools backend
build
# Twine publishes your package to PyPI (or test PyPI)
twine
```

Because setuptools is listed in your pyproject.toml file it will be installed
when your package is build. It will also install Wheel for you which you need
to create your package's wheel.

## Src Layout

This directory also uses a `src/` rather than a flat layout. You can read more
about why, here <TODO: link to packaging guide when current pr is merged>.

## pyproject toml metadata

### Build System specs

The build system here is setuptools which is your build backend. Because setuptools
does not have a default front end, you will use the [Build frontend](https://pypa-build.readthedocs.io/en/stable/) to build your package in this example.

```
[build-system]
requires = ["setuptools>=61.0.0", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"
```

## How to build this package

to build this package first install package requirements ideally in a virtual environment. Because this uses a src/ layout you must ensure that package.find
specifies the src/ directory in your pyproject.toml file :

```
[tool.setuptools.packages.find]
where = ["src"]
```

<todo - create tutorial on envs or link to one>

```bash
# Install package requirements
$ pip install -r requirements.txt
# Install stravalib in editable mode
$ pip install -e .
```

Now test out importing your package locally using a Python prompt (or in a
Jupyter notebook)):

```
>>> import examplePy.module1 as ep
>>> ep.add_values(1,2)
```

## Create the SDist and Wheel files

Then in your development environment run to build your packages :

```
python3 -m build
```

The `build` command will create your packages wheel and SDist in a directory
called `dist/`.

```
dist/
  examplePy-0.0.0-py3-none-any.whl
  examplePy-0.0.0.tar.gz
```

Once you have these files you can publish to PyPI

### How to Publish to PyPI

Once you have a build that your happy with, you can publish to pypi.
In this setuptools/build workflow you will use `twine` to publish.

To publish to test pypi use:
`twine upload -r testpypi dist/* `

To publish to PyPI use:

`twine upload dist/*`

This packaging example provides a bare bones setuptools example. In this example
your version tracking will either be manual OR using a tool such a bump version.

In another directory we will demonstrate setting up a package using setuptools_scm

## Learn more about pyOpenSci

[Learn more about us. ](https://www.pyopensci.org)
