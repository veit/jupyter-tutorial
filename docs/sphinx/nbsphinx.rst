``nbsphinx``
============

:doc:`nbsphinx <nbsphinx:index>` is a :doc:`Sphinx <sphinx:index>` extension
that provides a parser for :file:`*.ipynb` files: Jupyter Notebook code cells
are displayed in both HTML and LaTeX output. Notebooks with no output cells
saved are automatically created during the Sphinx build process.

Installation
------------

.. code-block:: console

    $ pipenv install sphinx nbsphinx

Requirements
~~~~~~~~~~~~

* :doc:`../nbconvert`

Configuration
-------------

Configure Sphinx
~~~~~~~~~~~~~~~~

#. Creating a documentation with Sphinx:

   .. code-block:: console

    $ pipenv run python -m sphinx.cmd.quickstart

#. The Sphinx configuration file :file:`conf.py` is then located in the newly
   created directory. In this, ``nbsphinx`` is added as an extension and
   notebook checkpoints are excluded:

   .. code-block:: python

    extensions = [
        ...
        "nbsphinx",
    ]
    ...
    exclude_patterns = [
        ...
        "**/.ipynb_checkpoints",
    ]

   You can find an example in the :download:`/conf.py` file of the Jupyter
   tutorial.

You can make further configurations for ``nbsphinx``.

Timeout
    In the standard setting of ``nbsphinx``, the timeout for a cell is set to 30
    seconds. You can change this for your Sphinx project in the  :file:`conf.py`
    file with :samp:`nbsphinx_timeout = {60}`.

    Alternatively, you can also specify this for individual code cells in the
    metadata of the code cell:

    .. code-block:: json

       {
        "cells": [
         {
          "cell_type": "markdown",
          "nbsphinx": {
            "timeout": 60
          }
         }
        ]
       }

    If the timeout is to be deactivated, ``-1`` can be specified.

Custom formats
    Libraries such as `jupytext <https://github.com/mwouts/jupytext>`_ save
    notebooks in other formats, for example as R-Markdown with the suffix
    ``Rmd``. So that these can also be executed by  ``nbsphinx``, further
    formats can be specified in the Sphinx configuration file :file:`conf.py`
    with ``nbsphinx_custom_formats``, for example

    .. code-block:: python

       import jupytext


       nbsphinx_custom_formats = {
           ".Rmd": lambda s: jupytext.reads(s, ".Rmd"),
       }

Configure cells
~~~~~~~~~~~~~~~

Don’t show cell
    .. code-block:: json

       {
        "cells": [
         {
          "cell_type": "markdown",
          "metadata": {
           "nbsphinx": "hidden"
          }
         }
        ]
       }

``nbsphinx-toctree``
    With this instruction Sphinx will create a table of contents within a
    notebook cell, for example

    .. code-block:: json

       {
        "cells": [
         {
          "cell_type": "markdown",
          "metadata": {
           "nbsphinx-toctree": {
             "maxdepth": 2
           },
          "source": [
           "The following title is rendered as ``toctree caption``.\n",
           "\n",
           "## Content\n",
           "\n",
           "[A notebook](a-notebook.ipynb)\n",
           "\n",
           "[An external HTML link](https://jupyter-tutorial.readthedocs.io/)\n"
          ]
          }
         }
        ]
       }

    Further options you will find in the :label:`Sphinx documentation
    <sphinx:toctree-directive>`.

Build
-----

#. Now you can add your ``*.ipynb`` file in the table of contents of your
   ``index.rst`` file, see for example
   `jupyter-tutorial/notebook/testing/index.rst
   <https://jupyter-tutorial.readthedocs.io/de/latest/_sources/notebook/testing/index.rst.txt>`_

