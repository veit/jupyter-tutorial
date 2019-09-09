``nbsphinx``
============

:doc:`nbsphinx <nbsphinx:index>` ist eine :doc:`Sphinx
<sphinx:contents>`-Erweiterung, die einen Parser für ``*.ipynb``-Dateien
bereitstellt: Jupyter Notebook-Code-Zellen werden sowohl in der HTML- wie auch
in der LaTeX-Ausgabe angezeigt. Notebooks ohne gespeicherte Ausgabezellen werden
automatisch während des Sphinx-Build-Prozesses erstellt.

Installation
------------

.. code-block:: console

    $ pipenv install sphinx nbsphinx

Requirements
~~~~~~~~~~~~

* :doc:`nbconvert`

Konfiguration
-------------

Sphinx konfigurieren
~~~~~~~~~~~~~~~~~~~~

#. Erstellen einer Dokumentation mit Sphinx:

   .. code-block:: console

    $ pipenv run python3 -m sphinx.cmd.quickstart

#. Danach befindet sich im neu erstellten Verzeichnis die
   Sphinx-Konfigurationsdatei ``conf.py``. In dieser  wird ``nbsphinx`` als
   Erweiterung hinzugefügt und generierte Notebooks ausgeschlossen:

   .. code-block:: python

    extensions = [
        ...
        'nbsphinx',
    ]
    ...
    exclude_patterns = [
        ...
        '**/.ipynb_checkpoints',
    ]

   Ein Beispiel findet ihr in der `conf.py
   <https://github.com/veit/jupyter-tutorial/blob/master/docs/conf.py>`_-Datei
   des Jupyter-Tutorials.

Ihr könnt noch weitere Konfigurationen für ``nbsphinx`` vornehmen.

Timeout
    In der Standardeinstellung von ``nbsphinx`` ist der Timeout für eine Zelle
    auf 30 Sekunden eingestellt. Ihr könnt dies für euer Sphinx-Projekt in der
    ``conf.py``-Datei ändern mit

    .. code-block:: python

        nbsphinx_timeout = 60

    Alternativ könnt ihr dies auch für einzelne Code-Zellen in den Metadaten der
    Code-Zelle angeben:

    .. code-block:: json

     {
      "cells": [
       {
        "cell_type": "markdown",
        "nbsphinx": {
          "timeout": 60
        },
       }
      ],
     }

    Soll das Timeout deaktiviert werden, kann ``-1`` angegeben werden.

Benutzerdefinierte Formate
    Bibliotheken wie z.B. `jupytext <https://github.com/mwouts/jupytext>`_
    speichern Notebooks in anderen Formaten ab, z.B. als *R-Markdown* mit dem
    Suffix ``Rmd``. Damit diese von ``nbsphinx`` ebnefalls ausgeführt werden
    können, können in der Sphinx-Konfigurationsdatei ``conf.py`` mit
    ``nbsphinx_custom_formats`` weitere Formate angegeben werden, z.B.

        .. code-block:: python

            import jupytext

            nbsphinx_custom_formats = {
                '.Rmd': lambda s: jupytext.reads(s, '.Rmd'),
            }

Zellen konfigurieren
~~~~~~~~~~~~~~~~~~~~

Zelle nicht anzeigen
    .. code-block:: json

     {
      "cells": [
       {
        "cell_type": "markdown",
        "metadata": {
         "nbsphinx": "hidden"
        },
       }
      ],
     }

``nbsphinx-toctree``
    Mit dieser Anweisung könnt ihr innerhalb einer Notebook-Zelle von Sphinx ein
    Inhaltsverzeichnis erstellen lassen, z.B.

    .. code-block:: json

     {
      "cells": [
       {
        "cell_type": "markdown",
        "metadata": {
         "nbsphinx-toctree": {
           "maxdepth": 2
         }
        "source": [
         "Der folgende Titel wird als ``toctree caption`` gerendert.\n",
         "\n",
         "## Inhalt\n",
         "\n",
         "[Ein Notebook](ein-notebook.ipynb)\n",
         "\n",
         "[Ein externer HTML-Link](https://jupyter-tutorial.readthedocs.io/)\n",
        ]
        },
       }
      ],
     }

    Weitere Optionen findet ihr in der :label:`Sphinx-Dokumentation
    <sphinx:toctree-directive>`.

