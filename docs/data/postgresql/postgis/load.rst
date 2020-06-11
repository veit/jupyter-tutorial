Laden von Geodaten
==================

Nun Laden wir einige Geodaten in unsere Datenbank, damit wir uns mit den Tools
und Prozessen zum Abrufen dieser Daten vertraut machen können.

`Natural Earth <http://www.naturalearthdata.com/>`_ bietet eine großartige
Quelle für Basisdaten für die ganze Welt in verschiedenen Maßstäben. Und sas
Beste ist, dass diese Daten gemeinfrei sind:

#. Herunterladen der Daten

.. code-block:: console

    $ mkdir nedata
    $ cd !$
    cd nedata
    $ wget http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/110m/cultural/ne_110m_admin_0_countries.zip

#. Entpacken der Datei

.. code-block:: console

    $ sudo apt install unzip
    $ unzip ne_110m_admin_0_countries.zip
    Archive:  ne_110m_admin_0_countries.zip
      inflating: ne_110m_admin_0_countries.README.html
     extracting: ne_110m_admin_0_countries.VERSION.txt
     extracting: ne_110m_admin_0_countries.cpg
      inflating: ne_110m_admin_0_countries.dbf
      inflating: ne_110m_admin_0_countries.prj
      inflating: ne_110m_admin_0_countries.shp
      inflating: ne_110m_admin_0_countries.shx

#. Laden in unsere ``postgis_db``-Datenbank

   Die Dateien ``.dbf``, ``.prj``, ``.shp`` und ``.shp`` bilden ein sog.
   ShapeFile, ein beliebtes Geodaten-Datenformat, das von der GIS-Software
   verwendet wird. Um dies in unsere Datenbank zu laden, benötigen wir
   zusätzlich `GDAL <http://www.gdal.org/>`_, die *Geospatial Data Abstraction
   Library*. Wenn wir GDAL installieren, erhalten wir auch OGR, *OpenGIS Simple
   Features Reference Implementation*, eine Vektordaten-Übersetzungsbibliothek,
   mit der wir das Shapefile in Daten übersetzen können.

   #. GDAL kann un einfach mit dem Paketmanager installiert werden:

      .. code-block:: console

        $ sudo apt install gdal-bin

   #. Anschließend wechseln wir in den ``postgresql``-User:

      .. code-block:: console

        $ sudo -i -u postgres

   #. Nun konvertieren wir das Shapefile mit ``ogr2ogr`` und importieren es in
      unsere Datenbank:

      .. code-block:: console

        $ ogr2ogr -f PostgreSQL PG:dbname=postgis_db -progress \
            -nlt PROMOTE_TO_MULTI \
            /home/veit/nedata/ne_110m_admin_0_countries.shp

      ``-f PostgreSQL``
        gibt an, dass das Ziel eine PostgreSQL-Datenbank ist
      ``PG:dbname=postgis_db``
        gibt den PostgreSQL-Datenbanknamen an.
        Neben dem Namen können so auch weitere Optionen angegeben werden, allgemein:

        .. code-block::

            PG:"dbname='db_ename' host='addr' port='5432' user='x' password='y'"

      ``-progress``
        gibt einen Fortschrittsbalken aus
      ``-nlt PROMOTE_TO_MULTI``
        gibt an, dass alle Objekttypen als Multipolygone in die Datenbank
        geladen werden sollen
      ``/home/veit/nedata/ne_110m_admin_0_countries.shp``
        gibt den Pfad zur Eingabedatei an

      .. seealso::
         * `ogr2ogr <http://www.gdal.org/ogr2ogr.html>`_

   #. Überprüfen des Imports mit ``ogrinfo``

      .. code-block:: console

        $ ogrinfo -so PG:dbname=postgis_db ne_110m_admin_0_countries
        Output
        INFO: Open of `PG:dbname=postgis_db'
              using driver `PostgreSQL' successful.

        Layer name: ne_110m_admin_0_countries
        Geometry: Multi Polygon
        Feature Count: 177
        …

   #. Alternativ können wir uns auch einzelne Tabellen auflisten lassen:

      .. code-block:: console

        $ psql -d postgis_db
        postgis_db=# \dt
                           List of relations
         Schema |           Name            | Type  |  Owner
        --------+---------------------------+-------+----------
         public | ne_110m_admin_0_countries | table | postgres
         public | spatial_ref_sys           | table | postgres
        (2 rows)

   #. Schließlich können wir uns bei der Datenbank abmelden mit

      .. code-block:: console

        psql> \q

.. seealso::
   * `PostGIS Reference <http://postgis.net/docs/reference.html>`_

