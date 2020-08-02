Reproduzieren
=============

Um die Ergebnisse eines Projekts zu reproduzieren, clonen wir rufen
anschließend die mit DVC verwalteten Daten ab:

.. code-block:: console

    $ git clone https://github.com/veit/dvc-example.git
    $ cd dvc-example
    $ dvc pull -TR
    A       data/data.xml
    1 file added
    $ ls data/
    data.xml	data.xml.dvc

Anschließend könnt ihr die Ergebnisse einfach reproduzieren mit `dvc repro
<https://dvc.org/doc/command-reference/repro>`_:

.. code-block:: console

    $ dvc repro
    Verifying data sources in stage: 'data/data.xml.dvc'
    Stage 'split' didn't change, skipping
    Stage 'featurize' didn't change, skipping
    Stage 'train' didn't change, skipping
    Stage 'evaluate' didn't change, skipping

Ihr könnt nun z.B. Parameter in der ``params.yaml``-Datei ändern und
anschließend die Pipeline erneut durchlaufen:

.. code-block:: console

    $ dvc repro
    Stage 'data/data.xml.dvc' didn't change, skipping
    Stage 'split' didn't change, skipping
    Running stage 'featurize' with command:
        python src/featurization.py data/splitted data/features
    …
    Stage 'train' didn't change, skipping
    Stage 'evaluate' didn't change, skipping
    To track the changes with git, run:
        git add dvc.lock

In unserem Fall hatte die Änderung der Parameter also keinen Einfluss auf das
Ergebnis. Beachtet dabei jedoch, dass DVC Änderungen an Abhängigkeiten und
Ausgaben über md5-Hashwerte erkennt, die in der ``dvc.lock``-Datei gespeichert
sind.
