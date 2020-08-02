Starten der IPython-Shell
=========================

Ihr könnt IPython einfach in einer Konsole starten:

.. code-block:: console

    $ pipenv run ipython
    Python 3.7.0 (default, Aug 22 2018, 15:22:29)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.6.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]:

Alternativ könnt ihr IPython auch in einem Jupyter-Notebook verwenden. Hierfür
startet ihr zunächst den Notebook-Server:

.. code-block:: console

    $ pipenv run jupyter notebook
    [I 17:35:02.419 NotebookApp] Serving notebooks from local directory: /Users/veit/vsc/jupyter-tutorial
    [I 17:35:02.419 NotebookApp] The Jupyter Notebook is running at:
    [I 17:35:02.427 NotebookApp] http://localhost:8888/?token=72209334c2e325a68115902a63bd064db436c0c84aeced7f
    [I 17:35:02.428 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 17:35:02.497 NotebookApp]

Anschließend sollte der Standardbrowser mit der angegebenen URL geöffnet
werden. Häufig ist dies ``http://localhost:8888``.

Nun könnt ihr im Browser einen Python-Prozess starten, indem ihr ein neues
Notebook erstellt.
