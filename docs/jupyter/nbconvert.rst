Jupyter Notebook Converter: ``nbconvert``
=========================================

`nbconvert <https://nbconvert.readthedocs.io/>`_ 
    konvertiert Notebooks in andere Formate

.. seealso::
    :doc:`/first-steps/install`: nbconvert ist Teil des Jupyter-Ökosystems.

Installation
------------

.. code-block:: console

    $ pipenv install nbconvert

.. important::
    Um alle Funktionen von nbconvert nutzen zu können, sind Pandoc und TeX
    (insbesondere XeLaTeX) erforderlich. Diese müssen separat installiert
    werden.

Pandoc installieren
~~~~~~~~~~~~~~~~~~~

nbconvert verwendet `Pandoc <http://pandoc.org/>`_ um Markdown in andere Formate
als HTML zu konvertieren. 

* für Ubuntu und Debian:

  .. code-block:: console

    $ sudo apt install pandoc

* für Mac OSX:

  .. code-block:: console

    $ brew install pandoc

Tex installieren
~~~~~~~~~~~~~~~~

Für die Konvertierung in PDF verwendet nbconvert das Tex-Ökosystem zur
Vorbereitung: Es wird eine ``.tex``-Datei erstellt, die von der XeTeX-Engine
in ein PDF konvertiert wird.

* für Ubuntu und Debian:

  .. code-block:: console

    $ sudo apt install texlive-xetex

* für Mac OSX:

  `MacTeX <http://tug.org/mactex/>`_

Verwenden auf der Kommandozeile
-------------------------------

.. code-block:: console

    $ jupyter nbconvert --to FORMAT mynotebook.ipynb

``latex``
    erzeugt eine Datei ``NOTEBOOK_NAME.tex`` und ggf. Bilder als PNG-Dateien in
    einem Ordner. Mit ``--template`` kann zwischen einem von zwei Vorlagen
    ausgewählt werden:

    ``--template article``
        Standard

        Latex-Artikel, abgeleitet aus dem How-To von Sphinx

    ``--template report``
        Latex-Bericht mit Inhaltsverzeichnis und Kapiteln

``pdf``
    erzeugt ein PDF über Latex. Unterstützt die gleichen Vorlagen wie ``latex``.

 ``slides``
    erstellt `Reveal.js <https://revealjs.com/>`_-Slides.

``script``
    konvertiert das Notebook in ein ausführbares Skript. Dies ist der einfachste
    Weg, ein Python-Skript oder ein Skript in einer anderen Sprache zu erzeugen.

    .. note::
        Enthält ein Notebook *Magics*, so können dies möglicherweise nur in einer
        Jupyter-Session ausgeführt werden.

    Wir können z.B. `docs/ipython/mypackage/foo.ipynb
    <../ipython/mypackage/foo.ipynb>`_ in ein Python-Skript verwandeln mit:

    .. code-block:: console

        $ pipenv run jupyter nbconvert --to script docs/basics/ipython/mypackage/foo.ipynb
        [NbConvertApp] Converting notebook docs/basics/ipython/mypackage/foo.ipynb to script
        [NbConvertApp] Writing 245 bytes to docs/basics/ipython/mypackage/foo.py

    Das Ergebnis ist dann ``foo.py`` mit:

    .. code-block:: python

        #!/usr/bin/env python
        # coding: utf-8

        # # `foo.ipynb`

        # In[1]:
        def bar():
            return "bar"

        # In[2]:
        def has_ip_syntax():
            listing = get_ipython().getoutput('ls')
            return listing

        # In[3]:
        def whatsmyname():
            return __name__

.. note::
    Um eine Zuordnung von Notebook-Cells zu Slides festzulegen, solltet ihr
    in :menuselection:`View --> Cell Toolbar --> Slideshow` auswählen.
    Daraufhin wird in jeder Zelle oben rechts ein Menü angezeigt mit den
    Optionen: :menuselection:`Slide, Sub-Slide, Fragment, Skip, Notes`.

.. note::
    Für Vortragsnotizen ist eine lokale Kopie von ``reveal.js``
    erforderlich. Damit nbconvert diese findet, kann folgende Option
    angegeben werden: ``--reveal-prefix /path/to/reveal.js``.

Weitere Angaben für ``FORMAT`` sind ``asciidoc``, ``custom``, ``html``,
``markdown``, ``notebook``, und ``rst``.

Eigene Exporter
---------------

.. seealso::
    `Customizing exporters
    <https://nbconvert.readthedocs.io/en/latest/external_exporters.html>`_
    erlaubt euch, eigene Exporter zu schreiben.

