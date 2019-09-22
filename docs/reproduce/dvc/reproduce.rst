Reproduzieren
=============

Um die Ergebnisse eines Projekts zu reproduzieren, clonen wir rufen
anschließend die mit DVC verwalteten Daten ab:

.. code-block:: console

    $ git clone https://github.com/iterative/example-get-started.git
    $ cd example-get-started
    $ dvc pull

Anschliepend könnt ihr die Ergebnisse einfach reproduzieren mit

.. code-block:: console

    $ dvc repro evaluate.dvc 
    Stage 'data/data.xml.dvc' didn't change.
    Stage 'prepare.dvc' didn't change.
    Stage 'featurize.dvc' didn't change.
    Stage 'train.dvc' didn't change.
    Stage 'evaluate.dvc' didn't change.
    Data and pipelines are up to date.

