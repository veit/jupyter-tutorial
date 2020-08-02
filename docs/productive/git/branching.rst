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
    befindet, z.B.:

    .. code-block:: console

        $ git checkout master
        $ git merge hotfix
        Updating f42c576..3a0874c
        Fast forward
         setup.py |    1 -
         1 files changed, 0 insertions(+), 1 deletions(-)

    ``Fast forward``
        besagt, dass der neue Commit direkt auf den ursprünglichen Commit folgte
        und somit der Zeiger (*branch pointer*) nur weitergeführt werden musste.

    In anderen Fällen kann die Ausgabe z.B. so aussehen:

    .. code-block:: console

        $ git checkout master
        $ git merge #42
        Merge made by recursive.
         setup.py |    1 +
         1 files changed, 1 insertions(+), 0 deletions(-)

    ``recursive``
        ist eine Merge-Strategie, die verwendet wird, sofern die Zusammenführung
        nur zu ``HEAD`` erfolgt.

Merge-Konflikte
---------------

Gelegentlich stößt Git beim Zusammenführen jedoch auf Probleme, z.B.:

    .. code-block:: console

        $ git merge #17
        Auto-merging setup.py
        CONFLICT (content): Merge conflict in setup.py
        Automatic merge failed; fix conflicts and then commit the result.

    .. seealso::

        * `Git Branching - Einfaches Branching und Merging
          <https://git-scm.com/book/de/v2/Git-Branching-Einfaches-Branching-und-Merging>`_
        * `Git Tools - Fortgeschrittenes Merging
          <https://git-scm.com/book/de/v2/Git-Tools-Fortgeschrittenes-Merging>`_

Verzweigungen (Branches)
------------------------

``$ git branch -d [name]``
    löscht den ausgewählten Zweig, wenn er bereits in einen anderen überführt
    wurde.

    ``-D`` statt ``-d`` erzwingt die Löschung.

.. seealso::
    * `Git Branching - Branches auf einen Blick
      <https://git-scm.com/book/de/v2/Git-Branching-Branches-auf-einen-Blick>`_
