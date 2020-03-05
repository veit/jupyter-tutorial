Matplotlib-Installation
=======================

Ihr könnt entweder die Python-Kernel des JupyterHub verwenden oder Matplotlib
lokal installieren mit:

.. code-block:: console

    $ pipenv install matplotlib

.. note::
   Falls ihr pipenv noch nicht installiert hab, findet ihr eine Anleitung hierzu
   unter :ref:`pipenv-installieren`.

Die Installation könnt Ihr dann überprüfen mit:

.. code-block:: python

    >>> import matplotlib.pyplot as plt

.. note::
    Wenn ihr den Fehler ``TclError: no display name and no $DISPLAY
    environment variable`` erhaltet, müsst ihr vermutlich das iPython Backend
    für Matplotlib verwenden mit
    
     .. code-block:: python

        import matplotlib.pyplot as plt

        # iPython backend for matplotlib
        %matplotlib inline

    Sofern Ihr Matplotlib in einer Python-Datei importiert, müsst ihr
    stattdessen folgendes einfügen::

        import matplotlib.pyplot as plt

        # iPython backend for matplotlib
        get_ipython().run_line_magic('matplotlib', 'inline')

