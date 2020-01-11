yt
==

`yt <https://yt-project.org/>`_ analysiert und visualisiert Volumendaten.

Installation
------------

.. code-block:: console

    $ pipenv install yt

.. note::
   Falls ihr pipenv noch nicht installiert hab, findet ihr eine Anleitung hierzu
   unter :ref:`pipenv-installieren`.

Die Installation könnt Ihr dann überprüfen mit:

.. code-block:: console

    $ yt -h
    usage: yt [-h] [--config CONFIG] [--paste] [--paste-detailed] [--detailed]
    …

Beispiel
--------

.. code-block:: python

    >>> import yt
    >>> ds = yt.load("IsolatedGalaxy/galaxy0030/galaxy0030")
    yt : [INFO     ] 2019-06-05 13:10:39,581 Parameters: current_time              = 0.0060000200028298
    yt : [INFO     ] 2019-06-05 13:10:39,583 Parameters: domain_dimensions         = [32 32 32]
    yt : [INFO     ] 2019-06-05 13:10:39,585 Parameters: domain_left_edge          = [0. 0. 0.]
    yt : [INFO     ] 2019-06-05 13:10:39,586 Parameters: domain_right_edge         = [1. 1. 1.]
    yt : [INFO     ] 2019-06-05 13:10:39,588 Parameters: cosmological_simulation   = 0.0
    >>> ds.r[0.45:0.55,:,:].sum("cell_mass").in_units("Mjup")
    Parsing Hierarchy : 100%|██████████| 173/173 [00:00<00:00, 3427.19it/s]
    yt : [INFO     ] 2019-06-05 13:10:39,676 Gathering a field list (this may take a moment.)
    9985379895930.627 Mjup

.. note::
    In Version 3.3 von yt wurde ein experimenteller hardware-beschleunigter
    interaktiver Volume-Renderer eingeführt. Um die `Interactive Data
    Visualization (IDV)
    <https://yt-project.org/doc/visualizing/interactive_data_visualization.html>`_ 
    verwenden zu können, müssen zusätzlich `PyOpenGL
    <https://pypi.python.org/pypi/PyOpenGL>`_ und `cyglfw3
    <https://pypi.python.org/pypi/cyglfw3/>`_ mit ihren jeweiligen
    Abhängigkeiten installiert werden.

.. seealso::
   - `Quickstart <https://yt-project.org/doc/quickstart/index.html>`_
   - `Cookbook <https://yt-project.org/doc/cookbook/index.html>`_
   - `Docs <https://yt-project.org/doc/>`_
   - `Extensions <https://yt-project.org/extensions.html>`_

