Example
=======

#. Notebooks are well suited for making rapid progress, but when the code
   becomes more extensive, it is advisable to move stable code into modules. For
   example, if you wrote in your notebook:

   .. code-block:: python

        df = pd.read_csv(filename)
        df.drop( ...
        df.query( ...
        df.groupby( ...

   so you can outsource it to a file ``dataprep.py``:

   .. code-block:: python

        def load_and_preprocess_data(filename):
           """Documentation"""
           # Do stuff
           # ...
           return df

   and this can be imported into the notebook with

   .. code-block:: python

        import dataprep
        df = dataprep.load_and_preprocess_data(filename)

   If you change the Python script, the updated variant can be automatically
   adopted with :mod:`IPython.extensions.autoreload`:

   .. code-block:: python

    %load_ext autoreload
    %autoreload
