Lizenzieren
===========

Damit andere Eure Software verwenden können, sollte sie eine Lizenz erhalten,
die die Nutzungsbedingungen beschreibt. Andernfalls dürfte sie meist
urheberrechtlich geschützt sein. Urheber sind diejenigen, die zur Software
originär beigetragen haben. Wenn eine Software relizenziert werden soll, ist
die Zustimmung aller Urheber erforderlich.

.. note::
   Dies stellt keine Rechtsberatung dar. Wendet Euch im Zweifelsfall bitte an
   einen Anwalt oder die Rechtsabteilung Eures Unternehmens.

Proprietäre Softwarelizenzen
----------------------------

Proprietäre Softwarelizenzen sind selten standardisiert; sie können kommerziell,
Shareware oder Freeware sein.

Freie und Open-Source Software-Lizenzen
---------------------------------------

Sie werden von der `Free Software Foundation (FSF)
<https://www.fsf.org/de/?set_language=de>`_ und der `Open Source Initiative
(OSI) <https://opensource.org/>`_ definiert. Dabei kann im Wesentlichen
unterschieden werden zwischen Copyleft-, freizügigen- und gemeinfreien Lizenzen.

Copyleft-Lizenzen
~~~~~~~~~~~~~~~~~

Copyleft-Lizenzen verpflichten die Lizenznehmer, jegliche Bearbeitung der
Software unter die Lizenz des ursprünglichen Werks zu stellen. Dies soll
Nutzungseinschränkungen der Software verhindern. Die bekannteste Copyleft-Lizenz
ist die GNU General Public License (GPL). Dabei wird das Copyleft der GPL als
sehr stark, das der Mozilla Public License hingegen als sehr schwach angesehen.

Da die Lizenzgeber nicht selbst an ih eigenes Copyleft gebunden sind, können sie
neue Versionen auch unter proprietärer Lizenz veröffentlichen oder Dritten dies
erlauben (Mehrfachlizenzierung).

Durch Copyleft-Lizenzen können jedoch schnell Inkompatibilitäten auch zu freien
Lizenzen ohne Copyleft entstehen. So ist beispielsweise die 3-Clause-BSD-Lizenz
mit der GPL inkompatibel.

Freizügige Open-Source-Lizenzen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Freizügige oder permissive Open-Source-Lizenzen erlauben eine breitere
Wiederverwendung als die Copyleft-Lizenzen. Ableitungen und Kopien des
Quellcodes können unter Bedingungen verbreitet werden, die grundlegend andere
Eigenschaften haben als die der Originallizenz. Die bekanntesten Beispiele
solcher Lizenzen sind die MIT-Lizenz und die BSD-Lizenz.

Gemeinfreie Lizenzen
~~~~~~~~~~~~~~~~~~~~

Bei gemeinfreien oder Public Domain-Lizenzen gehen die Urheberrechte an die
Allgemeinheit über. Zur Kennzeichnung der Freigabe weitest möglicher
Nutzungsrechte wurde die Creative Commons Zero-Lizenz erstellt.

Auswahl einer geeigneten Lizenz
-------------------------------

Übersichten über mögliche Lizenzen findet Ihr in `SPDX License List
<https://spdx.org/licenses/>`_ oder `OSI Open Source Licenses by Category
<https://opensource.org/licenses/category>`_. Bei der Wahl einer geeigneten
Lizenz unterstützt Euch die Website `Choose an open source license
<https://choosealicense.com/>`_.

GitHub
------

Auf `GitHub <http://github.com/>`_ könnt Ihr Euch eine Open Source-Lizenz in
Eurem Repository erstellen lassen.

#. Geht zur Hauptseite Eures Repository.
#. Klickt auf *Create new file* und gebt anschließend als Dateiname ``LICENSE``
   oder ``LICENSE.md`` ein.
#. Anschließend könnt Ihr rechts neben dem Feld für den Dateinamen auf *Choose a
   license template* klicken.
#. Nun könnt Ihr die für Euer Repository passende Open Source-Lizenz auswählen.
#. Ihr werdet nun zu zusätzlichen Angaben aufgefordert, sofern die gewählte
   Lizenz dies erfordert.
