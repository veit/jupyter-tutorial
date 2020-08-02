Extensions
==========

Built-in Extensions
-------------------

`sphinx.ext.autodoc <http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
    Dokumentation aus Docstrings integrieren
`sphinx.ext.autosummary <http://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_
    generiert Zusammenfassungen von Funktionen, Methoden und Attributen
    aus Docstrings
`sphinx.ext.autosectionlabel <http://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html>`_
    referenziert Abchnitt unter Verwendung des Titels
`sphinx.ext.graphviz <http://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html>`_
    Rendering von `Graphviz <https://www.graphviz.org/>`_-Graphen
`sphinx.ext.ifconfig <http://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html>`_
    schließt Inhalte nur unter bestimmten Bedingungen ein
`sphinx.ext.intersphinx <http://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_
    erlaubt die Verlinkung von anderen Projekt-Dokumentationen
`sphinx.ext.mathjax <http://www.sphinx-doc.org/en/master/usage/extensions/math.html#module-sphinx.ext.mathjax>`_
    Rendering via JavaScript
`sphinx.ext.napoleon <http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_
    Support für NumPy- und Google-Style Docstrings
`sphinx.ext.todo <http://www.sphinx-doc.org/en/master/usage/extensions/todo.html>`_
    Unterstützung für ToDo-Items
`sphinx.ext.viewcode <http://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html>`_
    fügt Links zum Quellcode der Sphinx-Dokumentation hinzu

.. seealso::
   Einen vollständigen Überblick erhaltet ihr unter `Sphinx Extensions
   <http://www.sphinx-doc.org/en/master/usage/extensions/index.html>`_

Third-party Extensions
----------------------

`nbsphinx <https://nbsphinx.readthedocs.io/>`_
    Jupyter Notebooks in Sphinx
`jupyter-sphinx <https://github.com/jupyter-widgets/jupyter-sphinx>`_
    erlaubt das Rendering von Jupyter interactive widgets in Sphinx,
    s.a.

    `Embedding Widgets in the Sphinx HTML Documentation
    <https://ipywidgets.readthedocs.io/en/latest/embedding.html#embedding-widgets-in-the-sphinx-html-documentation>`_

`numpydoc <https://github.com/numpy/numpydoc>`_
    `NumPy <NumPy>`_’s Sphinx-Extension
`Releases <https://github.com/bitprophet/releases>`_
    schreibt eine Changelog-Datei
`sphinxcontrib-napoleon <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/>`_
    Napoleon ist ein Pre-Processor zum Parsen von NumPy- und Google-Style
    Docstrings
`Sphinx-autodoc-typehints <https://github.com/agronholm/sphinx-autodoc-typehints>`_
    Type hints-Support für die Sphinx autodoc-Extension
`sphinx-git <sphinx-git>`_
    `git <https://git-scm.com/>`_-Changelog for Sphinx
`sphinx-intl <https://pypi.python.org/pypi/sphinx-intl>`_
    Sphinx-Erweiterung für Übersetzungen
`sphinx-autobuild <https://github.com/GaretJax/sphinx-autobuild>`_
    überwacht ein Sphinx-Repository und erstellt eine neue Dokumentation
    sobald Änderungen gemacht wurden
`Sphinxcontrib-mermaid <https://github.com/mgaitan/sphinxcontrib-mermaid>`_
    erlaubt, Mermaid- Grafiken in Ihre Dokumente einbetten.

Eigene Extensions
-----------------

Lokale Erweiterungen in einem Projekt sollten relativ zur Dokumentation
angegeben werden. Hierfür wird in der Sphinx-Konfigurationsdatei
``docs/conf.py`` der entsprechende Pfad angegeben. Wenn eure Erweiterung
im Verzeichnis ``exts`` in der Datei ``foo.py`` liegt, dann wird in der
``conf.py`` folgendes eingetragen:

.. code-block:: python

    import sys
    import os
    sys.path.insert(0, os.path.abspath('exts'))

    extensions = [
    'foo',
    ...
    ]
