Create packages
===============

#. Notebooks are well suited for moving forward quickly, but when the code
   becomes more extensive, it is advisable to store stable code in packages.
#. You can use :ref:`pytest </productive/testing/ipytest.ipynb>` not only within
   your notebooks for testing, but also within your packages.
#. Use Clean Code principles with meaningful variable and function names, make
   meaningful comments and modularise the code.

   There are also tools that automatically apply coding styles such as `PEP 8
   <https://www.python.org/dev/peps/pep-0008/>`_ for Python. With
   :doc:`nbextensions/code_prettify/README_autopep8` you can not only apply this
   to your notebooks, but also to your Python packages, for example with `black
   <https://black.readthedocs.io/en/stable/>`_.

   For other languages ​​you can find overviews in `Awesome-Linters
   <https://awesome-linters.hugomartins.io/>`_ and `awesome-code-formatters
   <https://github.com/rishirdua/awesome-code-formatters>`_.

   You can automatically execute these tools with a pre-commit hock in front of
   every, ``git commit``, e.g. `mirrors-autopep8
   <https://github.com/pre-commit/mirrors-autopep8>`_, `pygrep-hooks
   <https://github.com/pre-commit/pygrep-hooks>`_ or `blacken-docs
   <https://github.com/asottile/blacken-docs>`_. You can get a good overview of
   available Git pre-commit hocks at `pre-commit.com
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
