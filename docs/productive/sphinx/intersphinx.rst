Intersphinx
===========

`sphinx.ext.intersphinx
<http://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_
erlaubt die Verlinkung von anderen Projekt-Dokumentationen.

Konfiguration
-------------

In ``source/conf.py`` muss Intersphinx als Erweiterung angegeben werden:

.. code-block:: python

    extensions = [
        ...
        'sphinx.ext.intersphinx',
        ]

Anschließend können externe Sphinx-Dokumentationen angegeben werden, z.B. mit:

.. code-block:: python

    intersphinx_mapping = {
        'python': ('https://docs.python.org/3', None),
        'bokeh':  ('https://bokeh.pydata.org/en/latest/', None)
    }

Für ein Inventar können jedoch auch alternative Dateien angegeben werden, z.B.:

.. code-block:: python

    intersphinx_mapping = {
        'python': ('https://docs.python.org/3', (None, 'python-inv.txt'),
        ...
    }

Linkziele ermitteln
-------------------

Um die in einem Inventar zur Verfügung stehenden Links zu ermitteln, könnt Ihr
z.B. folgendes eingeben:

.. code-block:: console

    $ python -m sphinx.ext.intersphinx https://docs.python.org/3/objects.inv
    c:function
        PyAnySet_Check                           c-api/set.html#c.PyAnySet_Check
        PyAnySet_CheckExact                      c-api/set.html#c.PyAnySet_CheckExact
        PyArg_Parse                              c-api/arg.html#c.PyArg_Parse
    …

Link erstellen
--------------

Um nun z.B. auf https://docs.python.org/3/c-api/arg.html#c.PyArg_Parse zu 
verlinken, kann eine der folgenden Varianten angegeben werden:

:c:func:`PyArg_Parse`
    .. code-block:: rest

        :c:func:`PyArg_Parse`

:c:func:`!PyArg_Parse`
    .. code-block:: rest

        :c:func:`!PyArg_Parse`

:c:func:`Parsing arguments <PyArg_Parse>`
    .. code-block:: rest

        :c:func:`Parsing arguments <PyArg_Parse>`


Benutzerdefinierte Links
------------------------

Ihr könnt auch eigene ``intersphinx``-Zuordnungen erstellen, z.B. wenn
``objects.inv`` Fehler hat wie bei `Beautyfull Soup
<https://bugs.launchpad.net/beautifulsoup/+bug/1453370>`_.

Der Fehler kann behoben werden mit:

#. Installation von ``sphobjinv``:

   .. code-block:: console

    $ pipenv install sphobjinv

#. Anschließend kann die Originaldatei heruntergeladen werden mit:

   .. code-block:: console

    $ cd docs/build/
    $ mkdir _intersphinx
    $ !$
    $ curl -O https://www.crummy.com/software/BeautifulSoup/bs4/doc/objects.inv
    $ mv objects.inv bs4_objects.inv

#. Ändern der Sphinx-Konfiguration in ``docs/source/conf.py``:

   .. code-block:: console

    intersphinx_mapping = {
        …
        'bs4':    ('https://www.crummy.com/software/BeautifulSoup/bs4/doc/', "_intersphinx/bs4_objects.inv")
    }

#. Konvertieren in eine Textdatei:

   .. code-block:: console

    $ pipenv run sphobjinv convert plain bs4_objects.inv bs4_objects.txt

#. Editieren der Textdatei

   z.B.:

   .. code-block:: console

    bs4.BeautifulSoup           py:class  1 index.html#beautifulsoup -
    bs4.BeautifulSoup.get_text  py:method 1 index.html#get-text      -
    bs4.element.Tag             py:class  1 index.html#tag           -

   Diese Einträge lassen sich dann in einer Sphinx-Dokumentation referenzieren
   mit:

   .. code-block:: rest

    - :class:`bs4.BeautifulSoup`
    - :meth:`bs4.BeautifulSoup.get_text`
    - :class:`bs4.element.Tag`

   .. note::
      Beachtet dabei die `Sphinx objects.inv v2 Syntax
      <https://sphobjinv.readthedocs.io/en/latest/syntax.html>`_ dieser
      Textdateien.

#. Neue ``objects.inv``-Datei erstellen:

   .. code-block:: console

        $ pipenv run sphobjinv convert zlib bs4_objects.txt bs4_objects.txt

#. Sphinx-Dokumentation erstellen:

   .. code-block:: console

        $ pipenv run sphinx-build -ab html source/ build/

Rollen hinzufügen
-----------------

Wenn ihr eine Fehlermeldung erhaltet, dass eine bestimmte Textrolle unbekannt
sei, z.B. 

.. code-block:: console

    WARNING: Unknown interpreted text role "confval".

so könnt ihr diese in der ``conf.py`` hinzufügen:

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

