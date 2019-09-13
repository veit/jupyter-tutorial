Einbetten von Jupyter-Widgets
=============================

Jupyter-Widgets können serialisiert und dann in andere Kontexte eingebettet
werden:

* statische Webseiten
* Sphinx-Dokumentation
* HTML-konvertierte Notebooks auf Nbviewer

Dabei erlaubt das npm-Paket ``@jupyter-widgets/html-manager`` das Einbetten auf
zwei unterschiedliche Weisen:

* das Einbetten der Standardelemente, die auf jeder Website verwendet werden
  können
* das Einbetten mit `RequireJS <https://requirejs.org/>`_ auch für
  benutzerdefinierte Widgets.

Einbetten von Widgets in HTML-Seiten
------------------------------------

Hierfür stellt das *Widgets*-Menü mehrere Optionen zur Verfügung:

*Save Notebook Widget State*
    Eine Notebook-Datei wird mit dem aktuellen Widget-Status als Metadaten
    gespeichert. Dadurch kann sie mit den Widgets im Browser gerendert werden.
*Clear Notebook Widget State*
    Die Metadaten des Widget-Status werden aus der Notebook-Datei gelöscht.
*Embed widgets*
    Der Menüpunkt bietet ein Dialogfeld mit einer HTML-Seite, auf der die
    aktuellen Widgets eingebettet sind. Um benutzerdefinierte Widgets zu
    unterstützen, wird der RequireJS-Embedder verwendet.

    .. note::
        Das erste Skript-Tag lädt RequireJS von einem CDN. RequireJS sollte
        jedoch auf der Site selbst zur Verfügung gestellt und dieser Skript-Tag
        gelöscht werden.

    .. note::
        Das zweite Skript-Tag lädt den RequireJS-Widget-Embedder. Dadurch werden
        geeignete Module definiert und anschließend eine Funktion zum Rendern
        aller auf der Seite enthaltenen Widget-Ansichten eingerichtet.

        Wenn ihr nur Standard-Widgets einbettet und RequireJS nicht verwendet,
        könnt ihr die ersten beiden Skript-Tags durch ein Skript-Tag ersetzen,
        das das Standard-Skript lädt.

*Download Widget State*
    Die Option lädt eine JSON-Datei herunter, die den serialisierten Status
    aller derzeit verwendeten Widget-Modelle im Format
    ``application/vnd.jupyter.widget-state+json`` enthält, das im npm-Paket
    ``@jupyter-widgets/schema`` spezifiziert ist.

Sphinx-Integration
------------------

Jupyter Sphinx
~~~~~~~~~~~~~~

`jupyter_sphinx <https://github.com/jupyter/jupyter-sphinx>`_ ermöglicht
jupyter-spezifische Funktionen in Sphinx. Es kann mit ``pip`` installiert
werden.

Konfiguration
:::::::::::::

Fügt in der ``conf.py``-Datei ``jupyter_sphinx.embed_widgets`` in der Liste der
Erweiterungen hinzu.

Anschließend könnt ihr in reStructuredText folgende Direktiven verwenden:

``ipywidgets-setup``
    ::

        from ipywidgets import VBox, jsdlink, IntSlider, Button

``ipywidgets-display``
    ::

        s1, s2 = IntSlider(max=200, value=100), IntSlider(value=40)
        b = Button(icon='legal')
        jsdlink((s1, 'value'), (s2, 'max'))
        VBox([s1, s2, b])


Beispiel
::::::::

::

    .. ipywidgets-setup::

        from ipywidgets import VBox, jsdlink, IntSlider, Button

    .. ipywidgets-display::
        :hide-code:

        s1, s2 = IntSlider(max=200, value=100), IntSlider(value=40)
        b = Button(icon='legal')
        jsdlink((s1, 'value'), (s2, 'max'))
        VBox([s1, s2, b])

Optionen
::::::::

Die Direktiven ``ipywidgets-setup`` und ``ipywidgets-display`` haben die
folgenden Optionen:

``ipywidgets-setup``
    mit der Option ``:show:`` um den Setup-Code als Code-Block darzustellen
``ipywidgets-display``
    mit den folgenden Optionen:

    ``:hide-code:``
        zeigt den Code nicht an sondern nur das Widget
    ``:code-below:``
        zeigt den Code nach dem Widget an
    ``:alt:``
        Alternativer Text, wenn das Widget nicht gerendert werden kann

.. seealso::
   `Options <https://github.com/jupyter-widgets/jupyter-sphinx#options>`_

