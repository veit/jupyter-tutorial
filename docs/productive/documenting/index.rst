Dokumentieren
=============

Damit Euer Produkt sinnvoll genutzt werden kann, sind Dokumentationen sowohl für
die Zielgruppen Daten-Wissenschaftler und Daten-Ingenieure als auch für
System-Ingenieure erforderlich:

* Daten-Wissenschaftler wollen dokumentiert sehen

  * welche Probleme Euer Produkt löst und was die Hauptfunktionen und
    Limitationen der Software sind (``README``)
  * wie das Produkt beispielhaft verwendet werden kann
  * welche Veränderungen in aktuelleren Software-Versionen gekommen sind
    (``CHANGELOG``)

* Daten-Ingenieure wollen wissen, wie sie mit Fehlerbehebungen zur Verbesserung
  des Produkts beitragen können (``CONTRIBUTING``) und wie sie mit anderen
  kommunizieren (``CODE_OF_CONDUCT``) können
* System-Ingenieure benötigen eine Installationsanleitung für Euer Produkt
  und der erforderlichen Abhängigkeiten

Alle gemeinsam benötigen Informationen, wie das Produkt lizenziert ist
(``LICENSE``-Datei oder ``LICENSES``-Ordner) und wie sie bei Bedarf Hilfe
erhalten können.

Um schnell einen Überblick übr ein Produkt zu erhalten, sind sog. Badges
hilfreich. Für das `cookiecutter-namespace-template
<https://github.com/veit/cookiecutter-namespace-template>`_ sind dies z.B.:

|Downloads| |Updates| |Versions| |Contributors| |License| |Docs|

.. |Downloads| image:: https://pepy.tech/badge/cookiecutter-namespace-template
   :target: https://pepy.tech/project/cookiecutter-namespace-template
.. |Updates| image:: https://pyup.io/repos/github/veit/cookiecutter-namespace-template/shield.svg
   :target: https://pyup.io/repos/github/veit/cookiecutter-namespace-template/
.. |Versions| image:: https://img.shields.io/pypi/pyversions/cookiecutter-namespace-template.svg
   :target: https://pypi.org/project/cookiecutter-namespace-template/
.. |Contributors| image:: https://img.shields.io/github/contributors/veit/cookiecutter-namespace-template.svg
   :target: https://github.com/veit/cookiecutter-namespace-template/graphs/contributors
.. |License| image:: https://img.shields.io/github/license/veit/cookiecutter-namespace-template.svg
   :target: https://github.com/veit/cookiecutter-namespace-template/blob/master/LICENSE
.. |Docs| image:: https://readthedocs.org/projects/cookiecutter-namespace-template/badge/?version=latest
   :target: https://cookiecutter-namespace-template.readthedocs.io/en/latest/

Für umfangreiche Dokuemtationen könnt Ihr z.B. `Sphinx
<http://www.sphinx-doc.org/>`_ verwenden, ein Dokumentationswerkzeug, das
:doc:`rest`, eine einfache Auszeichnungssprache, in HTML oder auch PDF,
EPub und Manpages umwandelt.
Den Quellcode dieser Seite könnt ihr euch anschauen unter `Sources
<../../_sources/productive/sphinx/index.rst.txt>`_. Ursprünglich wurde Sphinx
für die Dokumentation von Python entwickelt und wird heute auch in fast allen
Python-Projekten verwendet, u.a. für `NumPy und SciPy
<https://docs.scipy.org/doc/>`_, `Matplotlib
<https://matplotlib.org/users/index.html>`_, `Pandas
<https://pandas.pydata.org/pandas-docs/>`_ und `SQLAlchemy
<https://docs.sqlalchemy.org/>`_. 

Zur Verbreitung von Sphinx unter den Python-Entwicklern dürfte auch beigetragen
haben, dass Sphinx `autodoc
<http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_-Feature
auch aus Python :doc:`docstrings` Dokumentationen erzeugen kann.

Auch in Projekten außerhalb der Python-Community wird Sphinx
verwendet, z.B. für die Dokumentation des Linux Kernels: `Kernel documentation
update <https://lwn.net/Articles/705224/>`_. 

Um die Erstellung von Dokumentationen weiter zu vereinfachen, wurde
`Read the Docs <https://readthedocs.org/>`_ entwickelt. Read the Docs
vereinfacht das Erstellen und Veröffentlichen von Dokumentation nach jedem
*Commit*. 

.. seealso::
   * `Christina Czeschik und Matthias Lindhorst: Weniger schlecht über IT
     schreiben
     <https://www.oreilly.de/buecher/13079/9783960090632-weniger-schlecht-%C3%BCber-it-schreiben.html>`_
   * `Google Technical Writing Courses for Engineers
     <https://developers.google.com/tech-writing/overview>`_
   * `Eric Holscher: Testing your Documentation
     <http://www.writethedocs.org/guide/tools/testing/>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    start
    rest
    docstrings
    intersphinx
    extensions

