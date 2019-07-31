=========================
Branches & merge requests
=========================

Merge requests unterstützen einen Workflow bei regelmäßigen Deployments.

1. Erstellen eines Feature-Branch
=================================

Beim Erstellen eines Branches erzeugt ihr eine neue Umgebung, in der ihr
neues ausprobieren könnt. Dies wirkt sich nicht auf den ``master``-Branch
aus. Und ihr könnt euch sicher sein, dass der Branch nicht mit dem ``master``
zusammengeführt wird, bevor er nicht von einer Person überprüft wurde, mit
der ihr zusammenarbeitet.

.. note::
   Achtet darauf, dass die Namen der Branches möglichst aussagekräftig sind,
   also z.B. ``refactor-user-model`` oder ``user-content-cache``.

.. note::
   Achtet darauf, dass der ``master``-Branch immer nur Code enthält, der auch
   für ein Deployment geeignet ist. 

2. Hinzufügen von Commits
=========================

Sobald ein Feature-Branch erstellt wurde, könnt ihr mit den Änderungen
beginnen. Immer wenn ihr eine Datei hinzufügt, bearbeitet oder löscht, könnt
ihr diese Änderungen in eurem Branch festhalten. Der Fortschritt wird dann in
euren Commits sichtbar.

Die Commits erlauben darüberhinaus auch allen anderen Projektbeteiligten, eure
Arbeit zu verstehen: was ihr getan habt und warum. 

.. note::
   Commit-Messages erleichtern nicht nur das aktuelle Verständnis für eure
   Änderungen, sondern erlauben auch später, z.B. mit ``git blame``,
   Nachvollziehen zu können, warum ihr diese Änderungen gemacht habt.
   
3. Merge request stellen
========================

Merge-Requests initiieren eine Diskussion über ein Bündel von Commits. Da sie
eng in das  zugrunde liegenden Git-Repository integriert sind, können alle
Projektbetieligten genau sehen, welche Änderungen zusammengeführt werden würden,
wenn die Anfrage akzeptiert wird.

Ihr könnt einen Merge-Request auch jederzeit stellen, wenn ihr nicht
weiterkommt und Hilfe oder Rat benötigt. Mit ``@`` in euren Kommentaren könnt
ihr auch bestimmte Personen aus dem Projektteam nach Feedback fragen.

4. Review und Diskussion des Codes
==================================

Nachdem ihr einen Merge Request gestellt habt, wird eine Person oder das
Projektteam Fragen oder Kommentare zu euren Änderungen abgeben: Eventuell
entspricht der Coding Style nicht den Projektrichtlinien, oder des Fehlen
Unit-Tests oder es sieht alles gut aus. Merge Requests sind dazu da, solche
Diskussionen zu fördern und zu dokumentieren. 

Ihr könnt auch nach einem Merge Request auf diesem Branch ``git push``
ausführen, z.B. um Fixes, die aus diesen Diskussionen entstanden, ebenfalls
noch in diesen Merge Request aufzunehmen. GitLab zeigt diesen erneuten Commit
in der Ansicht dieses Merge Requests an.

.. note::
   Auch die Kommentare zu eurem Merge Request werden in Markdown geschrieben,
   sodass ihr auch hier z.B. vorformattierte Textblöcke für Quellcode etc.
   verwenden könnt.

5. Deployment
=============

Mit GitLab lassen sich Deployments erstellen z.B. für das automatisierte Testen
oder die Qualitätssicherung in einem Staging-Environment.

Auf diese Weise lässt sich dann auch sicherstellen, dass die Änderungen deployed
werden können.

6. Merge
========

Wenn  auch das Deployment eurer Änderungen erfolgreich war, können eure
Änderungen mit dem ``master``-Branch zusammengeführt werden.

.. note::
    Durch das Einfügen bestimmter Schlüsselwörter im Text eures Merge Request
    könnt ihr in GitLab Issues mit Code verknüpfen. Wird euer Merge Request
    bestätigt, kann z.B. auch ein Issue geschlossen werden. So würde beim
    Kommentar ``/close #42`` zu einem Merge Request beim Zusammenführen auch das
    Item mit der Nummer 42 geschlossen werden. Weitere Infos hierzu erhaltet ihr unter
    `GitLab quick actions
    <>https://docs.gitlab.com/ee/user/project/quick_actions.html`_.


