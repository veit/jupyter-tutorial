Pandas
======

`Pandas-Visualization
<https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html>`_ 
baut auf :doc:`/viz/matplotlib` auf, bietet jedoch ein einfacher zu bedienendes
Interface für Pandas-Dataframes und -Zeitreihen.

Installation
------------

Ihr könnt entweder die Python-Kernel des JupyterHub verwenden oder Pandas
lokal installieren mit:

.. code-block:: console

    $ pipenv install pandas

.. note::
    Falls ihr pipenv noch nicht installiert hab, findet ihr eine Anleitung
    hierzu unter :ref:`pipenv-installieren`.

Die Installation könnt Ihr dann überprüfen mit:

.. code-block:: python

    >>> import pandas as pd

Beispiel
--------

.. code-block:: python

    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.random.randn(1000, 4), columns=['A','B','C','D'])
    pd.plotting.scatter_matrix(df, alpha=0.2)

.. seealso::
   - `Pandas Plotting Docs
     <https://pandas.pydata.org/pandas-docs/stable/reference/plotting.html>`_

