Underline the title with punctuation marks
==========================================

Change the punctuation mark for subtitles
-----------------------------------------

*Italic*, **bold** und ``preformatted``
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
