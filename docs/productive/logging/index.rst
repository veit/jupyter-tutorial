Logging
=======

The `logging <https://docs.python.org/3/library/logging.html#module-logging>`_
module is part of the Python standard library. It is described in `PEP 0282
<https://www.python.org/dev/peps/pep-0282>`_. You can get a first introduction
to the module in the `Basic Logging Tutorial
<https://docs.python.org/3/howto/logging.html#logging-basic-tutorial>`_.

Logging usually serves two different purposes:

* Diagnosis:

  * You can display the context of certain events.
  * Tools like `Sentry <https://sentry.io/>`_ group related events and
    facilitate user identification, etc., so that developers can find the cause
    of the error more quickly.

* Monitoring:

  * The logging records events for user-defined heuristics, e.g. for business
    analyses. These records can be used for reports or optimisation of the
    business goals and, if necessary, visualised.

What are the advantages of  ``logging`` over  ``print``?

* The log file contains all available diagnostic information such as file name,
  path, function and line number.
* All events are automatically available via the root logger unless they are
  explicitly filtered out.
* Logging can be muted using either of the following two methods:
  `logging.Logger.setLevel()
  <https://docs.python.org/3/library/logging.html#logging.Logger.setLevel>`_ or
  `logging.disabled
  <https://docs.python.org/3/library/logging.html#logging.disable>`_.

.. seealso::

   * `loguru <https://github.com/Delgan/loguru>`_, which makes logging almost as
     easy as using print instructions.
   * `structlog <https://www.structlog.org/>`_ adds structure to your log
     entries.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    config.ipynb
