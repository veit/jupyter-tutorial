Intersphinx
===========

`sphinx.ext.intersphinx
<http://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_
allows the linking of other project documentation.

Configuration
-------------

In ``source/conf.py`` Intersphinx must be indicated as an extension:

.. code-block:: python

    extensions = [
        ...
        'sphinx.ext.intersphinx',
        ]

External Sphinx documentation can then be specified, e.g. with:

.. code-block:: python

    intersphinx_mapping = {
        'python': ('https://docs.python.org/3', None),
        'bokeh':  ('https://bokeh.pydata.org/en/latest/', None)
    }

However, alternative files can also be specified for an inventory, for example:

.. code-block:: python

    intersphinx_mapping = {
        'python': ('https://docs.python.org/3', (None, 'python-inv.txt'),
        ...
    }

Determine link targets
----------------------

To determine the links available in an inventory, you can enter the following,
for example:

.. code-block:: console

    $ python -m sphinx.ext.intersphinx https://docs.python.org/3/objects.inv
    c:function
        PyAnySet_Check                           c-api/set.html#c.PyAnySet_Check
        PyAnySet_CheckExact                      c-api/set.html#c.PyAnySet_CheckExact
        PyArg_Parse                              c-api/arg.html#c.PyArg_Parse
    …

Create a link
-------------

In order to link to https://docs.python.org/3/c-api/arg.html#c.PyArg_Parse, one
of the following variants can be specified:

:c:func:`PyArg_Parse`
    .. code-block:: rest

        :c:func:`PyArg_Parse`

:c:func:`!PyArg_Parse`
    .. code-block:: rest

        :c:func:`!PyArg_Parse`

:c:func:`Parsing arguments <PyArg_Parse>`
    .. code-block:: rest

        :c:func:`Parsing arguments <PyArg_Parse>`

Custom links
------------

You can also create your own ``intersphinx`` assignments, e.g. if
``objects.inv`` in `Beautiful Soup
<https://bugs.launchpad.net/beautifulsoup/+bug/1453370>`_ has errors.

The error can be corrected with:

#. Installation of ``sphobjinv``:

   .. code-block:: console

    $ pipenv install sphobjinv

#. Then the original file can be downloaded with:

   .. code-block:: console

    $ cd docs/build/
    $ mkdir _intersphinx
    $ !$
    $ curl -O https://www.crummy.com/software/BeautifulSoup/bs4/doc/objects.inv
    $ mv objects.inv bs4_objects.inv

#. Change the Sphinx configuration ``docs/source/conf.py``:

   .. code-block:: console

    intersphinx_mapping = {
        …
        'bs4':    ('https://www.crummy.com/software/BeautifulSoup/bs4/doc/', "_intersphinx/bs4_objects.inv")
    }

#. Convert to a text file:

   .. code-block:: console

    $ pipenv run sphobjinv convert plain bs4_objects.inv bs4_objects.txt

#. Editing the text file

   e.g.:

   .. code-block:: console

    bs4.BeautifulSoup           py:class  1 index.html#beautifulsoup -
    bs4.BeautifulSoup.get_text  py:method 1 index.html#get-text      -
    bs4.element.Tag             py:class  1 index.html#tag           -

   These entries can then be referenced in a Sphinx documentation with:

   .. code-block:: rest

    - :class:`bs4.BeautifulSoup`
    - :meth:`bs4.BeautifulSoup.get_text`
    - :class:`bs4.element.Tag`

   .. seealso::
      * `Sphinx objects.inv v2 Syntax
        <https://sphobjinv.readthedocs.io/en/latest/syntax.html>`_

#. Create a new ``objects.inv`` file:

   .. code-block:: console

        $ pipenv run sphobjinv convert zlib bs4_objects.txt bs4_objects.txt

#. Create Sphinx documentation:

   .. code-block:: console

        $ pipenv run sphinx-build -ab html source/ build/

Add roles
---------

If you get an error message that a certain text role is unknown, e.g.

.. code-block:: console

    WARNING: Unknown interpreted text role "confval".

so you can add them in the ``conf.py``:

.. code-block:: python

    def setup(app):
        # from sphinx.ext.autodoc import cut_lines
        # app.connect('autodoc-process-docstring', cut_lines(4, what=['module']))
        app.add_object_type(
            "confval",
            "confval",
            objname="configuration value",
            indextemplate="pair: %s; configuration value",
        )
