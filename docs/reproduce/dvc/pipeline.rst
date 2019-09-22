Pipelines
=========

Code und Daten verbinden
------------------------

Befehle wie ``dvc add``, ``dvc push`` und ``dvc pull`` können unabhängig von
Änderungen im Git-Repository vorgenommen werden und bieten daher nur die Basis
um Modelle und große Datenmengen zu verwalten. Um tatsächlich reproduzierbare
Ergebnisse zu erzielen, müssen Code und Daten miteinander verbunden werden.

Mit ``dvc run`` könnt ihr euren Code in eine reproduzierbare Pipeline-Phase
eurer ML-Pipeline verwandeln, z.B.:

.. code-block:: console

    $ dvc run -f prepare.dvc \
      -d src/prepare.py -d data/data.xml \
      -o data/prepared \
      pipenv run python src/prepare.py data/data.xml

``-f``
    gibt den Namen der generierten CVS-Datei an.
``-d``
    gibt Abhängigkeiten für das reproduzierbare Kommando an.

    Wenn zm Reproduzieren der Ergebnisse beim nächsten Mal ``dvc repo``
    aufgerufen wird, überprüft DVC diese Abhängigkeiten und entscheidet, ob
    diese auf dem aktuellen Stand ist oder erneut ausgeführt werden muss um
    aktuellere Ergebnisse zu erhalten.

``-o``
    gibt die Ausgabedatei oder das Ausgabeverzeichnis an.

    Diese generierten Dateien werden von ``dvc run`` automatisch von DVC
    verwaltet, ihr müsst also nicht noch zusätzlich ``dvc add`` aufrufen.

Die generierte ``prepare.dvc`` sieht dann z.B. folgendermaßen aus:

.. code-block:: yaml

    cmd: pipenv run python src/prepare.py data/data.xml
    outs:
    - path: data/prepared
      metric: false
      cache: true
      persist: false
      md5: 6836f797f3924fb46fcfd6b9f6aa6416.dir
    deps:
    - path: src/prepare.py
      md5: 1a18704abffac804adf2d5c4549f00f7
    - path: data/data.xml
      md5: a304afb96060aad90176268345e10355
    md5: 51cba7345de3eab359598b068452202b

Anschließend müssen die geänderten Daten nur noch in Git bzw. DVC übernommen
werden:

.. code-block:: console

    $ git add data/.gitignore prepare.dvc
    $ git commit -m "Create prepare stage"
    $ dvc push

Werden nun mehrere Phasen mit ``dvc run`` erstellt, wobei die Ausgabe eines
Kommandos als Abhängigkeit eines anderen angegeben wird, entsteht eine `DVC
Pipeline <https://dvc.org/doc/commands-reference/pipeline>`_.

Pipelines anzeigen
------------------

Solche Datenpipelines lassen sich anzeigen oder als Abhängigkeitsgraph
darstellen mit ``dvc pipeline``

* für die einzelnen Phasen:

  .. code-block:: console

    $ dvc pipeline show evaluate.dvc
    data/data.xml.dvc
    prepare.dvc
    featurize.dvc
    train.dvc
    evaluate.dvc

* für die aufeinanderfolgenden Kommandos:

  .. code-block:: console

    $ dvc pipeline show train.dvc --commands
    python src/prepare.py data/data.xml
    python src/featurization.py data/prepared data/features
    python src/train.py data/features model.pkl
    python src/evaluate.py model.pkl data/features auc.metric

* für die aufeinanderfolgenden Ausgaben:

  .. code-block:: console

    $ dvc pipeline show train.dvc --outs
    data/data.xml
    data/prepared
    data/features
    model.pkl
    auc.metric

* Sofern `Graphviz <http://www.graphviz.org/>`_ und `pydot
  <https://pypi.org/project/pydot/>`_ installiert ist, läst sich der
  der Abhängigkeitsgraph auch visualisieren:

.. graphviz::

    strict digraph  {
        "featurize.dvc";
        "train.dvc";
        "prepare.dvc";
        "evaluate.dvc";
        "data/data.xml.dvc";
        "featurize.dvc" -> "train.dvc";
        "featurize.dvc" -> "evaluate.dvc";
        "train.dvc" -> "evaluate.dvc";
        "prepare.dvc" -> "featurize.dvc";
        "data/data.xml.dvc" -> "prepare.dvc";
    }

