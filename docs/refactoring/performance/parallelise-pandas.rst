Parallelise pandas
==================

In  :doc:`pandas:user_guide/enhancingperf`, some possibilities are described for
improving the performance of pandas. However, there are also special libraries
that can parallelise the processing of data frames.

cuDF
----

cuDF is a GPU DataFrame library that implements a `Pandas-like API
<https://docs.rapids.ai/api/cudf/stable/api.html>`_.

.. seealso::

    * `Docs <https://docs.rapids.ai/api/cudf/stable/>`_
    * `GitHub <https://github.com/rapidsai/cudf>`_
    * `PyPI <https://pypi.org/project/cudf/>`_
    * `Example notebooks
      <https://github.com/rapidsai-community/notebooks-contrib>`_

Modin
-----

Modin parallelises almost the entire Pandas API. In most cases, the existing
Pandas code only needs to be extended by the following import:

.. code-block:: python

    import modin.pandas as pd

The restrictions refer to  ``pd.read_json``, which is only implemented for
``lines=True``.

.. seealso::

    * `Docs <https://modin.readthedocs.io/en/latest/>`_
    * `GitHub <https://github.com/modin-project/modin>`_

Dask
----

:doc:`dask` DataFrame is a large parallel DataFrame made up of multiple
Pandas DataFrames. Here, the  ``dask.dataframe`` API is a subset of the Pandas
API, although there are minor changes.

.. seealso::

    * `Home <https://docs.dask.org/en/latest/dataframe.html>`_
    * `API docs <https://docs.dask.org/en/latest/dataframe-api.html>`_
    * `Example notebook <https://examples.dask.org/dataframe.html>`_
    * `Tutorial <https://tutorial.dask.org/04_dataframe.html>`_
