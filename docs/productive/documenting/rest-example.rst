Titel mit Satzzeichen  unterstreichen
=====================================

Wechselt für Untertitel das Satzzeichen
---------------------------------------

*Italic*, **fett** und ``vorformatiert``
`Hyperlink <https://en.wikipedia.org/wiki/Hyperlink>`_ `Link`_

.. _Link: https://en.wikipedia.org/wiki/Link_(The_Legend_of_Zelda)
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
