Example
=======

Notebooks are well suited for making rapid progress, but when the code
becomes more extensive, it is advisable to move stable code to individual
files. Such files are called :doc:`python:tutorial/modules`. For example, if
you wrote in your notebook:

.. code-block:: python

    filename = 'example.csv'
    df = pd.read_csv(filename)

so you can outsource it to a module. The file name is the module name
``dataprep``, supplemented by the suffix ``.py``.

Within this file you can now define the method ``load_data``:

.. literalinclude:: dataprep.py
   :language: python
   :linenos:

and this can be imported into the notebook with

.. code-block:: python

    import dataprep

Then you can use the method ``load_data`` to read for example the CSV file
``example.csv``:
   .. code-block:: python

        df = dataprep.load_and_preprocess_data(filename)

If you change the Python script, the updated variant can be automatically
adopted with :mod:`IPython.extensions.autoreload`:

.. code-block:: python

    %load_ext autoreload
    %autoreload
