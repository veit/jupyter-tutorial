================
Jupyter Tutorial
================

Motivation
==========

`Jupyter-Notebooks <https://jupyter-notebook.readthedocs.io/>`_ erfreuen sich
bei Datenwissenschaftlern wachsender Beliebtheit und werden zum
De-facto-Standard für schnelles Prototyping und explorative Analysen. In diesem
Tutorial erläutere ich euch meine Motivationen und Gründe für Jupyter-Notebooks.
Sie beflügeln nicht nur Experimente und Innovationen enorm, sie machen auch den
gesamten Forschungsprozess schneller und zuverlässiger. Zudem entstehen viele
zusätzliche Komponenten, die die ursprünglichen Grenzen ihrer Nutzung erweitern
und neue Verwendungsmöglichkeiten ermöglichen.

Zielgruppe
==========

Die Nutzer von Jupyter-Notebooks sind vielfältig von Analysten über
Wissenschaftler bis hin zu Informatikern. Meist nehmen sie unterschiedliche
Rollen ein:

* *Data Scientists* führen beispielsweise Experimente mit verschiedenen
  Koeffizienten durch und fassen die Ergebnisse zusammen.
* *Data Engineers* überprüft die Qualität des Codes und macht ihn robuster,
  effizienter und skalierbar.
* *Data Analysts* führen systematische Untersuchungen der Daten durch, wobei
  sie den von *Data Engineers* bereitgestellten Code verwenden.
* *Software Engineers* erstellen das `Hub <https://jupyter.org/hub>`_, die
  Kernel, Erweiterungen etc. und gewährleisten den möglichst reibungslosen
  Betrieb dieser Infrastruktur.

In diesem Tutorial wenden wir uns zunächst vor allem an *Software Engineers*,
die eine Plattform auf Basis von Jupyter-Notebooks aufbauen und betreiben
wollen. In der Folge erläutern wir dann, wie diese Plattform effektiv von
*Data Scientists*, *Data Engineers* und *Data Analysts* genutzt werden kann.

Use Cases
=========

Wenn wir uns einen typischen Workflow genauer anschauen, können wir sehen, wie
die verschiedenen Aufgaben ineinandergreifen:

#. **Datenexploration** kann die tabellarische Ansicht von Beispieldaten,
   explorative Analysen und das Visualisieren von Daten umfassen.
#. **Datenaufbereitung** ist eine iterative Aufgabe, die das Bereinigen,
   Standardisieren, Transformieren, Denormalisieren und Aggregieren von
   Daten umfassen.
#. **Datenvalidierung** ist eine wiederkehrende Aufgabe, die die Ansicht von
   Beispieldaten, aggregierte Analysen sowie die Visualisierung von Daten
   umfasst. 
#. **Produktrealisierung** findet erst zu einem späten Zeitpunkt des
   Projekts statt und stellt z.B. Software-Pakete für die Produktion oder
   Schulungsmodelle bereit.

Warum Jupyter?
==============

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
:doc:`jupyter/kernels/index`
    Kernel sind Prozesse, die interaktiven Code in einer bestimmten
    Programmiersprache ausführen und die Ausgabe an den Benutzer zurückgeben.

Jupyter-Infrastruktur
=====================

Eine Plattform für die oben genannten Use Cases erfordert eine umfangreiche
Infrastruktur, die icht nur die Bereitstellung der Kernel sowie die
Parametrisierung, Zeitsteuerung und Parallelisierung von Notebooks erlaubt,
sondern darüberhinaus auch die gleichmäßige Bereitstellung der Ressourcen.

Es würde jedoch den Rahmen dieses Tutorials sprengen, wenn ich umfassend auf
unsere Datenplattform mit *Streaming Pipelines* und *Domain Driven Data Stores*
eingehen würde. Ich werde mich daher darauf beschränken, wie Nutzer in ihrem
Home-Verzeichnis Notebooks erstellen und ausführen können. Auf diese Datei kann
der Nutzer dann sowohl mit Jupyter Notebook wie auch mit dem Terminal zugreifen.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    first-steps/index
    ipython/index
    jupyter/index
    reproduce/index
    refactoring/index

.. Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`

