Jupyter Dashboards
==================

Die `Jupyter Dashboards Layout Extension
<https://jupyter-dashboards-layout.readthedocs.io/>`_ ist ein Add-On für
Jupyter-Notebooks, womit Outputs (Text, Plots, Widgets usw.) in einem
Gestaltungsraster oder in Berichtform angeordnet werden können. Sie speichert
die Informationen zum Layout direkt im Notebook, sodass andere Nutzer dieser
Erweiterung das Notebook ebenfalls im entsprechenden Notebook angezeigt
bekommen. Beispiele für Dashboards findet ihr in `Jupyter Dashboards Demos
<https://github.com/jupyter/dashboards/tree/master/etc/notebooks>`_.

Use Case
--------

Die Jupyter Dashboards sollten folgendes Problem lösen:

#. Alice erstellt ein Jupyter Notebook mit Plots und interaktiven Widgets.
#. Alice ordnet die Notebook-Zellen in einem Raster- oder Report-Format an.
#. Alice stellt das Dashboard auf einem Dashboard-Server bereit.
#. Bob ruft das Dashboard auf dem `Jupyter Dashboards Server
   <https://github.com/jupyter-attic/dashboards_server>`_ auf und interagiert
   mit Alice Dashboard-Applikation.
#. Alice aktualisiert ihr Jupyter Notebook und stellt das Dashboard anschließend
   erneut auf dem Dashboard-Server bereit.

Für die Schritte 3–5 werden jedoch zusätzlich `Jupyter Dashboards Bundler
<https://github.com/jupyter-attic/dashboards_bundlers>`_ und `Jupyter Dashboards
Server <https://github.com/jupyter-attic/dashboards_server>`_ benötigt; beide
sind jedoch mittlerweile als *retired* gekennzeichnet, sollten also nicht weiter
verwendet werden.

.. toctree::
    :titlesonly:
    :maxdepth: 3

    install
    use

.. toctree::
    :hidden:

    matplotlib-example.ipynb

