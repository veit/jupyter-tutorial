hvPlot-Installation
===================

hvPlot kann installiert werden mit

.. code-block:: console

    $ pipenv install hvplot
    Installing hvplot…
    Adding hvplot to Pipfile's [packages]…
    ✔ Installation Succeeded
    …

Um die Beispiele aus :doc:`examples` selbst ausführen zu können, müssen
zusätzlich weitere Pakete installiert werden.

* Für Debian/Ubuntu:

  .. code-block:: console

    $ sudo apt install libsnappy-dev

* Für Mac OS:

  .. code-block:: console

    $ brew install snappy

Anschließend sollten für euren Jupyter-Kernel folgende Python-Pakete installiert
werden:

.. code-block:: console

    $ pipenv install  bokeh==1.4.0 s3fs tqdm python-snappy six numpy>=1.14 pyparsing>=2.0.2 python-dateutil>=2.1 pandas pillow>=4.0  matplotlib scipy xarray datashader
    …