#. Finally, you can generate the pages, for example HTML with :samp:`$ pipenv
   run python -m sphinx {SOURCE_DIR} {BUILD_DIR}` or :samp:`$ pipenv run python
   -m sphinx {SOURCE_DIR} {BUILD_DIR} -j NUMBER_OF_PROCESSES` where ``-j`` is
   the number of processes to run in parallel.

   If you want to create a LaTeX file, you can do so with :samp:`$ pipenv run
   python -m sphinx {SOURCE_DIR} {BUILD_DIR} -b latex`.

#. Alternatively, you can have the documentation generated automatically with
   ``sphinx-autobuild``. It can be installed with :samp:`$ pipenv run python -m
   pip install sphinx-autobuild`.

   The automatic creation can then be started with :samp:`$ pipenv run python -m
   sphinx_autobuild {SOURCE_DIR} {BUILD_DIR}`.

   This starts a local web server that provides the generated HTML pages at
   ``http://localhost:8000/``. And every time you save changes in the Sphinx
   documentation, the corresponding HTML pages are regenerated and the browser
   view is updated.

   You can also use this to automatically generate the LaTeX output: :samp:`$
   pipenv run python -m sphinx_autobuild {SOURCE_DIR} {BUILD_DIR} -b latex`.

#. Another alternative is publication on `readthedocs.org
   <https://readthedocs.org/>`_.

   To do this, you first have to create an account at https://readthedocs.org/
   and then connect your GitLab, Github or Bitbucket account.

Markdown cells
~~~~~~~~~~~~~~

Equations
    Equations can be specified *inline* between ``$`` characters, for example

    .. code-block:: latex

        $\text{e}^{i\pi} = -1$

    Equations can also be expressed line by line, for example

    .. code-block:: latex

        \begin{equation}
        \int\limits_{-\infty}^\infty f(x) \delta(x - x_0) dx = f(x_0)
        \end{equation}

    .. seealso::
        * `Equation Numbering
          <https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/equation-numbering/readme.html>`_

Quotes
    ``nbsphinx`` supports the same syntax for quotations as `nbconvert
    <https://nbconvert.readthedocs.io/en/latest/latex_citations.html>`_:

    .. code-block:: html

        <cite data-cite="kluyver2016jupyter">Kluyver et al. (2016)</cite>

Alert boxes
    .. code-block:: html

        <div class="alert alert-block alert-info">

        **Note**

        This is a notice!
        </div>

        <div class="alert alert-block alert-success">

        **Success**

        This is a success notice!
        </div>

        <div class="alert alert-block alert-warning">

        **Warning**

        This is a warning!
        </div>

        <div class="alert alert-block alert-danger">

        **Danger**

        This is a danger notice!
        </div>

Links to other notebooks
    .. code-block:: md

        a link to a notebook in a subdirectory](subdir/notebook-in-a-subdir.ipynb)

Links to ``*.rst`` files
    .. code-block:: md

        [reStructuredText file](rst-file.rst)

Links to local files
    .. code-block:: md

        [Pipfile](Pipfile)

Code cells
~~~~~~~~~~

Javascript
    Javascript can be used for the generated HTML, for example:

    .. code-block:: javascript

        %%javascript

        var text = document.createTextNode("Hello, I was generated with JavaScript!");
        // Content appended to "element" will be visible in the output area:
        element.appendChild(text);

Galleries
---------

nbsphinx provides support for `creating thumbnail galleries from a list of
Jupyter notebooks
<https://nbsphinx.readthedocs.io/en/0.9.2/subdir/gallery.html>`_. This
functionality is based on `Sphinx-Gallery <https://sphinx-gallery.github.io/>`_
and extends nbsphinx to work with Jupyter notebooks instead of Python scripts.

Sphinx-Gallery also directly supports :doc:`pyviz:matplotlib/index`,
:doc:`pyviz:matplotlib/seaborn/index` and `Mayavi
<https://docs.enthought.com/mayavi/mayavi/>`_.

Installation
~~~~~~~~~~~~

Sphinx-Gallery can be installed for Sphinx ≥ 1.8.3 with

.. code-block:: console

    $ pipenv install sphinx-gallery

Configuration
~~~~~~~~~~~~~

In order for Sphinx-Gallery to be used, it must also be entered into the
:file:`conf.py` file:

.. code-block:: python

   extensions = [
       "nbsphinx",
       "sphinx_gallery.load_style",
   ]

You can then use Sphinx-Gallery in two different ways:

#. With the reStructuredText directive ``.. nbgallery::``.

   .. seealso::
      `Thumbnail Galleries
      <https://nbsphinx.readthedocs.io/en/0.9.2/a-normal-rst-file.html#thumbnail-galleries>`_

#. In a Jupyter notebook, by adding an ``nbsphinx-gallery`` tag to the metadata
   of a cell:

   .. code-block:: javascript

      {
          "tags": [
              "nbsphinx-gallery"
          ]
      }
