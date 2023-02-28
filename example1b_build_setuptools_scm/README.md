# examplePy - setuptools example

This directory illustrates how to create a Python package using setuptools.

Optionally you can use `setuptools_scm` for versioning which is also shown here.

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

to build this package first install package requirements ideally in a virtual environment

<todo - create tutorial on envs or link to one>

```bash
# Install package requirements
$ pip install -r requirements.txt
# Install stravalib in editable mode
$ pip install -e .
```

Then in your development environment run:

```
python3 -m build
```

Now test out the package:

```
>>> import examplePy.module1 as ep
>>> ep.add_values(1,2)
```

## Learn more about pyOpenSci

[Learn more about us. ](https://www.pyopensci.org)