Build
-----

#. Nun könnt ihr im Inhaltsverzeichnis eurer ``index.rst``-Datei eure
   ``*.ipynb``-Datei hinzufügen, siehe z.B. `jupyter-tutorial/ipython/index.rst
   <https://jupyter-tutorial.readthedocs.io/de/latest/_sources/ipython/index.rst.txt>`_. 

#. Schließlich könnt ihr die Seiten generieren, z.B. HTML mit

   .. code-block:: console

    $ pipenv run python3 -m sphinx <source-dir> <build-dir>

   oder

   .. code-block:: console

    $ pipenv run python3 -m sphinx <source-dir> <build-dir> -j <number-of-processes>

   wobei ``-j`` die Zahl der Prozesse angibt, die parallel ausgeführt werden
   sollen.

   Wenn ihr eine LaTeX-Datei erzeugen wollt, könnt ihr dies mit

   .. code-block:: console

    $ pipenv run python3 -m sphinx <source-dir> <build-dir> -b latex

#. Alternativ könnt ihr euch mit ``sphinx-autobuild`` die Dokumentation auch
   automatisch generieren lassen. Es kann installiert werden it

   .. code-block:: console

    $ pipenv run python3 -m pip install sphinx-autobuild

   Anschließend kann die automatische Erstellung gestartet werden mit

   .. code-block:: console

    $ pipenv run python3 -m sphinx_autobuild <source-dir> <build-dir>

   Dadurch wird ein lokaler Webserver gestartet, der die generierten HTML-Seiten
   unter ``http://localhost:8000/`` bereitstellt. Und jedes Mal, wenn ihr
   Änderungen in der Sphinx-Dokumentation speichert, werden die entsprechenden
   HTML-Seiten neu generiert und die Browseransicht aktualisiert.

   Ihr könnt dies auch nutzen, um die LaTeX-Ausgabe automatisch zu erstellen:

   .. code-block:: console

    $ pipenv run python3 -m sphinx_autobuild <source-dir> <build-dir> -b latex

#. Eine andere Alternative ist die Publikation auf `readthedocs.org
   <https://readthedocs.org/>`_.

   Hierfür müsst ihr  zunächst ein Konto unter https://readthedocs.org/
   erstellen und dann euer GitLab-, Github- oder Bitbucket-Konto verbinden.

Markdown-Zellen
~~~~~~~~~~~~~~~

Gleichungen
    Gleichungen können *inline* zwischen ``$``-Zeichen angegeben werden, z.B.

    .. code-block:: latex

        $\text{e}^{i\pi} = -1$

    Und auch zeilenweise können Gleichungen ausgedrückt werden z.B.

    .. code-block:: latex

        \begin{equation}
        \int\limits_{-\infty}^\infty f(x) \delta(x - x_0) dx = f(x_0)
        \end{equation}

    .. seealso::
        * `Equation Numbering
          <https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/equation-numbering/readme.html>`_

Zitate
    ``nbsphinx`` unterstützt dieselbe Syntax für Zitate wie `nbconvert
    <https://nbconvert.readthedocs.io/en/latest/latex_citations.html>`_:

    .. code-block:: html

        <cite data-cite="kluyver2016jupyter">Kluyver et al. (2016)</cite>

Info- und Warnboxen
    .. code-block:: html

        <div class="alert alert-info">
        **Note:** This is a note!
        </div>

Links zu anderen Notebooks

    .. code-block:: md

        a link to a notebook in a subdirectory](subdir/notebook-in-a-subdir.ipynb)

Links zu ``*.rst``-Dateien

    .. code-block:: md

        [reStructuredText file](rst-file.rst)

Links zu lokalen Dateien

    .. code-block:: md

        [Pipfile](Pipfile)

Code-Zellen
~~~~~~~~~~~

Javascript
    Für das generierte HTML kann Javascript verwendet werden, z.B.:

    .. code-block:: javascript

        %%javascript

        var text = document.createTextNode("Hello, I was generated with JavaScript!");
        // Content appended to "element" will be visible in the output area:
        element.appendChild(text);