#. Nachdem Ihr eine Commit-Message angegeben habt, z.B. ``Add license``, könnt
   Ihr auf *Commit new file* klicken.

Falls Ihr in Eurem Repository bereits eine ``/LICENSE``-Datei hinzugefügt habt,
verwendet GitHub `licensee <https://github.com/licensee/licensee>`_ um die Datei
mit einer kurzen `Liste von Open-Source-Lizenzen
<https://choosealicense.com/appendix/>`_ abzugleichen. Falls GitHub die Lizenz
Eures Repository nicht erkennen kann, enthält es möglicherweise mehrere
Lizenzen oder ist zu komplex. Überlegt Euch dann, ob Ihr die Lizenz vereinfachen
könnt, z.B. indem Ihr Komplexität in die ``/README``-Datei auslagert.

Umgekehrt könnt Ihr auf GitHub auch nach Repositories mit bestimmten Lizenzen
oder Lizenzfamilien suchen. Eine Übersicht über die Lizenz-Schlüsswlwörter
erhaltet Ihr in `Searching GitHub by license type
<https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository#searching-github-by-license-type>`_.

Schließlich könnt Ihr Euch von `Shields.io <https://shields.io/>`_ ein
License-Badge generieren lassen, das Ihr z.B. auf Eurer ``README``-Datei
einbinden könnt, z.B.

.. code-block:: rst

    |License|

    .. |License| image:: https://img.shields.io/github/license/veit/jupyter-tutorial.svg
       :target: https://github.com/veit/jupyter-tutorial/blob/master/LICENSE

|License|

.. |License| image:: https://img.shields.io/github/license/veit/jupyter-tutorial.svg
   :target: https://github.com/veit/jupyter-tutorial/blob/master/LICENSE

Standardformat für die Lizenzierung
-----------------------------------

Wir empfehlen die Verwendung von ``SPDX-FileCopyrightText: [year] [copyright
holder]``. Üblicherweise sollte die Angabe das gesamte Software-Produkt
umfassen, Ihr könnt jedoch auch Elemente ausnehmen.

Konformität überprüfen
----------------------

`REUSE <https://reuse.software/>`_ wurde von der  Free Software Foundation
Europe (FSFE) initiiert, um die Lizenzierung freier Software-Projekte zu
erleichtern. Das `REUSE tool <https://git.fsfe.org/reuse/tool>`_ überprüft
Lizenzen und unterstützt Euch bei der Einhaltung der Lizenzkonformität.
Mit der `REUSE API <https://reuse.software/dev/#api>`_ könnt Ihr Euch auch
ein dynamisches Compliance-Badge generieren:

.. figure:: reuse-compliant.png
   :alt: REUSE-compliant Badge

CI-Workflow
~~~~~~~~~~~

Ihr könnt REUSE einfach in Euren Continuous Integration-Workflow integrieren,
z.B. für GitLab in der ``.gitlab-ci.yml``-Datei mit:

.. code-block:: yaml

    reuse:
      image:
        name: fsfe/reuse:latest
        entrypoint: [""]
      script:
        - reuse lint

Alternativen
~~~~~~~~~~~~

`SPDX <https://spdx.org/>`_
    SPDX definiert eine standardisierte Methode zum Austausch von Urheberrechts-
    und Lizenzinformationen zwischen Projekten und Personen
`ClearlyDefined <https://clearlydefined.io/>`_
    Es sammelt und zeigt Informationen über die Lizenzierungs- und
    Urheberrechtssituation eines Software-Projekts an
`OpenChain <https://www.openchainproject.org/>`_
    Es empfiehlt REUSE als eine Komponente, um die Klarheit der Lizenz- und
    Urheberrechtssituation zu verbessern, stellt jedoch höhere Anforderungen, um
    eine vollständige Konformität zu erreichen.
`FOSSology <https://www.fossology.org/>`_
    Toolkit für die Einhaltung freier Software, das Informationen in einer
    Datenbank mit Lizenz-, Copyright- und Exportscanner

.. seealso::
   * `A Quick Guide to Software Licensing for the Scientist-Programmer
     <https://doi.org/10.1371/journal.pcbi.1002598>`_
