Einführung
==========

Status
------

-|Contributors| |Commits| |License| |Docs|

.. |Contributors| image:: https://img.shields.io/github/contributors/veit/jupyter-tutorial.svg
   :target: https://github.com/veit/jupyter-tutorial/graphs/contributors
.. |Commits| image::  https://raster.shields.io/github/commit-activity/y/veit/jupyter-tutorial
   :target: https://github.com/veit/jupyter-tutorial/commits
.. |License| image:: https://img.shields.io/github/license/veit/jupyter-tutorial.svg
   :target: https://github.com/veit/jupyter-tutorial/blob/master/LICENSE
.. |Docs| image:: https://readthedocs.org/projects/jupyter-tutorial/badge/?version=latest
   :target: https://jupyter-tutorial.readthedocs.io/de/latest/

Zielgruppe
----------

Die Nutzer von Jupyter-Notebooks sind vielfältig von Daten-Wissenschaftlern über
-Ingenieure und -Analysten bis hin zu System-Ingenieuren. Dabei sind ihre
Fähigkeiten und Arbeitsabläufe sehr unterschiedlich. Eine der großen Stärken von
Jupyter-Notebooks ist jedoch, dass sie eine enge Zusammenarbeit dieser
unterschiedlichen Experten in funktionsübergreifenden Teams ermöglichen.

* **Daten-Wissenschaftler** führen Experimente mit verschiedenen Koeffizienten
  durch und fassen die Ergebnisse zusammen.
* **Daten-Ingenieure** überprüfen die Qualität des Codes und machen ihn robuster,
  effizienter und skalierbar.
* **Daten-Analysten** führen systematische Untersuchungen der Daten durch, wobei
  sie den von Dateningenieuren bereitgestellten Code verwenden.
* **System-Ingenieure** erstellen das `Hub <https://jupyter.org/hub>`_, die
  Kernel, Erweiterungen etc. und gewährleisten den möglichst reibungslosen
  Betrieb dieser Infrastruktur.

In diesem Tutorial wenden wir uns zunächst vor allem an System-Ingenieure,
die eine Plattform auf Basis von Jupyter-Notebooks aufbauen und betreiben
wollen. In der Folge erläutern wir dann, wie diese Plattform effektiv von
Datenwissenschaftlern, -Ingenieuren und -Analysten genutzt werden kann.

Aufbau des Jupyter-Tutorial
---------------------------

Das Jupyter-Tutorial folgt ab Kapitel 3 dem prototypischen Verlauf eines
Forschungsprojekts:

3. **Arbeitsbereich einrichten** mit der Installation und Konfiguration von
   :doc:`workspace/ipython/index`, :doc:`workspace/jupyter/index` mit
   :doc:`workspace/jupyter/nbextensions/index` und
   :doc:`workspace/jupyter/ipywidgets/index`.
4. **Daten sammeln**, entweder durch eine :doc:`Rest-API <gather/web-api>` oder
   direkt von einer :doc:`HTML-Seite <gather/html>`.
5. **Daten bereinigen** ist eine wiederkehrende Aufgabe, die u.a. redundante,
   inkonsistente oder falsch formatierte Daten entfernen oder modifizieren soll.
6. **Erschließen der Daten –** :doc:`viz/index` umfasst expolorative Analysen und
   das Visualisieren von Daten.
7. **Refactoring** umfasst das Parametrisieren, Validieren und
   Performance-Optimierungen, u.a. durch :doc:`Refactoring
   <refactoring/parallel/index>`.
8. **Produkt erstellen** umfasst das :doc:`productive/testing/index`,
   :doc:`productive/logging` und :doc:`productive/sphinx/index` der
   Methoden und Funktionen sowie das :doc:`Erstellen von Paketen
   <productive/packaging/index>`.
9. **Web-Anwendungen** können entweder aus Jupyter-Notebooks
   :doc:`web/dashboards/index` generieren oder umfassendere Applikationslogik
   benötigen, wie z.B. in :doc:`/viz/bokeh/embedding-export/flask` demonstriert,
   oder Daten über eine `RESTful API
   <https://de.wikipedia.org/wiki/Representational_State_Transfer>`_
   bereitstellen.

Warum Jupyter?
--------------

Wie können nun diese vielfältigen Aufgaben vereinfacht werden? Es wird sich
kaum ein Werkzeug finden, das all diese Aufgaben abdeckt und selbst für einzelne
Aufgaben sind häufig mehrere Werkzeuge notwendig. Daher suchen wir auf einer
abstrakteren Ebene allgemeinere Muster für Tools und Sprachen, mit denen Daten
analysiert und visualisiert sowie ein Projekt dokumentiert und präsentiert
werden kann. Genau dies wir mit dem `Project Jupyter <https://jupyter.org/>`_
angestrebt.

Das Projekt Jupyter startete 2014 mit dem Ziel, ein konsistentes Set von
Open-Source-Tools für wissenschaftliche Forschung, reproduzierbare Workflows,
`Computational Narratives
<https://blog.jupyter.org/project-jupyter-computational-narratives-as-the-engine-of-collaborative-data-science-2b5fb94c3c58>`_
und Datenanalyse zu erstellen. Bereits 2017 wurde Jupyter dann mit dem `ACM
Software Systems Award
<https://blog.jupyter.org/jupyter-receives-the-acm-software-system-award-d433b0dfe3a2>`_
ausgezeichnet - eine prestigeträchtige Auszeichnung, die es u.a. mit Unix und
dem Web teilt.

Um zu verstehen, warum Jupyter-Notebooks so erfolgreich sind, schauen wir uns
die Kernfunktionen einmal genauer an:

`Jupyter Notebook Format <https://nbformat.readthedocs.io/>`_
    Jupyter Notebooks sind ein offenes, auf JSON basierendes Dokumentenformat
    mit vollständigen Aufzeichnungen der Sitzungen des Benutzers und des
    enthalten Code.
Interactive Computing Protocol
    Das Notebook kommuniziert mit Rechenkernel über das *Interactive Computing
    Protocol*, einem offenen Netzwerkprotokoll basierend auf JSON-Daten über
    `ZMQ <http://zeromq.org/>`_ und `WebSockets
    <https://de.wikipedia.org/wiki/WebSocket>`_.
:doc:`workspace/jupyter/kernels/index`
    Kernel sind Prozesse, die interaktiven Code in einer bestimmten
    Programmiersprache ausführen und die Ausgabe an den Benutzer zurückgeben.

Jupyter-Infrastruktur
---------------------

Eine Plattform für die oben genannten Use Cases erfordert eine umfangreiche
Infrastruktur, die nicht nur die Bereitstellung der Kernel sowie die
Parametrisierung, Zeitsteuerung und Parallelisierung von Notebooks erlaubt,
sondern darüberhinaus auch die gleichmäßige Bereitstellung der Ressourcen.

Es würde jedoch den Rahmen dieses Tutorials sprengen, wenn ich umfassend auf
unsere Datenplattform mit *Streaming Pipelines* und *Domain Driven Data Stores*
eingehen würde. Ich werde mich daher darauf beschränken, wie Nutzer in ihrem
Home-Verzeichnis Notebooks erstellen und ausführen können. Auf diese Datei kann
der Nutzer dann sowohl mit Jupyter Notebook wie auch mit dem Terminal zugreifen.

