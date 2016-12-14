[rst](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html)
documentation for Nuage Networks [python
vspk](https://github.com/nuagenetworks/vspk-python)

This can be used to generate html documentation with
[sphinx](https://github.com/nuagenetworks/vspk-python). You'll need to install the theme too:

```
pip install sphinx_rtd_theme
```

To generate the html documentation:

```
sphinx-build -b html . build/html
```

For LaTeX:

```
sphinx-build -b latex . build/tex
```
