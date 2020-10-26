Extensions
==========

Built-in extensions
-------------------

`sphinx.ext.autodoc <http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
    Integrate documentation from docstrings
`sphinx.ext.autosummary <http://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_
    generates summaries of functions, methods and attributes from docstrings
`sphinx.ext.autosectionlabel <http://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html>`_
    references section using the title
`sphinx.ext.graphviz <http://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html>`_
    Rendering of `Graphviz <https://www.graphviz.org/>`_ graphs
`sphinx.ext.ifconfig <http://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html>`_
    includes content only under certain conditions
`sphinx.ext.intersphinx <http://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_
    allows the linking of other project documentation
`sphinx.ext.mathjax <http://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax>`_
    Rendering via JavaScript
`sphinx.ext.napoleon <http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_
    Support for NumPy and Google style docstrings
`sphinx.ext.todo <http://www.sphinx-doc.org/en/master/usage/extensions/todo.html>`_
    Support for ToDo items
`sphinx.ext.viewcode <http://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html>`_
    adds links to the source code of the Sphinx documentation

.. seealso::
   You can get a complete overview at `Sphinx Extensions
   <http://www.sphinx-doc.org/en/master/usage/extensions/index.html>`_

Third-party extensions
----------------------

`nbsphinx <https://nbsphinx.readthedocs.io/>`_
    Jupyter Notebooks in Sphinx
`jupyter-sphinx <https://github.com/jupyter-widgets/jupyter-sphinx>`_
    allows rendering of Jupyter interactive widgets in Sphinx, see also

    `Embedding Widgets in the Sphinx HTML Documentation
    <https://ipywidgets.readthedocs.io/en/latest/embedding.html#embedding-widgets-in-the-sphinx-html-documentation>`_

`numpydoc <https://github.com/numpy/numpydoc>`_
    `NumPy <NumPy>`_’s Sphinx extension
`Releases <https://github.com/bitprophet/releases>`_
    writes a changelog file
`sphinxcontrib-napoleon <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/>`_
    Napoleon is a pre-processor for parsing NumPy- and Google-style docstrings
`Sphinx-autodoc-typehints <https://github.com/agronholm/sphinx-autodoc-typehints>`_
    Type hints support for the Sphinx autodoc extension
`sphinx-git <sphinx-git>`_
    `git <https://git-scm.com/>`_-Changelog for Sphinx
`sphinx-intl <https://pypi.python.org/pypi/sphinx-intl>`_
    Sphinx extension for translations
`sphinx-autobuild <https://github.com/GaretJax/sphinx-autobuild>`_
    monitors a Sphinx repository and creates new documentation as soon as
    changes are made
`Sphinxcontrib-mermaid <https://github.com/mgaitan/sphinxcontrib-mermaid>`_
    allows you to embed Mermaid graphics in your documents.

Own Extensions
--------------

Local extensions in a project should be specified relative to the documentation.
The appropriate path is specified in the Sphinx configuration ``docs/conf.py``.
If your extension is in the directory ``exts`` in the file ``foo.py``, then the
``conf.py`` should look like this:

.. code-block:: python

    import sys
    import os
    sys.path.insert(0, os.path.abspath('exts'))

    extensions = [
    'foo',
    ...
    ]
