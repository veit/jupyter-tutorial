=========
Monorepos
=========

Git ist ein sehr flexibles Versionskontrollsystem. Insbesondere ``branch`` und
``merge`` sind mächtige Werkzeuge in verteilten Entwicklungsumgebungen. Manchmal
schafft dies jedoch auch eine unnötige Komplexität. In diesen Fällen kann es
sinnvoll sein, mit einem monolithischen Repository oder *Monorepo* zu arbeiten.

Definition
==========

* Das Repository enthält mehrere logische Projekte (z.B. einen iOS-Client und
  eine Webanwendung)
* Diese Projekte sind meist nur lose miteinander verbunden
* Meist haben diese Projekte auch eine lineare History

Vor- und Nachteile
==================

Ein Vorteil von Monorepos kann sein, dass die Aufwände um zu bestimmen, welche
Versionen des einen Projekts mit welchen Versionen des anderen Projekts
kompatibel sind, deutlich verringert sein könnten. Dies ist zumindest immer
dan der Fall, wenn alle Projekte eines Repository von nur einem Entwicklerteam
bearbeitet werden. Dann empfiehlt sich, mit jedem *Merge* wieder eine lauffähige
Version zu erhalten auch wenn die API zwischen den beiden Projekten geändert
wurde.

Als Nachteil können sich jedoch Performance-Einbußen erweisen. Diese können z.B.
entstehen durch:

eine große Anzahl an Commits
    Da Git DAGs (*directed acyclic graphs*) verwendet um die Historie eines
    Projekts darzustellen, werden alle Operationen, die diesen Graphen
    durchlaufen, also z.B. ``git log`` oder ``git blame``, langsam werden.

eine große Anzahl von Refs
    Eine große Anzahl von *branches* und *tags* verlangsamen git ebenfalls.
    Mit ``git ls-remote`` könnt ihr euch die *Refs* eines Repository anzeigen
    lassen und mit ``git gc`` werden lose *Refs* in einer einzigen Datei
    zusammengefasst.

    Jede Operation, die den Commit-Verlauf eines Repositorys durchlaufen und die
    einzelnen *Refs* berücksichtigen muss, wie z.B. bei ``git branch --contains
    <commit>``, werden bei einem Repo mit vielen *Refs* langsam.

eine große Anzahl an versionierten Dateien
    Der Index des Directory Cache (``.git/index``) wird von Git verwendet um
    zu ermitteln, ob die Datei verändert wurde. Dabei verlangsamen sich mit
    zunehmender Anzahl an Dateien viele Vorgänge, wie z.B. ``git status``
    und ``git commit``.

große Dateien
    Große Dateien in einem Teilbaum oder einem Projekt verringern die Leistung
    des gesamten Repository.

