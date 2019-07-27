Erste Schritte
==============

Wenn ihr von einem bereits vorhandenen Notebook ausgeht, solltet ihr zunächst
einen ``filter``-Commit hinzufügen, indem ihr einfach die neu gefilterte
Version eures Notebooks ohne die unerwünschten Metadaten einlest. Nachdem ihr
mit ``git add`` das Notebook hinzugefügt habt, könnt ihr mit
``git diff --cached`` schauen, ob der Filter auch wirklich gewirkt hat.

Dennoch bleibt jetzt das Problem, dass ``git status`` Änderungen an Dateien
anzeigt wenn die Zellen eines Notebook ausgeführt wurden, und dies obwohl
``git diff`` weiterhin keine Änderungen anzeigt. Daher habe ich in der
``~/.bashrc``-Datei folgendes eingetragen um schnell mein jeweiliges
Arbeitsverzeichnis reinigen zu können:

.. code-block:: bash

    function nbstrip_all_cwd {
        for nbfile in *.ipynb; do
            echo "$( nbstrip_jq $nbfile )" > $nbfile
        done
        unset nbfile
    }

.. warning::
   Wenn ihr ``git rebase`` durchführen wollt, solltet ihr vorher die Zeile:

   .. code-block:: ini

    * .ipynb filter = nbstrip_full

   in ``~/.gitattributes_global`` deaktivieren.

