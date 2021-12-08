Pysa
====

The Python Static Analyzer Pysa performs `taint
<https://en.wikipedia.org/wiki/Taint_checking>`_ analysis to identify potential
security problems. Pysa traces data streams from their origin to their endpoint
and identifies vulnerable code.

.. seealso::
   * `What Is Taint Analysis and Why Should I Care?
     <https://dzone.com/articles/what-is-taint-analysis-and-why-should-i-care>`_
   * `How Pysa works <https://pyre-check.org/docs/pysa-basics>`_
   * `Running Pysa <https://pyre-check.org/docs/pysa-running/>`_
   * `Pysa Tutorial <https://github.com/facebook/pyre-check/tree/master/documentation/pysa_tutorial>`_

Configuration
-------------

Pysa uses two file types for configuration:

* a ``taint.config`` file in JSON format, in which ``sources``, ``sinks``,
  ``features`` and ``rules`` are defined.

  .. code-block:: javascript

    {
      "comment": "UserControlled, Test, Demo sources are predefined. Same for Demo, Test and RemoteCodeExecution sinks",
      "sources": [],
      "sinks": [],
      "features": [],
      "rules": []
    }

* files with the extension ``.pysa`` in a directory configured with
  ``taint_models_path`` in your ``.pyre_configuration`` file.

You can find practical examples in the `Pyre repository
<https://github.com/facebook/pyre-check/tree/master/stubs/taint/core_privacy_security>`_.

Use
---

Pyre can be called, e.g. with

.. code-block:: console

    $ $ pipenv run pyre analyze --save-results-to ./

The  ``--save-results-to`` option stores detailed results in
``./taint-output.json``.

Pysa postprozessor
------------------

Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pipenv install fb-sapp

Use
~~~

#. Parsing the JSON file, e.g. with

   .. code-block:: console

    $ pipenv run sapp --database-name sapp.db analyze ./taint-output.json

   The results are stored in the local SQLite file ``sapp.db``.

#. Exploring the problems with

   .. code-block:: console

    $ pipenv run sapp --database-name sapp.db explore

   This starts an IPython interface connected to the SQLite database:

   ``issues``
    lists all issues
   ``issue 1``
    selects the first issue
   ``trace``
    shows the data flow from ``source`` to ``sink``
   ``n``
    jumps to the next call
   ``list``
    shows the source code of the call
   ``jump 1``
    jumps to the first call and shows the source code

Further commands can be found in `Commands
<https://pyre-check.org/docs/static-analysis-post-processor/#commands>`_.
