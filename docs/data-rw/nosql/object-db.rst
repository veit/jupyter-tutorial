Objektdatenbanksysteme
======================

Viele Programmiersprachen legen eine objektorientierte Programmierung nahe und
daher erscheint die Speicherung dieser Objekte natürlich. Daher liegt nahe, den
kompletten Prozess von der Implementierung bis zur Speicherung einheitlich und
einfach zu gestalten. Im Einzelnen sind die Vorteile:

Natürliche Modellierung und Repräsentation von Problemen
    Probleme lassen sich auf eine Weise modellieren, die der menschlichen
    Denkweise sehr nahe kommen.
Übersichtlicher, lesbarer und verständlicher
    Die Daten und die auf diesen operierenden Funktionen werden zu einer Einheit
    zusammengefasst, wodurch die Programme übersichtlicher, lesbarer und
    verständlicher werden.
Modular und wiederverwendbar
    Programmteile  lassen sich einfach und flexibel wiederverwenden.
Erweiterbar
    Programme lassen sich einfach erweitern und an geänderte Anforderungen
    anpassen.

Object-relational impedance mismatch
------------------------------------

Objektorientierte Programmierung und relationale Datenhaltung sind aus
verschiedenen Gründen problematisch. So ist ein wichtiges Konzept der OOP zur
Umsetzung komplexer Modelle die Vererbung. Im relationalen Paradigma gibt es
jedoch nichts vergleichbares. Zur Umwandlung entsprechender Klassenhierarchien
in ein relationales Modell wurden objekt-relationale Mapper, ORM entwickelt, wie
z.B. :doc:`../postgresql/sqlalchemy`. Prinzipiell gibt es zwei verschiedene
Ansätze für ein ORM, wobei in beiden Fällen eine Tabelle für eine Klasse
angelegt wird:

Vertikale Partitionierung
    Die Tabelle enthält nur die Attribute der entsprechenden Klasse sowie einen
    Fremdschlüssel für die Tabelle der Oberklasse. Für jedes Objekt wird ein dann
    ein Eintrag in der zur Klasse gehörenden Tabelle sowie in den Tabellen aller
    Oberklassen angelegt. Beim Zugriff müssen die Tabellen mit Joins verbunden
    werden, wodurch es bei komplexen Modellen zu erheblichen
    Performance-Verlusten kommen kann.
Horizontale Partitionierung
    Jede Tabelle enthält die Attribute der zugehörigen Klasse sowie aller
    Oberklassen. Bei einer Änderung der Oberklasse müssen dann jedoch die
    Tabellen aller abgeleiteten Klassen ebenfalls aktualisiert werden.

Grundsätzlich müssen bei der Kombination von OOP und relationaler Datenhaltung
immer zwei Datenmodelle erstellt werden. Dies macht diese Architektur deutlich
komplexer, fehleranfälliger und in der Wartung aufwändiger.

Datenbanksysteme
----------------

Beispiele für Objektdatenbanksysteme sind ZODB und Objectivity/DB.

+------------------------+----------------------------------------+----------------------------------------+
| **Home**               | `ZODB`_                                | `Objectivity/DB`_                      |
+------------------------+----------------------------------------+----------------------------------------+
| **GitHub**             | `zopefoundation/ZODB`_                 |                                        |
+------------------------+----------------------------------------+----------------------------------------+
| **Docs**               | `www.zodb.org/en/latest/tutorial.html`_| `Objectivity/DB Basics Tutorial`_      |
+------------------------+----------------------------------------+----------------------------------------+
| **Anwendungsgebiete**  | Plone, Pyramid, BTrees, volatile Daten | IoT, Telekommunikation, Netzwerktechnik|
+------------------------+----------------------------------------+----------------------------------------+
| **Entwicklungssprache**| Python                                 | Java                                   |
+------------------------+----------------------------------------+----------------------------------------+
| **Lizenzen**           | Zope Public License (ZPL) 2.1          | kommerziell                            |
+------------------------+----------------------------------------+----------------------------------------+
| **Datenmodell**        | PersistentList, PersistentMapping,     | Objects, References, Relationships,    |
|                        | BTree                                  | Indexes, Trees und Collections         |
+------------------------+----------------------------------------+----------------------------------------+
| **Query-Langauge**     |                                        | Objectivity/DB predicate query language|
+------------------------+----------------------------------------+----------------------------------------+
| **Transaktionen,       | :term:`ACID`                           | :term:`ACID`                           |
| Nebenläufigkeit**      |                                        |                                        |
+------------------------+----------------------------------------+----------------------------------------+
| **Replikation,         | `ZODB Replication Services (ZRS)`_     | Quorum basierte synchrone Replikation  |
| Skalierung**           |                                        |                                        |
+------------------------+----------------------------------------+----------------------------------------+
| **Anmerkungen**        |                                        |                                        |
+------------------------+----------------------------------------+----------------------------------------+

.. _`ZODB`: hhttp://www.zodb.org/
.. _`Objectivity/DB`: https://www.objectivity.com/products/objectivitydb/
.. _`Objectivity/DB Basics Tutorial`: https://support.objectivity.com/sites/default/files/docs/objy/R12_4_1/html/assist/tutorial/Tutorial.html
.. _`zopefoundation/ZODB`: https://github.com/zopefoundation/ZODB
.. _`www.zodb.org/en/latest/tutorial.html`: http://www.zodb.org/en/latest/tutorial.html
.. _`ZODB Replication Services (ZRS)`: https://pypi.org/project/zc.zrs/
