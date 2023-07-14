``nbconvert``
=============

`nbconvert <https://nbconvert.readthedocs.io/en/latest/>`_
    converts notebooks to other formats

Installation
------------

.. code-block:: console

    $ pipenv install nbconvert

.. important::
    To be able to use all functions of ``nbconvert``, Pandoc and TeX
    (especially XeLaTeX) are required. These must be installed separately.

Install Pandoc
~~~~~~~~~~~~~~

``nbconvert`` uses `Pandoc <https://pandoc.org/>`_  to convert Markdown to
formats other than HTML.

.. tab:: Debian/Ubuntu

    .. code-block:: console

        $ sudo apt install pandoc

.. tab:: macOS

    .. code-block:: console

        $ brew install pandoc

Install Tex
~~~~~~~~~~~

For the conversion to PDF, ``nbconvert`` uses the Tex ecosystem in preparation:
A ``.tex`` file is created, which is converted into a PDF by the XeTeX engine.

.. tab:: Debian/Ubuntu

    .. code-block:: console

        $ sudo apt install texlive-xetex

.. tab:: macOS

    .. code-block:: console

        $ eval "$(/usr/libexec/path_helper)"
        $ brew install --cask mactex

    .. seealso::

        `MacTeX <https://tug.org/mactex/>`_

Use on the command line
-----------------------

.. code-block:: console

    $ jupyter nbconvert --to FORMAT mynotebook.ipynb

``latex``
    creates a ``NOTEBOOK_NAME.tex`` file and possibly images as PNG files in a
    folder. With ``--template`` you can choose between one of two templates:

    ``--template article``
        default

        Latex article, derived from the Sphinx how-to

    ``--template report``
        Latex report with table of contents and chapters

``pdf``
    creates a PDF over latex. Supports the same templates as ``latex``.

``slides``
    creates `Reveal.js <https://revealjs.com/>`_ slides.

``script``
    kconverts the notebook into an executable script. This is the easiest way to
    create a Python script or a script in another language.

    .. note::
        If a notebook contains *Magics*, then this can possibly only be carried
        out in one Jupyter session.

    We can for example convert
    :doc:`python4datascience:workspace/ipython/mypackage/foo` into a Python
    script with:

    .. code-block:: console

        $ pipenv run jupyter nbconvert --to script workspace/ipython/mypackage/foo.ipynb
        [NbConvertApp] Converting notebook docs/basics/ipython/mypackage/foo.ipynb to script
        [NbConvertApp] Writing 245 bytes to docs/basics/ipython/mypackage/foo.py

    The result is then :file:`foo.py` with:

    .. code-block:: python

        #!/usr/bin/env python
        # coding: utf-8

        # # `foo.ipynb`

        # In[1]:
        def bar():
            return "bar"

        # In[2]:
        def has_ip_syntax():
            listing = get_ipython().getoutput("ls")
            return listing

        # In[3]:
        def whatsmyname():
            return __name__

.. note::
    In order to assign notebook cells to slides, you should select
    :menuselection:`View --> Cell Toolbar --> Slideshow`. Then a menu is
    displayed in each cell at the top right with the options:
    :menuselection:`Slide, Sub-Slide, Fragment, Skip, Notes`.

.. note::
    Lecture notes require a local copy of ``reveal.js``. The following option
    can be specified so that ``nbconvert`` can find this: ``--reveal-prefix
    /path/to/reveal.js``.

Further details for ``FORMAT`` are ``asciidoc``, ``custom``, ``html``,
``markdown``, ``notebook``, and ``rst``.

nb2xls
------

`nb2xls <https://github.com/ideonate/nb2xls>`_ converts Jupyter notebooks into
Excel files (``.xlsx``) taking into account pandas DataFrames and Matplotlib
outputs. However, the input cells are not converted and only part of the
Markdown is converted.

Own exporters
-------------

.. seealso::
    `Customizing exporters
    <https://nbconvert.readthedocs.io/en/latest/external_exporters.html>`_
    allows you to write your own exporters.
