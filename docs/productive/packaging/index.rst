Pakete erstellen
================

#. Notebooks sind gut geeignet um schnell voranzukommen, doch bei umfangreicher
   werdendem Code empfiehlt sich, stabilen Code in Pakete auszulagern.
#. Ihr könnt :ref:`pytest </productive/testing/ipytest.ipynb>` nicht nur
   innerhalb Eurer Notebooks zum Testen verwenden, sondern auch innerhalb Eurer
   Pakete.
#. Verwendet `Clean Code <https://de.wikipedia.org/wiki/Clean_Code>`_-Prinzipien
   mit aussagekräftigen Variablen- und Funktionsnamen, kommentiert sinnvoll
   und modularisiert den Code.

   Es gibt auch Werkzeuge, die automatisch Coding-Styles anwenden wie z.B.
   `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ für Python. Mit
   :doc:`nbextensions/code_prettify/README_autopep8` könnt Ihr dies nicht nur
   auf Eure Notebooks anwenden, sondern z.B. mit `black
   <https://black.readthedocs.io/en/stable/>`_ auch auf Eure Python-Pakete.

   Für andere Sprachen findet Ihr Übersichten in `Awesome-Linters
   <https://awesome-linters.hugomartins.io/>`_ und `awesome-code-formatters
   <https://github.com/rishirdua/awesome-code-formatters>`_.

   Ihr könnt diese Werkzeuge mit einem Pre-Commit-Hock automatisch vor jedem
   ``git commit`` ausfähren, z.B. `mirrors-autopep8
   <https://github.com/pre-commit/mirrors-autopep8>`_, `pygrep-hooks
   <https://github.com/pre-commit/pygrep-hooks>`_ oder `blacken-docs
   <https://github.com/asottile/blacken-docs>`_. Eine gute Übersicht über
   verfügbare Git Pre-Commit-Hocks erhaltet Ihr auf `pre-commit.com
   <https://pre-commit.com/hooks.html>`_.

.. seealso::
   * `Python Application Layouts
     <https://realpython.com/python-application-layouts/>`_
   * `The Hitchhiker’s Guide to Python: Structuring Your Project
     <https://docs.python-guide.org/writing/structure>`_
   * `Poetry <https://python-poetry.org/>`_
   * `Python Modules <https://docs.python.org/3/tutorial/modules.html>`_
   * `Python Packaging <https://python-packaging.readthedocs.io/>`_

.. toctree::
   :hidden:

   example
   distribution
   upload-install
   binary-extensions
   templating/index
   next-steps
