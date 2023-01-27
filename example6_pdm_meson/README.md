# Pure python meson example using PDM

TO build with `build` you need to install meson python 
`pip install meson-python`

To build with meson run:
`python -m build`

This creates a build using meson - to run this you need to have ninja installed in your envt. 
`pip install --no-build-isolation .`

`pdm build` doesn't work currently


```bash
python -m pip install --no-deps dist/*.whl
```
