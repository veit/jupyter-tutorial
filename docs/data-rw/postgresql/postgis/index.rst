PostGIS
=======

`PostGIS <https://postgis.net/>`_ ist eine Erweiterung für PostgreSQL, die
geografische Objekte und Funktionen umfasst. Die Erweiterung implementiert u.a.
die `Simple-Feature-Access <https://www.ogc.org/standards/sfa>`_-Spezifikation
des `Open Geospatial Consortium <https://www.ogc.org/>`_. Obwohl PostgreSQL
bereits Geometrietypen unterstützt, sind diese jedoch für geographische Aufgaben
ungenügend. Daher erstellt PostGIS eigene Datentypen, die besser für
geographische Aufgaben geeignet sind. Im Einzelnen werden folgende
Geometrietypen unterstützt:

* OpenGIS mit Well-Known Text und Well-Known Binary
* Extended Well-Known Text und Extended Well-Known Binary zusätzlich mit
  Höheninformationen und/oder Messwerten
* SQL/MM mit Circularstring, Compoundcurve, Curvepolygon, Multicurve und
  Multisurface

`GEOS <https://trac.osgeo.org/geos/>`_ hingegen enthält die zahlreichen
räumlichen Funktionen und Operatoren für geographische Daten.

`pgRouting <https://pgrouting.org/>`_ schließlich enthält Routing-Funktionen
auf Basis von PostGIS.

Im `OpenStreetMap <https://www.openstreetmap.org>`_-Projekt wird PostGIS zum
Rendern von Karten mit `Mapnik <https://mapnik.org/>`_ verwendet.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    install
    optimising
    load
