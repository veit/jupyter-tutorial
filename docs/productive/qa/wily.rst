Wily
====

The *Zen of Python* [#]_ emphasises complexity reduction in many ways:

    Simple is better than complex.

    Complex is better than complicated.

    Flat is better than nested.

Wily is a command line tool for checking the complexity of Python code in tests
and applications. For this purpose, Wily uses the following metrics:

`Cyclomatic complexity <https://en.wikipedia.org/wiki/Cyclomatic_complexity>`_
    measures the complexity of code by the number of linearly independent paths
    in the control flow graph.

    The Software Engineering Institute at Carnegie Mellon University
    distinguishes the following four levels of risk [#]_:

    +--------------------------------+--------------------------------+
    | Cyclomatic complexity          | Risk assessment                |
    +================================+================================+
    |  1–10                          | Simple programme without much  |
    |                                | risk                           |
    +--------------------------------+--------------------------------+
    | 11–20                          | moderate risk                  |
    +--------------------------------+--------------------------------+
    | 21–50                          | complex, high-risk programme   |
    +--------------------------------+--------------------------------+
    | > 50                           | untestable programme with very |
    |                                | high risk                      |
    +--------------------------------+--------------------------------+

`Halstead complexity measures <https://en.wikipedia.org/wiki/Halstead_complexity_measures>`_
    Statically analysing procedure that calculates the difficulty of the
    programme, the effort and the implementation time from the number of
    operators and operands.
Maintainability Index
    is based on the cyclomatic complexity, the Halstead complexity measures and
    the number of lines of code [#]_:

    +--------------------------------+--------------------------------+
    | Index                          | Maintainability                |
    +================================+================================+
    |  0–25                          | unmaintainable                 |
    +--------------------------------+--------------------------------+
    | 25–50                          | worrying                       |
    +--------------------------------+--------------------------------+
    | 50–75                          | in need of improvement         |
    +--------------------------------+--------------------------------+
    | 75–100                         | Superhero code                 |
    +--------------------------------+--------------------------------+

.. seealso::

   * `Docs <https://wily.readthedocs.io/en/latest/>`_
   * `GitHub <https://github.com/tonybaloney/wily>`_
   * `PyPI <https://pypi.org/project/wily/>`_
   * `wily-pycharm <https://github.com/tonybaloney/wily-pycharm>`_

Installation
------------

Wily can be easily installed with

.. code-block:: console

    $ pipenv install wily

You can then check the installation with

.. code-block:: console

    $ pipenv run wily --help
    Usage: wily [OPTIONS] COMMAND [ARGS]...
      Version: 1.19.0
      🦊 Inspect and search through the complexity of your source code. To get
      started, run setup:
        $ wily setup …

Configuration
-------------

A ``wily.cfg`` file can be created in the project directory with the list of
available operators:

.. code-block:: ini

    [wily]
    # list of operators, choose from cyclomatic, maintainability, mccabe and raw
    operators = cyclomatic,raw
    # archiver to use, defaults to git
    archiver = git
    # path to analyse, defaults to .
    path = /path/to/target
    # max revisions to archive, defaults to 50
    max_revisions = 20

Python code in ``.ipynb`` files is also usually recognised automatically.
However, you may be able to disable this for a Jupyter notebook with

.. code-block:: python

    ipynb_support = false

or for individual cells with

.. code-block:: python

    ipynb_cells = false

Use
---

… as a command line tool
~~~~~~~~~~~~~~~~~~~~~~~~

#. Building a cache with the statistics of the project

   .. note::
      Wily assumes that your project folder is a :doc:`Git
      <../../productive/git/index>` repository. However, Wily does not create a
      cache if the working directory is dirty.

   .. code-block:: console

        $ pipenv run wily build

#. Show metric

   .. code-block:: console

        $ pipenv run wily report

   This outputs both the metric and the delta to the previous revision.

#. Show ranking

   .. code-block:: console

        $ pipenv run wily rank

   This shows the ranking of all files in a directory or a single file based on
   the specified metric, if present in ``.wily/``.

#. Show graph

   .. code-block:: console

        $ pipenv run wily graph

   This displays a graph in the default browser.

#. Show build directory information

   .. code-block:: console

        $ pipenv run wily index

#. List the metrics available in the Wily operators

   .. code-block:: console

        $ pipenv run wily list-metrics

… as pre-commit hook
~~~~~~~~~~~~~~~~~~~~

You can also use Wily as a :doc:`pre-commit hook
<../../productive/git/pre-commit>`. To do this, you would have to add the
following to the ``pre-commit-config.yaml`` configuration file, for example:

.. code-block:: yaml

    repos:
    -   repo: local
        hooks:
        -   id: wily
            name: wily
            entry: wily diff
            verbose: true
            language: python
            additional_dependencies: [wily]

… in a CI/CD pipeline
~~~~~~~~~~~~~~~~~~~~~

Usually Wily compares the complexity with the previous revision. However, you
can also specify other references, for example ``HEAD^1`` with

.. code-block:: console

    $ pipenv run wily build src/
    $ pipenv run wily diff src/ -r HEAD^1

----

.. [#] `PEP 20 – The Zen of Python <https://www.python.org/dev/peps/pep-0020/>`_
.. [#] `C4 Software Technology Reference Guide, S. 147
       <https://resources.sei.cmu.edu/asset_files/Handbook/1997_002_001_16523.pdf>`_
.. [#] `Using Metrics to Evaluate Software System Maintainability
       <https://www.ecs.csun.edu/~rlingard/comp589/ColemanPaper.pdf>`_
