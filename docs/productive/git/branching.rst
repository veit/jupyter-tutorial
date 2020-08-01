Git-Verzweigungen
=================

``$ git branch [-a]``
    zeigt alle lokalen Verzweigungen in einem Repository an.

    ``-a``
        zeigt auch alle entfernten Verzweigungen an.

``$ git branch [branch_name]``
    erstellt auf Basis des aktuellen ``HEAD`` einen neuen Zweig.
``$ git checkout [-b] [branch_name]``
    ändert das Arbeitsverzeichnis in den angegebenen Zweig.

    ``-b``
        erstellt den angegebenen Zweig, wenn dieser nicht schon besteht.
``$ git merge [from name]``
    verbindet den angegebenen mit dem aktuellen Zweig, in dem Ihr euch gerade
    befindet.
``$ git branch -d [name]``
    löscht den ausgewählten Zweig, wenn er bereits in einen anderen überführt
    wurde.

    ``-D`` statt ``-d`` erzwingt die Löschung.

