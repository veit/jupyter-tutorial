Git für Jupyter Notebooks konfigurieren
=======================================

Im Notebook-Dateiformat :ref:`nbformat <was-ist-eine-ipynb-datei>` können auch
die Ergebnisse der Berechnungen gespeichert werden. Dies können auch
Base-64-codierte Blobs für Bilder und andere Binärdaten sein, die üblicherweise
nicht in eine Versionsverwaltung übernommen werden sollen. Diese können zwar
manuell entfernt werden mit :menuselection:`Cell --> All Output --> Clear`, ihr
müsst diese Schritte jedoch vor jedem ``git add`` ausführen, und es löst auch
eine zweite Ursache für das Rauschen in ``git diff`` nicht, nämlich dasjeinige
in den `Metadaten
<https://nbformat.readthedocs.io/en/latest/format_description.html#metadata>`_.

Um nun systematisch vergleichbare Versionen von Notebooks in der
Versionsverwaltung zu erhalten, können wir `jq
<https://stedolan.github.io/jq/>`_ verwenden, einen leichtgewichtigen
JSON-Prozessor. Zwar benötigt man einige Zeit um ``jq`` einzurichten da es
eine eigene eine eigene Abfrage-/Filtersprache mitbringt, aber meist sind
schon die Standardeinstellungen gut gewählt. 

Installation
------------

``jq`` für Debian/Ubuntu kann installiert werden mit:

.. code-block:: console

    $ sudo apt install jq

oder für Mac OS X mit:

.. code-block:: console

    $ brew install jq

Beispiel
--------

Ein typischer Aufruf ist:

.. code-block:: console

    jq --indent 1  \ 
      '(.cells [] | select (has ("output")) | .outputs) = [] 
      | (.cells [] | select (has ("execution_count")) | .execution_count) = null 
      | .metadata = {"language_info": {"name": "python", "pygments_lexer": "ipython3"}} 
      | .Cells []. Metadaten = {} 
      '  example.ipynb

Jede Zeile innerhalb der einfachen Anführungszeichen definiert einen Filter –
die erste wählt alle Einträge aus der Liste *cells* aus und löscht die Ausgaben.
Der nächste Eintrag setzt alle Ausgaben zurück. Der dritte Schritt löscht die
Metadaten des Notebooks und ersetzt sie durch ein Minimum an erforderlichen
Informationen, damit das Notebook noch ohne Beanstandungen ausgeführt werden
kann, folgendes eingeben:wenn es mit nbsphinx formatiert sind. Die vierte Filterzeile,
``.cells []. metadata = {}``, löscht alle Metainformationen. Falls ihr bestimmte
Metainformationen beibehalten wollt, könnt ihr dies hier angeben. 

Einrichten
----------

#. Um euch die Arbeit zu erleichtern, könnt ihr einen Alias in der
   ``~/.bashrc``-Datei anlegen:

   .. code-block:: bash

    alias nbstrip_jq="jq --indent 1 \
        '(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
        | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
        | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
        | .cells[].metadata = {} \
        '"

#. Anschließend könnt ihr bequem im Terminal folgendes eingeben:

   .. code-block:: console

    $ nbstrip_jq example.ipynb > stripped.ipynb

#. Wenn ihr von einem bereits vorhandenen Notebook ausgeht, solltet ihr zunächst
   einen ``filter``-Commit hinzufügen, indem ihr einfach die neu gefilterte
   Version eures Notebooks ohne die unerwünschten Metadaten einlest. Nachdem ihr
   mit ``git add`` das Notebook hinzugefügt habt, könnt ihr mit
   ``git diff --cached`` schauen, ob der Filter auch wirklich gewirkt hat bevor
   ihr dann ``git commit -m 'filter'`` angebt.

#. Wenn ihr diesen Filter für alle Git-Repositories verwenden wollt, könnt ihr
   euer Git auch global konfigurieren:

   #. Zunächst fügt ihr in  ``~/.gitconfig`` folgendes hinzu:

      .. code-block:: ini

        [core]
        attributesfile = ~/.gitattributes

        [filter "nbstrip_jq"]
        clean = "jq --indent 1 \
                '(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
                | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
                | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
                | .cells[].metadata = {} \
                '"
        smudge = cat
        required = true

   #. Anschließend müsst ihr in ``~/.gitattribute`` nur noch folgendes angeben:

      .. code-block:: ini

        *.ipynb filter=nbstrip_jq

      .. warning::
         Wenn ihr ``git rebase`` durchführen wollt, solltet ihr vorher die Zeile
         deaktivieren.

#. Dennoch bleibt das Problem, dass ``git status`` Änderungen an Dateien
   anzeigt wenn die Zellen eines Notebook ausgeführt wurden, und dies obwohl
   ``git diff`` weiterhin keine Änderungen anzeigt. Daher sollte in der
   ``~/.bashrc``-Datei folgendes eingetragen um schnell das jeweilige
   Arbeitsverzeichnis reinigen zu können:

   .. code-block:: bash

    function nbstrip_all_cwd {
        for nbfile in *.ipynb; do
            echo "$( nbstrip_jq $nbfile )" > $nbfile
        done
        unset nbfile
    }

