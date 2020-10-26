Installation und Nutzung
========================

Installation
------------

voilà kann installiert werden mit:

.. code-block:: console

    $ pipenv run voila docs/jupyter/ipywidgets/examples.ipynb
    pipenv install voila
    Installing voila…
    …
    Successfully installed jupyter-server-0.1.1 jupyterlab-pygments-0.1.0 voila-0.1.10
    …

Starten
-------

… als eigenständige Anwendung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ihr könnt die Installation überprüfen,z.B. mit:

.. code-block:: console

    $ pipenv run voila docs/workspace/jupyter/ipywidgets/examples.ipynb
    …
    [Voila] Voila is running at:
    http://localhost:8866/

Hierbei sollte sich euer Standardbrowser öffnen und die ``ipywidget``-Beispiele
aus unserem Tutorial anzeigen:

.. image:: voila-example-1.png
   :alt: Voilà-Beispiel examples.ipynb

Alternativ könnt ihr euch auch ein Verzeichnis anzeigen lassen mit allen darin
enthaltenen Notebooks:

.. code-block:: console

    $ pipenv run voila docs/workspace/jupyter/ipywidgets
    …

.. image:: voila-example-2.png
   :alt: Voilà-Beispiel für eine Verzeichnisansicht

Es ist auch möglich, sich den Quellcode anzeigen zu lassen mit:

.. code-block:: console

    $ pipenv run voila --strip_sources=False docs/workspace/jupyter/ipywidgets/examples.ipynb
    …

.. note::
    Beachtet, dass der Code nur angezeigt wird. Voilà erlaubt Benutzern nicht,
    den Code zu bearbeiten oder auszuführen.

.. image:: voila-example-3.png
   :alt: Voilà-Beispiel mit Quellcode

Üblicherweise wird das ``light``-Theme verwendet; ihr könnt jedoch auch das
``dark``-Theme auswählen:

.. code-block:: console

    $ pipenv run voila --theme=dark docs/workspace/jupyter/ipywidgets/examples.ipynb
    …

… als Erweiterung des Jupyter-Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternativ könnt ihr voilà auch als Erweiterung des Jupyter-Server starten:

.. code-block:: console

    $ pipenv run jupyter notebook
    …

Anschließend könnt ihr voilà aufrufen, z.B. unter der URL
``http://localhost:8888/voila``.
