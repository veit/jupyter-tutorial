Sphinx-Projekt erstellen
========================

Installation und Start
----------------------

.. code-block:: console

    $ mkdir example
    $ cd !$
    cd example
    $ pipenv install sphinx
    Creating a virtualenv for this project…
    …
    $ pipenv run sphinx-quickstart docs
    Selected root path: docs
    > Separate source and build directories (y/n) [n]: y
    > Name prefix for templates and static dir [_]: 
    > Project name: my.package
    > Author name(s): Veit Schiele
    > Project release []: 1.0
    > Project language [en]: 
    > Source file suffix [.rst]: 
    > Name of your master document (without suffix) [index]: 
    > autodoc: automatically insert docstrings from modules (y/n) [n]: y
    > doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
    > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
    > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
    > coverage: checks for documentation coverage (y/n) [n]: 
    > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: 
    > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: 
    > ifconfig: conditional inclusion of content based on config values (y/n) [n]: 
    > viewcode: include links to the source code of documented Python objects (y/n) [n]: y
    > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: 
    > Create Makefile? (y/n) [y]: 
    > Create Windows command file? (y/n) [y]: 

    Creating file docs/source/conf.py.
    Creating file docs/source/index.rst.
    Creating file docs/Makefile.
    Creating file docs/make.bat.

Sphinx-Layout
-------------

::

    my.package
    ├── Pipfile
    └── docs
        ├── Makefile
        ├── _build
        ├── _static
        ├── _templates
        ├── conf.py
        ├── index.rst
        └── make.bat

``index.rst`` ist die initiale Datei für die Dokumentation, in der sich das
Inhaltsverzeichnis befindet. Das Inhaltsverzeichnis wird von euch erweitert
werden sobald ihr neue ``*.rst``-Dateien hinzufügt.

