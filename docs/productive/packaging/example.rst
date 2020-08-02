Beispiel
========

#. Notebooks sind gut geeignet um schnell voranzukommen, doch bei umfangreicher
   werdendem Code empfiehlt sich, stabilen Code in Module auszulagern. Wenn ihr
   z.B. in eurem Notebook geschrieben habt:

   .. code-block:: python

        df = pd.read_csv(filename)
        df.drop( ...
        df.query( ...
        df.groupby( ...

   so könnt ihr das in eine Datei ``dataprep.py`` auslagern

   .. code-block:: python

        def load_and_preprocess_data(filename):
           """Documentation"""
           # Do stuff
           # ...
           return df

   und dies kann wieder in das Notebook übernommen werden mit

   .. code-block:: python

        import dataprep
        df = dataprep.load_and_preprocess_data(filename)

   Wenn ihr das Python-Skript ändert, kann die aktualiserte Variante automatisch
   übernommen werden mit :mod:`IPython.extensions.autoreload`:

   .. code-block:: python

    %load_ext autoreload
    %autoreload
