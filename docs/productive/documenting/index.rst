Document
========

So that your product can be used effectively, documentation is required for the
target groups of data scientists and data engineers as well as for system
engineers:

* Data scientists want to see documented

  * which problems your product solves and what the main functions and
    limitations of the software are (``README``)
  * how the product can be used
  * which changes have come in more recent software versions (``CHANGELOG``)

* Data engineers want to know how troubleshooting can help improve the product
  (``CONTRIBUTING``) and how they can communicate with others
  (``CODE_OF_CONDUCT``)
* System engineers need installation instructions for your product and the
  required dependencies

Together, they all need information about how the product is licensed
(``LICENSE`` file or ``LICENSES`` folder and how they can get help if needed.

Badges are helpful in getting a quick overview of a product. For the
`cookiecutter-namespace-template
<https://github.com/veit/cookiecutter-namespace-template>`_ these are, for example:

|Downloads| |Updates| |Versions| |Contributors| |License| |Docs|

.. |Downloads| image:: https://static.pepy.tech/badge/cookiecutter-namespace-template
   :target: https://pepy.tech/project/cookiecutter-namespace-template
.. |Updates| image:: https://pyup.io/repos/github/veit/cookiecutter-namespace-template/shield.svg
   :target: https://pyup.io/repos/github/veit/cookiecutter-namespace-template/
.. |Versions| image:: https://img.shields.io/pypi/pyversions/cookiecutter-namespace-template.svg
   :target: https://pypi.org/project/cookiecutter-namespace-template/
.. |Contributors| image:: https://img.shields.io/github/contributors/veit/cookiecutter-namespace-template.svg
   :target: https://github.com/veit/cookiecutter-namespace-template/graphs/contributors
.. |License| image:: https://img.shields.io/github/license/veit/cookiecutter-namespace-template.svg
   :target: https://github.com/veit/cookiecutter-namespace-template/blob/main/LICENSE
.. |Docs| image:: https://readthedocs.org/projects/cookiecutter-namespace-template/badge/?version=latest
   :target: https://cookiecutter-namespace-template.readthedocs.io/en/latest/

For extensive documentation you can, for example, use `Sphinx
<https://www.sphinx-doc.org/>`_, a documentation tool that converts :doc:`rest`,
a simple markup language, into HTML or PDF, EPub and man pages. The Jupyter
tutorial was also created with Sphinx. To get a first impression of the Sphinx,
you can have a look at the source code of this page by following the link
`Sources <../../_sources/productive/sphinx/index.rst.txt>`_ folgt.

Originally, Sphinx was developed for the documentation of Python and is now used
in almost all Python projects, including `NumPy und SciPy
<https://docs.scipy.org/doc/>`_, `Matplotlib
<https://matplotlib.org/users/index.html>`_, `Pandas
<https://pandas.pydata.org/docs/>`_ and `SQLAlchemy
<https://docs.sqlalchemy.org/>`_.

The Sphinx `autodoc
<http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ feature,
which can be used to create documentation from Python :doc:`docstrings`, may
also  be conducive to the spread of Sphinx among Python developers. Overall,
Sphinx allows developers to create complete documentation in place. Often the
documentation is also stored in the same :doc:`Git <../git/index>` repository,
so that the creation of the latest software documentation remains easy.

Sphinx is also used in projects outside the Python community, e.g. for the
documentation of the Linux kernel: `Kernel documentation update
<https://lwn.net/Articles/705224/>`_.

`Read the Docs <https://readthedocs.org/>`_ was developed to forther simplify
documentation. Read the Docs makes it easy to create and publish documentation
after each commit.

.. seealso::
   * `Google developer documentation style guide
     <https://developers.google.com/style/>`_
   * `Google Technical Writing Courses for Engineers
     <https://developers.google.com/tech-writing/overview>`_
   * `Cusy-Design-System: Testen
     <https://cusy-design-system.readthedocs.io/de/latest/content/testing.html>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    start
    rest
    docstrings
    intersphinx
    extensions
