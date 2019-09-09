Notebook
========

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    ../../first-steps/install
    ../../first-steps/create-notebook
    shortcuts
    config

Einführung
----------

Jupyter Notebooks erweitern den konsolenbasierten Ansatz für *interactive
Computing* um eine webbasierte Anwendung, mit der der gesamte Prozess erfasst
werden kann: vom Entwickeln zum Ausführen des Codes bis hin zum Dokumentieren
und Präsentieren der Ergebnisse. Dabei kombinieren Jupyter-Notebooks drei
verschiedene Komponenten:

Interactive Computing Protocol:
    offenes Netzwerkprotokoll basierend auf JSON-Daten über `ZMQ
    <http://zeromq.org/>`_ und `WebSockets
    <https://de.wikipedia.org/wiki/WebSocket>`_. 
Motebook Document Format:
    offenes, auf JSON basierendes Dokumentenformat mit vollständigen
    Aufzeichnungen der Sitzungen des Benutzers und des enthalten Code.
Kernel:
    Prozesse, die interaktiven Code in einer bestimmten Programmiersprache
    ausführen und die Ausgabe an den Benutzer zurückgeben.

