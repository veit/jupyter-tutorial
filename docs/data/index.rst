Read, persist and provide data
==============================

You can get an overview of public repositories with research data e.g. in

* `Registry of research data repositories (re3data) <https://www.re3data.org/>`_
* `Awesome Public Datasets
  <https://github.com/awesomedata/awesome-public-datasets>`_
* `Public APIs <https://github.com/public-apis/public-apis>`_
* `Machine learning datasets <https://www.datasetlist.com/>`_
* `Roboflow Computer Vision Datasets <https://public.roboflow.com/>`_
* `DBpedia <https://wiki.dbpedia.org/>`_
* `World Health Data Platform/Global Health Observatory
  <https://www.who.int/data/gho/>`_
* `UNICEF Data <https://data.unicef.org/>`_
* `World Bank Open Data <https://data.worldbank.org/>`_
* `EU Open Data Portal Data <>http://open-data.europa.eu/en/data/`_
* `US Census Bureau <https://www.census.gov/data.html>`_
* `data.gov <https://www.data.gov/>`_
* `Google Dataset Search <https://datasetsearch.research.google.com/>`_
* `Google Public Data Search <https://www.google.com/publicdata/directory>`_
* `Registry of Open Data on AWS <https://registry.opendata.aws/>`_
* `Yelp Open Dataset <https://www.yelp.com/dataset>`_
* `Kaggle Datasets <https://www.kaggle.com/datasets>`_
* `OpenDataMonitor
  <https://opendatamonitor.eu/frontend/web/index.php?r=dashboard%2Findex>`_
* `Open Data Impact Map <https://opendataimpactmap.org/>`_
* `CKAN <https://ckan.org/>`_
* `UC Irvine Machine Learning Repository
  <https://archive.ics.uci.edu/ml/index.php>`_
* `Hugging Face Datasets <https://github.com/huggingface/datasets>`_
* `Dataverse Project <https://dataverse.org/>`_
* `Open Data Kit <https://opendatakit.org/>`_
* `LODUM University of Münster‘s Open Data initiative
  <https://www.uni-muenster.de/LODUM/>`_
* `freeCodeCamp open-data <https://github.com/freeCodeCamp/open-data>`_
* `Reddit Datasets Community <https://www.reddit.com/r/datasets/>`_

In addition to specific Python libraries for accessing :ref:`remote storage
media </data/overview.rst#remote-storage-media>` and
:ref:`/data/overview.rst#geodata`, we will introduce you to different
:doc:`serialisation formats <serialisation-formats/index>` and three tools in
more detail that make data accessible:

* :doc:`requests/index`
* :doc:`beautifulsoup`
* :doc:`intake/index`

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

For the storage of other data types we introduce you to different
:doc:`NoSQL databases and concepts <nosql/index>`.

With :doc:`fastapi/index` we show you a way to provide data with a REST server.

With :doc:`DVC <../productive/dvc/index>` we present you a tool that allows data
provenance, i.e. the traceability of the origin of the data and the way they are
created.

Finally in the next chapter you will learn some good practices and helpful
Python packages to :doc:`clean up and validate data <../clean-prep/index>`.

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
