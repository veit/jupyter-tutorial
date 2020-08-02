reStructuredText
================

Kurzanleitung
-------------

Den folgenden reStructuredText könnt ihr euch als HTML anschauen unter
 :doc:`rest-example`::

    Titel mit Satzzeichen  unterstreichen
    =====================================

    Wechselt für Untertitel das Satzzeichen
    ---------------------------------------

    *Italic*, **fett** und ``vorformatiert``
    `Hyperlink <http://en.wikipedia.org/wiki/Hyperlink>`_ `Link`_

    .. _Link: http://en.wikipedia.org/wiki/Link_(The_Legend_of_Zelda)
    .. image:: python-logo.png
    .. Ein Kommentarblock beginnt mit zwei Punkten und kann weiter eingerückt
       werden.

    Ein Absatz besteht aus einer oder mehreren Zeilen mit nicht eingerücktem
    Text, getrennt aus dem Material oben und unten durch Leerzeilen.

        »Block-Anführungszeichen sehen aus wie Absätze, sind aber eingerückt mit
        einem oder mehreren Leerzeichen.«

    | Aufgrund des Pipe-Zeichens wird dies zu einer Zeile.
    | Und dies wird eine andere Zeile werden.

    Begriff
      Definition für den Begriff
    Anderer Begriff
      …und seine Definition

    * Jeder Eintrag in einer Liste beginnt mit einem Sternchen (oder ``1.``,
      ``a.`` usw.).
    * Listenelemente können für mehrere Zeilen angezeigt werden, solange die
      Listenelemente eingerückt bleiben

    Codeblöcke werden mit einem Doppelpunkt eingeführt und eingerückt::

        import docutils
        print help(docutils)

    >>> print 'Aber doctests beginnen mit ">>>" und brauchen keine Einrückung.'


.. note::
   Wenn der Inhalt von ``long_description`` in
   ``setuptools.setup()`` in reStructured Text geschrieben ist, wird es im
   :term:`Python Package Index (PyPI)` als wohlformattiertes HTML
   ausgegeben.

.. seealso::
   * `reStructuredText Primer
     <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
   * `reStructuredText Quick Reference
     <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_

Direktiven
----------

reStructuredText lässt sich durch sog. `Directives
<http://docutils.sourceforge.net/docs/ref/rst/directives.html>`_ erweitern.
Hiervon macht Sphinx umfassend Gebrauch. Hier einige Beispiele:

Inhaltsverzeichnis

    .. code-block:: rest

        .. toctree::
           :maxdepth: 2

           rest
           docstrings

    .. toctree::
       :maxdepth: 2

       rest
       docstrings

Meta-Informationen

    .. code-block:: rest

        .. sectionauthor:: Veit Schiele <veit@cusy.io>
        .. codeauthor:: Veit Schiele <veit@cusy.io>

    .. sectionauthor:: Veit Schiele <veit@cusy.io>
    .. codeauthor:: Veit Schiele <veit@cusy.io>

Code-Block

    .. code-block:: rest

        .. code-block:: python
           :emphasize-lines: 3,5

           def some_function():
               interesting = False
               print 'This line is highlighted.'
               print 'This one is not...'
               print '...but this one is.'

    .. code-block:: python
       :emphasize-lines: 3,5

       def some_function():
           interesting = False
           print 'This line is highlighted.'
           print 'This one is not...'
           print '...but this one is.'

Siehe auch

    .. code-block:: rest

        .. seealso::
            `Sphinx Directives
            <http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_

    .. seealso::
       `Sphinx Directives
       <http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_

Glossar

    .. code-block:: rest

        .. glossary::

           environment
              A structure where information about all documents under the root is
              saved, and used for cross-referencing.  The environment is pickled
              after the parsing stage, so that successive runs only need to read
              and parse new and changed documents.

           source directory
              The directory which, including its subdirectories, contains all
              source files for one Sphinx project.

    .. glossary::

       environment
          A structure where information about all documents under the root is
          saved, and used for cross-referencing.  The environment is pickled
          after the parsing stage, so that successive runs only need to read
          and parse new and changed documents.

       source directory
          The directory which, including its subdirectories, contains all
          source files for one Sphinx project.
