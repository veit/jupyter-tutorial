Liste der Erweiterungen
=======================

Ihr könnt die Notebook-Erweiterungen aktivieren und konfigurieren, indem ihr auf
den Reiter :menuselection:`Nbextensions` klickt. Dort habt ihr Zugriff auf die
Erweiterungen, die über Kontrollkästchen aktiviert/deaktiviert werden können.
Zusätzlich werden für jede Erweiterung eine Dokumentation und
Konfigurationsoptionen angezeigt.

.. image:: configure-nbextensions.png
   :alt: Konfiguration der Notebook-Erweiterungen

Im Folgenden gebe ich einen kurzen Überblick über einige der
Notebook-Erweiterungen. 

(some) LaTeX environments for Jupyter notebook
    ermöglicht die Verwendung von Markdown-Zellen für LaTeX-Befehle und
    -Umgebungen. Zudem werden zwei Menüs hinzugefügt:
    :menuselection:`LaTeX_envs` für die schnelle Auswahl der passenden
    LaTeX-Umgebung und  :menuselection:`Some configuration options` weiteren
    Optionen:

    .. image:: latex-env.png
       :alt: LaTeX-Umgebung

    Das Notebook kann anschließend als HTML oder LaTeX-Dokument exportiert
    werden. 

    Die Konfiguration der LaTeX-Umgebungen erfolgt in ``user_envs.json`` und für
    die Stile in ``latex_env.css``. Weitere Umgebungen können in
    ``user_envs.json`` oder in ``thmsInNb4.js`` hinzugefügt werden
    (→ `LaTeX-Environments doc
    <https://rawgit.com/jfbercher/jupyter_latex_envs/master/src/latex_envs/static/doc/documentation.pdf>`_).

:doc:`nbextensions/code_prettify/README_autopep8`
    formatiert/verschönert Code in Python-Code-Zellen. Die Erweiterung verwendet
    `autopep8 <https://github.com/hhatto/autopep8>`_ und ist daher nur mit
    Python-Kernel zu verwenden.

:doc:`nbextensions/code_prettify/README_code_prettify`
    formatiert/verschönert Code in Notebook-Code-Zellen. Dabei wird der aktuelle
    Notebook-Kernel verwendet, weswegen das verwendete Prettifier-Paket in
    diesem Kernel verfügbar sein muss. Beispielimplementierungen werden für
    ipython-, R- und Javascript-Kernel bereitgestellt.

:doc:`nbextensions/limit_output/readme`
    begrenzt die Anzahl der Zeichen, die eine Codezelle als Text oder HTML
    ausgibt. Dies unterbricht auch Endlosschleifen. Ihr könnt die Anzahl der
    Zeichen mit dem ``ConfigManager`` festlegen:

    .. code-block::

        from notebook.services.config import ConfigManager
        cm = ConfigManager().update('notebook', {'limit_output': 1000})

`Nbextensions edit menu item <https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator>`_
    fügt ein Bearbeitungsmenü hinzu, um die Konfigurationsseite für
    ``nbextensions`` zu öffnen.

:doc:`nbextensions/printview/readme`
    fügt eine Symbol hinzu, um die Druckansicht des aktuellen Notizbuchs in einem
    neuen Browser-Reiter anzuzeigen.

:doc:`nbextensions/ruler/readme`
    fügt ein Lineal nach einer bestimmten Anzahl von Zeichen hinzu. Die Anzahl
    der Zeichen lässt sich mit dem  ``ConfigManager`` festlegen:

    .. code-block::

        from notebook.services.config import ConfigManager
        ip = get_ipython()
        cm = ConfigManager(parent=ip)
        cm.update('notebook', {"ruler_column": [80]})

:doc:`nbextensions/scratchpad/README`
    fügt dem Notizbuch eine Notizzelle hinzu. In dieser Zelle könnt ihr Code
    des aktuellen Kernel ausführen, ohne das Dokument zu ändern.

:doc:`nbextensions/snippets/README`
    fügt Notebooks ein konfigurierbares Menüelement hinzu um Snippets,
    Boilerplate und Codebeispiele einzufügen.

    .. image:: snippets-menu.png
       :alt: Snippets-Menü

    Ihr könnt auch eigene Menüeinträge definieren, s.
    :doc:`nbextensions/snippets/README`.

:doc:`nbextensions/toc2/README`
    ermöglicht es, alle Überschriften zu sammeln und in einem schwebenden
    Fenster, als Sidebar oder in einem Navigationsmenü anzuzeigen.

    Falls Überschriften nicht im Inhaltsverzeichnis angezeigt werden sollen,
    geht dies mit:

    .. code-block:: HTML

        ## My title <a class="tocSkip">

    Das Inhaltsverzeichnis lässt sich auch exportieren indem ein entsprechendes
    Template angegeben wird, also z.B.

    .. code-block:: console

        $ jupyter nbconvert mynotebook.ipynb --template toc2

    Eine allgemeine Dokumentation zu Vorlagen findet ihr in
    :label:`nbconvert:external_exporters`.

:doc:`nbextensions/tree-filter/readme`
    filtert im Jupyter-Dashboard nach Dateinamen.

:doc:`nbextensions/code_prettify/README_2to3`
    konvertiert in einer Code-Zelle Python2- in Python3-Code unter Verwendung der
    `lib2to3 <https://github.com/python/cpython/tree/3.7/Lib/lib2to3/>`_-Bibliothek

:doc:`nbextensions/codefolding/readme`
    ermöglicht Codefolding in Code-Zellen.

    .. image:: code-folding.png
       :alt: Codefolding
 
    Üblicherweise wird das Codefolding beim Export mit :doc:`../nbconvert`
    beibehalten. Dies kann entweder in ``jupyter_nbconvert_config.py`` geändert
    werden mit:

    .. code-block:: python

        c.CodeFoldingPreprocessor.remove_folded_code=True = True

    oder auf der Kommandozeile mit

    .. code-block:: console

        $ jupyter nbconvert --to html --CodeFoldingPreprocessor.remove_folded_code=True mynotebook.ipynb

:doc:`nbextensions/collapsible_headings/readme`
    ermöglicht Notebooks, zusammenklappbare Abschnitte zu haben, die durch
    Überschriften getrennt werden.

:doc:`nbextensions/datestamper/readme`
    fügt die aktuelle Zeit und das aktuelle Datum in eine Zelle ein.

:doc:`nbextensions/hinterland/README`
    ermöglicht Autovervollständigung.

:doc:`nbextensions/varInspector/README`
    sammelt alle definierten Variablen und zeigt sie in einem schwebenden
    Fenster an.

:doc:`nbextensions/load_tex_macros/readme`
    lädt automatisch eine Reihe von Latex-Befehlen aus der Datei
    ``latexdefs.tex`` wenn ein Notizbuch geöffnet wird.

