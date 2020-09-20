Daten lesen und schreiben
=========================

Einen Überblick über öffentliche Repositories mit Forschungsdaten erhaltet ihr
z.B. in der `Registry of research data repositories (re3data)
<https://www.re3data.org/>`_.

Neben spezifischen Python-Bibliotheken zum Zugriff auf :ref:`entfernte
Speichermedien </data-rw/overview.rst#entfernte-speichermedien>` und
:ref:`/data-rw/overview.rst#geodaten` stellen wir Euch vier Werkzeuge genauer vor:

* :doc:`requests/index`
* :doc:`beautifulsoup`
* :doc:`intake/index`
* :doc:`DVC <../productive/dvc/index>`

.. seealso::
    `Scrapy <https://scrapy.org/>`_
        Framework zum Extrahieren von Daten aus Websites als JSON-, CSV- oder
        XML-Dateien.
    `Pattern <https://github.com/clips/pattern>`_
        Python-Modul zum Data Mining, Verarbeitung natürlicher Sprache, ML und
        Netzwerkanalyse

Zum Speichern von relationalen Daten, Python-Objekten und Geodaten stellen wir
Euch :doc:`postgresql/index`, :doc:`postgresql/sqlalchemy` und
:doc:`postgresql/postgis/index` vor.

Zum Bereinigen und Vorbereiten der Daten stellen wir Euch einige Best Practices
und hilfreiche Python-Pakete in :doc:`../clean-prep/index` vor.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    requests/index
    beautifulsoup
    intake/index
    postgresql/index
    nosql/index
    glossary
