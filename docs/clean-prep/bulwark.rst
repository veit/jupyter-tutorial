Bulwark
=======

`Bulwark <https://bulwark.readthedocs.io/en/stable/index.html>`_ is a package
for property-based testing of pandas dataframes. The project was heavily
influenced by the no-longer-supported :doc:`engarde.ipynb` library.

Installation
------------

.. code-block:: console

    $ pipenv install bulwark
    Installing bulwark…
    Adding bulwark to Pipfile's [packages]…
    ✔ Installation Succeeded
    Locking [dev-packages] dependencies…
    ✔ Success!
    Updated Pipfile.lock (0d075a)!

Usage
-----

Checks
~~~~~~

Bulwark comes with checks for many of the common assumptions.

.. code-block:: python

    import bulwark.checks as ck

    df.pipe(ck.has_no_nans())

Decorators
~~~~~~~~~~

For each check in ```check.py`` ``bulwark.decorators`` creates decorators, e.g.:

.. code-block:: python

    import bulwark.decorators as dc

    @dc.IsShape((-1, 10))
    @dc.IsMonotonic(strict=True)
    @dc.HasNoNans()
    def compute(df):
        # complex operations to determine result
        ...
    return result_df

``CustomCheck``
~~~~~~~~~~~~~~~

You can also create your own custom function, e.g.:

.. code-block:: python

    import bulwark.checks as ck
    import bulwark.decorators as dc
    import numpy as np
    import pandas as pd

    def len_longer_than(df, l):
        if len(df) <= l:
            raise AssertionError("df is not as long as expected.")
        return df

    @dc.CustomCheck(len_longer_than, 10, enabled=False)
    def append_a_df(df, df2):
        return df.append(df2, ignore_index=True)

    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df2 = pd.DataFrame({"a": [1, np.nan, 3, 4], "b": [4, 5, 6, 7]})

    append_a_df(df, df2)  # doesn’t fail because the check is disabled

``MultiCheck``
~~~~~~~~~~~~~~

With the built-in ``MultiCheck`` you can run multiple tests and see all the
errors at once, e.g.:

.. code-block:: python

    @dc.MultiCheck(checks={ck.has_no_nans: {"columns": None},
                           len_longer_than: {"l": 6}},
                   warn=False)
    def append_a_df(df, df2):
        return df.append(df2, ignore_index=True)

    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    df2 = pd.DataFrame({"a": [1, np.nan, 3, 4], "b": [4, 5, 6, 7]})

    append_a_df(df, df2)


.. note::

    When you use ``MultiCheck``, there’s no need to use ``CustomCheck`` – just
    feed in the function.
