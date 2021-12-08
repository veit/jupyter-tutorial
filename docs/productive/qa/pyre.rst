PyRe
====

PyRe (Python Reliability) analyses the structural reliability of Python code and
summarises it in a report. Currently, however, only first-order randomness
methods such as Crude Monte Carlo Simulation and Importance Sampling are
supported.

.. seealso::
   * `Docs <https://hackl.science/pyre/>`_
   * `GitHub <https://github.com/hackl/pyre>`_

Installation
------------

.. code-block:: console

    $ pipenv install git+git://github.com/hackl/pyre.git

Reliability analysis
--------------------

A FORM (first-order reliability method) analysis can lead to the following
result, for example:

.. code-block:: console

    ==================================================

     RESULTS FROM RUNNING FORM RELIABILITY ANALYSIS

     Number of iterations:      17
     Reliability index beta:    1.75397614074
     Failure probability:       0.039717297753
     Number of calls to the limit-state function: 164

    ==================================================
