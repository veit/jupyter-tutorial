reStructuredText
================

Quick guide
-----------

Den folgenden reStructuredText könnt ihr euch als HTML anschauen unter
 :doc:`rest-example`::

    Underline the title with punctuation marks
    ==========================================

    Change the punctuation mark for subtitles
    -----------------------------------------

    *Italic*, **bold** and ``preformatted``
    `hyperlink <http://en.wikipedia.org/wiki/Hyperlink>`_ `link`_

    .. _link: http://en.wikipedia.org/wiki/Link_(The_Legend_of_Zelda)
    .. image:: python-logo.png
    .. A comment block begins with two points and can be indented further

    A paragraph consists of one or more lines of non-indented text, separated
    from the material above and below by blank lines.

        »Block quotation marks look like paragraphs, but are indented with one
        or more spaces.«

    | Because of the pipe character, this becomes one line.
    | And this will be another line.

    term
      Definition of the term
    Different term
      …and its definition

    * Each entry in a list begins with an asterisk (or ``1.``,
      ``a.`` etc.).
    * List items can be displayed for multiple lines as long as the list items
      remain indented

    Blocks of code are introduced and indented with a colon::

        import docutils
        print help(docutils)

    >>> print 'But doctests start with ">>>" and don’t need to be indented.'


.. note::
   If the content of ``long_description`` in ``setuptools.setup()`` is written
   in reStructured Text, it is displayed as well-formatted HTML on the
   :term:`Python Package Index (PyPI)`.

.. seealso::
   * `reStructuredText Primer
     <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
   * `reStructuredText Quick Reference
     <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_

Directives
----------

reStructuredText can be expanded with `Directives
<https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_.
Sphinx makes extensive use of this. Here are some examples:

Table of Contents

    .. code-block:: rest

        .. toctree::
           :maxdepth: 2

           rest
           docstrings

    .. toctree::
       :maxdepth: 2

       rest
       docstrings

Meta information

    .. code-block:: rest

        .. sectionauthor:: Veit Schiele <veit@cusy.io>
        .. codeauthor:: Veit Schiele <veit@cusy.io>

    .. sectionauthor:: Veit Schiele <veit@cusy.io>
    .. codeauthor:: Veit Schiele <veit@cusy.io>

Code block

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

See also

    .. code-block:: rest

        .. seealso::
            `Sphinx Directives
            <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_

    .. seealso::
       `Sphinx Directives
       <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_

Glossary

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
