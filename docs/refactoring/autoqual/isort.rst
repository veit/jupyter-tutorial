``isort``
=========

`isort <https://github.com/timothycrosley/isort>`_ format eure
``imput``-Anweisungen in getrennte und sortierte Blöcke.

Installation
------------

.. code-block:: console

    $ pipenv install isort

Konfiguration
-------------

``isort`` lässt sich z.B. in der ``setup.cfg``-Datei konfigurieren:

.. code-block:: ini

    [isort]
    atomic=true
    force_grid_wrap=0
    include_trailing_comma=true
    lines_after_imports=2
    lines_between_types=1
    multi_line_output=3
    not_skip=__init__.py
    use_parentheses=true

    known_first_party=attr
    known_third_party=hypothesis,pytest,setuptools,six

Um Pakete von Drittanbietern gegenüber Ihren Projektimporten zu erkennen, könnt
ihr entweder euer Projekt zusammen mit ``isort`` installieren oder
`seed-isort-config <https://github.com/asottile/seed-isort-config>`_ verwenden.
