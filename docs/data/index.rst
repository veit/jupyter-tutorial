Read, persist and provide data
==============================

You can get an overview of public repositories with research data e.g. in the
`Registry of research data repositories (re3data) <https://www.re3data.org/>`_.

In addition to specific Python libraries for accessing :ref:`remote storage
media</data-rw/overview.rst#remotestorage-media>` and
:ref:`/data-rw/overview.rst#geodata`, we will introduce you to different
:doc:`serialisation-formats` and four tools in more detail:

* :doc:`requests/index`
* :doc:`beautifulsoup`
* :doc:`intake/index`
* :doc:`DVC <../productive/dvc/index>`

.. seealso::
    `pandas I/O API <https://pandas.pydata.org/docs/user_guide/io.html>`_
        The pandas I/O API is a set of top level ``reader`` functions that
        return a  pandas object. In most cases corresponding ``write`` methods
        are also available.
    `Scrapy <https://scrapy.org/>`_
        Framework for extracting data from websites as JSON, CSV or XML files.
    `Pattern <https://github.com/clips/pattern>`_
        Python module for data mining, natural language processing, ML and
        network analysis.
    `Web Scraping Reference <https://blog.hartleybrody.com/web-scraping-cheat-sheet/#javascript-heavy-websites>`_
        Overview of web scraping with Python.

We introduce :doc:`postgresql/index`, :doc:`postgresql/sqlalchemy` and
:doc:`postgresql/postgis/index` for storing relational data, Python objects and
geodata.

To clean up and prepare the data, we present you some best practices and helpful
Python packages in Data  :doc:`../clean-prep/index`.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    serialisation-formats/index
    requests/index
    beautifulsoup
    intake/index
    postgresql/index
    nosql/index
    fastapi/index
    glossary
