Check and improve code quality and complexity
=============================================

Before you start refactoring, you should measure the complexity of your code. In
the following, I would like to introduce you to some tools and concepts that
check the complexity of your code and simplify the maintenance and care of
Python packages and other source code. Often, together with
:doc:`/productive/git/pre-commit`, the code quality can also be checked and
improved automatically.

.. seealso::
   * `PyCQA Meta Documentation <https://meta.pycqa.org/>`_
   * `github.com/PyCQA <https://github.com/PyCQA>`_

Checker
-------

.. toctree::
   :maxdepth: 1

   flake8
   manifest
   mypy
   pytype
   wily
   pyre
   pysa

Formatter
---------

.. toctree::
   :maxdepth: 1

   black
   isort
   prettier

Refactoring
-----------

.. toctree::
   :maxdepth: 1

   anti-patterns
   rope.ipynb


.. seealso::
   * `Martin Fowler: Refactoring
     <https://www.mitp.de/IT-WEB/Software-Entwicklung/Refactoring.html>`_
