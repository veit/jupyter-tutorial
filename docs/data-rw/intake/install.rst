Intake installieren
===================

Anforderungen
-------------

Für die Verwendung von `intake.gui` müssen aktuelle Versionen von
Bokeh≥2.0 und Panel verfügbar sein.

Installation
------------

Intake lässt sich einfach für euren Jupyter-Kernel installieren mit:

.. code-block:: console

    $ pipenv install intake

Katalog mit Beispieldaten erstellen
-----------------------------------

Für die nachfolgenden Beispiele benötigen wir einige Datensätze, die wir
erstellen mit:

.. code-block:: console

    $ pipenv run intake example
    Creating example catalog...
      Writing us_states.yml
      Writing states_1.csv
      Writing states_2.csv

    To load the catalog:
        >>> import intake
        >>> cat = intake.open_catalog('us_states.yml')
