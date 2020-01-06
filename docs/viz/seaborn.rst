seaborn
=======

`seaborn <https://seaborn.pydata.org/>`_ basiert auf :ref:`matplotlib` und
bietet ein High-Level-Interface für die Visualisierung statistischer Daten.

Installation
------------

Ihr könnt entweder die Python-Kernel des JupyterHub verwenden oder Seaborn
lokal installieren mit:

.. code-block:: console

    $ pipenv install seaborn

.. note::
    Falls ihr pipenv noch nicht installiert hab, findet ihr eine Anleitung
    hierzu unter :ref:`pipenv-installieren`.

Die Installation könnt Ihr dann überprüfen mit:

.. code-block:: python

    >>> import seaborn as sns

Beispiel
--------

.. code-block:: python

    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.set(style="white", color_codes=True)

    # Generate a random bivariate dataset
    rs = np.random.RandomState(9)
    mean = [0, 0]
    cov = [(1, 0), (0, 2)]
    x, y = rs.multivariate_normal(mean, cov, 100).T

    # Use JointGrid directly to draw a custom plot
    grid = sns.JointGrid(x, y, space=0, height=6, ratio=50)
    grid.plot_joint(plt.scatter, color="g")
    grid.plot_marginals(sns.rugplot, height=1, color="g")

.. seealso::
   - `Tutorial <https://seaborn.pydata.org/tutorial.html>`_
   - `Example Gallery <https://seaborn.pydata.org/examples/index.html>`_

