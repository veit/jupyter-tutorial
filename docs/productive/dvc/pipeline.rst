Pipelines
=========

Code und Daten verbinden
------------------------

Befehle wie ``dvc add``, ``dvc push`` und ``dvc pull`` können unabhängig von
Änderungen im Git-Repository vorgenommen werden und bieten daher nur die Basis
um große Datenmengen und Modelle zu verwalten. Um tatsächlich reproduzierbare
Ergebnisse zu erzielen, müssen Code und Daten miteinander verbunden werden.

.. figure:: combine-git-dvc.png
   :alt: Git und DVC verbinden

Mit ``dvc run`` könnt Ihr einzelne Verbeitungsstufen erstellen, wobei jede
Stufe durch eine, mit Git verwaltete, Quellcode-Datei sowie weiteren
Abhängigkeiten und Ausgabedaten beschrieben wird. Alle Stufen zusammen bilden
dann die DVC-Pipeline.

In unserem Beispiel `dvc-example <https://github.com/veit/dvc-example>`_ soll
die erste Stufe die Daten in Trainings- und Testdaten aufteilen:

.. code-block:: console

    $ dvc run -n split -d src/split.py -d data/data.xml -o data/splitted \
        python src/split.py data/data.xml

``-n``
    gibt den Namen der Verarbeitungsstufe an.
``-d``
    gibt Abhängigkeiten (*dependencies*) für das reproduzierbare Kommando an.

    Wenn zum Reproduzieren der Ergebnisse beim nächsten Mal ``dvc repo``
    aufgerufen wird, überprüft DVC diese Abhängigkeiten und entscheidet, ob
    diese auf dem aktuellen Stand sond oder erneut ausgeführt werden müssen um
    aktuellere Ergebnisse zu erhalten.

``-o``
    gibt die Ausgabedatei oder das Ausgabeverzeichnis an.

In unserem Fall sollte sich der Arbeitsbereich geändert haben in:

.. code-block:: console

      .
      ├── data
      │   ├── data.xml
      │   ├── data.xml.dvc
    + │   └── splitted
    + │       ├── test.tsv
    + │       └── train.tsv
    + ├── dvc.lock
    + ├── dvc.yaml
      ├── requirements.txt
      └── src
          └── split.py

Die generierte ``dvc.yaml``-Datei sieht dann z.B. folgendermaßen aus:

.. code-block:: yaml

    stages:
      split:
        cmd: pipenv run python src/split.py data/data.xml
        deps:
        - data/data.xml
        - src/split.py
        outs:
        - data/splitted

Da die Daten im Ausgabeverzeichnis nie mit Git versioniert werden sollten, hat
``dvc run`` dies auch bereits die ``data/.gitignore``-Datei geschrieben:

 .. code-block:: console

      /data.xml
    + /splitted

Anschließend müssen die geänderten Daten nur noch in Git bzw. DVC übernommen
werden:

.. code-block:: console

    $ git add data/.gitignore dvc.yaml
    $ git commit -m "Create split stage"
    $ dvc push

Werden nun mehrere Phasen mit ``dvc run`` erstellt, wobei die Ausgabe eines
Kommandos als Abhängigkeit eines anderen angegeben wird, entsteht eine `DVC
Pipeline <https://dvc.org/doc/commands-reference/pipeline>`_.

