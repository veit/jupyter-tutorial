Änderungen zurücknehmen
=======================

``$ git reset [--hard] [target reference]``
   wechselt vom aktuellen Zweig zur Zielreferenz und hinterlässt den Unterschied
   als nicht festgeschriebene Änderung.

   ``--hard`` verwirft alle Änderungen.

``$ git revert [commit sha]``
    erstellt einen neuen Commit und nimmt die Änderungen des angegebenen Commits
    zurück. Die Änderungen werden invertiert.
``$ git fetch [remote]``
    übernimmt die Änderungen von Remote, aktualisiert jedoch nicht die Zweige.
``$ git fetch --prune [remote]``
    Remote-Refs werden entfernt wenn sie im Remote-Repository entfernt wurden.
``$ git pull [remote]``
    ruft Änderungen aus dem Remote-Repository ab und führt den aktuellen Zweig
    mit dem Upstream zusammen.
``$ git push [--tags] [remote]``
    überträgt lokale Änderungen nach Remote.

    Mit ``--tags`` können gleichzeitig Tags übertragen werden.
``$ git push -u [remote] [branch]``
    Übertragen des lokalen Zweigs in das Remote-Repository wobei die Kopie als
    Upstream festgelegt wird.

