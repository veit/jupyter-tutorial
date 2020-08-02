Objektrelationale Abbildung
===========================

    «Objektrelationale Abbildung (englisch object-relational mapping, ORM) ist
    eine Technik der Softwareentwicklung, mit der ein in einer
    objektorientierten Programmiersprache geschriebenes Anwendungsprogramm seine
    Objekte in einer relationalen Datenbank ablegen kann.»[#]_

.. [#] `Wikipedia: Objektrelationale Abbildung
   <https://de.wikipedia.org/wiki/Objektrelationale_Abbildung>`_

Im einfachsten Fall werden Klassen auf Tabellen abgebildet, wobei jedes Objekt einer
Tabellenzeile entspricht und jedem Attribut eine Tabellenspalte.

Um Vererbungshierarchien abzubilden gibt es im Wesentlichen drei verschiedene
Verfahren:

*Single Table*
    Dabei wird eine Tabelle pro Vererbungshierarchie angelegt, wobei alle
    Attribute der Basisklasse und aller davon abgeleiteten Klassen in einer
    gemeinsamen Tabelle gespeichert wird.
*Joined Table* oder *Class Table*
    Dabei wird eine Tabelle je Unterklasse angelegt und für jede davon
    abgeleitete Unterklasse eine weitere Tabelle.
*Table per Class* oder *Concrete Table*
    Dabei werden die Attribute der abstrakten Basisklasse in die Tabellen für
    die konkreten Unterklassen mit aufgenommen. Hierbei ist es jedoch nicht
    möglich, mit einer Abfrage Instanzen verschiedener Klassen zu ermitteln.
