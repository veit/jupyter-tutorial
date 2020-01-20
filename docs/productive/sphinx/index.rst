Dokumentation
=============

`Sphinx <http://www.sphinx-doc.org/>`_ ist ein Dokumentationswerkzeug, das
:doc:`rest`, eine einfache Auszeichnungssprache, in HTML oder auch PDF,
EPub und man pages umwandelt.
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
   `Eric Holscher: Testing your Documentation
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

