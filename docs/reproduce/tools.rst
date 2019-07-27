Git-Tools
=========

``nbdime``
----------

`nbdime <https://nbdime.readthedocs.io/>`_, ein GUI für `nbformat
<https://nbformat.readthedocs.io/>`_-Diffs, ersetzt `nbdiff
<https://github.com/tarmstrong/nbdiff>`_ und versucht *Content-Aware*-Diffing
sowie das Merging von Notebooks. ``nbdime``  beschränkt sich nicht nur darauf,
Diffs darzustellen, sondern verhindert auch, dass unnötige Änderungen
eingecheckt werden.

.. _nbstripout_label:

``nbstripout``
--------------

`nbstripout <https://github.com/kynan/nbstripout>`_ automatisiert *Clear all
outputs*. Es nutzt `nbformat <https://nbformat.readthedocs.io/>`_ und ein paar
Automagien um ``git config`` einzurichten. Meines Erachtens hat es jedoch zwei
Nachteile: es beschränkt sich auf den problematischen Metadaten-Abschnitt und
es ist langsam.

``jq``
------

Da ``nbformat`` eine JSON-Datei ist, können wir auch `jq
<https://stedolan.github.io/jq/>`_ verwenden, einen leichtgewichtigen
JSON-Prozessor. Zwar benötigt man einige Zeit um ``jq`` einzurichten da es
eine eigene eine eigene Abfrage-/Filtersprache mitbringt, aber meist sind
schon die Standardeinstellungen gut gewählt. Ein typischer Aufruf ist:

.. code-block:: console

    $ jq --indent 1  \ 
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
kann, wenn es mit nbsphinx formatiert sind. Die vierte Filterzeile,
``.cells []. metadata = {}``, löscht alle Metainformationen. Falls ihr bestimmte
Metainformationen beibehalten wollt, könnt ihr dies hier angeben. 

.. note::
   Um sich die Arbeit zu erleichtern, könnt ihr euch einen Alias in der
   ``~/.bashrc``-Datei anlegen:

   .. code-block:: bash

    $ alias nbstrip_jq="jq --indent 1 \
          '(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
          | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
          | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
          | .cells[].metadata = {} \
          '"

   Anschließend könnt ihr bequem im Terminal eingeben:

   .. code-block:: console

    $ nbstrip_jq example.ipynb > stripped.ipynb

