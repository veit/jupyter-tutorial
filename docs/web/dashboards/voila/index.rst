Voilà
=====

`Voilà <https://github.com/voila-dashboards/voila>`_ wurde von `QuantStack
<http://quantstack.net/>`_ entwickelt.

Features
--------

* Voilà unterstützt :doc:`interaktive Jupyter-Widgets
  </workspace/jupyter/ipywidgets/index>`, einschließlich der Roundtrips zum
  Kernel. Auch benutzerdefinierte Widgets wie
  :doc:`/viz/d3js/bqplot/index`,
  :doc:`/viz/js/ipyleaflet`, 
  :doc:`/viz/js/ipyvolume`, 
  `ipympl <https://github.com/matplotlib/jupyter-matplotlib/>`_, 
  :doc:`ipysheet </workspace/jupyter/ipywidgets/libs/ipysheet>`, 
  `plotly <https://github.com/plotly/plotly.py>`_, 
  `ipywebrtc <https://github.com/maartenbreddels/ipywebrtc>`_ usw. werden
  unterstützt.
* Voilà erlaubt keine willkürliche Ausführung von Code durch Nutzer von
  Dashboards.
* Voilà basiert auf Jupyter-Standardprotokollen und -Dateiformaten und
  funktioniert mit jedem
  :doc:`Jupyter-Kernel </workspace/jupyter/kernels/index>`: C++, Python, Julia.
  Dies macht es zu einem sprachunabhängigen Dashboard-System.
* Voilà ist erweiterbar. Es enthält ein flexibles :doc:`Template
  <templating>`-System zur Erstellung
  umfangreicher Layouts.

Ausführungsmodell
-----------------

.. graphviz::

    digraph  execution_model {
        graph [fontname = "Calibri", fontsize="12"];
        node [fontname = "Calibri", fontsize="12"];
        edge [fontname = "Consolas", fontsize="12"];
        tooltip="Ausführungsmodell";
        subgraph cluster_browser {
            notebook_url [
                shape=box,
                label="Notebook URL";
                style=filled;
                fillcolor="#edf8fb";
                color="#b2e2e2"];
            html_rendering [
                shape=box,
                label="HTML-Rendering";
                style=filled;
                fillcolor="#edf8fb";
                color="#b2e2e2"];
            init_websocket [
                shape=box,
                label="Javascript initiiert Websocket\nmit dem Jupyter-Kernel",
                style=filled;
                fillcolor="#edf8fb";
                color="#b2e2e2"];
            label="Browser";
            labeljust="l";
        }
        subgraph cluster_server {
            html_open_notebook [
                shape=box,
                label="Notebook öffnen und\nzugehörigen Kernel starten";
                style=filled;
                fillcolor="#bdd7e7";
                color="#2171b5"];
            html_run_notebook [
                shape=box,
                label="Notebook-Zellen ausführen\nErgebnisse ausgeben\nVoilà-Template zuweisen\nNotebook konvertieren";
                style=filled;
                fillcolor="#bdd7e7";
                color="#2171b5"];
            ws_open_notebook [
                shape=box,
                label="Notebook öffnen und\nzugehörigen Kernel starten";
                style=filled;
                fillcolor="#bdd7e7";
                color="#2171b5"];
            label="Server";
            labeljust="l";
        }
        // Edges
        notebook_url -> html_open_notebook [label="GET Request"]
        html_open_notebook -> html_run_notebook
        html_run_notebook -> html_rendering [label="HTTP Responses\lmit HTML oder\lHTML-Fragmenten\l"]
        html_rendering -> init_websocket
        init_websocket -> ws_open_notebook [dir=both label="Web-Socket:\l- comm_msg\l- comm_info_request\l- kernel_info_request\l- shutdown_request\l"]
        // Arrangement
        {rank = same; notebook_url; html_rendering; init_websocket;}
        {rank = same; html_open_notebook; html_run_notebook; ws_open_notebook;}
    }

Ein wichtiger Aspekt dieses Ausführungsmodells ist, dass vom Frontend nicht
angegeben werden kann, welcher Code vom Backend ausgeführt wird. Sofern mit der
Option ``--strip-sources=False`` nicht anders angegeben, gelangt der Quellcode
des gerenderten Notizbuchs noch nicht einmal an das Frontend. Die Voilà-Instanz
des ``jupyter_server`` erlaubt standardmäßig keine Ausführungsanforderungen.

.. warning::
    Die aktuelle Version von Voilà antwortet auf den ersten ``GET``-Request
    erst, wenn alle Zellen ausgeführt wurden. Dies kann länger dauern. Es wird
    jedoch daran gearbeitet, progressives Rendern zu ermöglichen, s. `feat:
    progressive cell rendering
    <https://github.com/maartenbreddels/voila/commit/cfd0204231313ebe5dd110c488a5cc6254c85a65>`_.

.. seealso::

    * `Voilà Gallery <https://voila-gallery.org/>`_
    * `And voilà! <https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    install
    templating
    bqplot_vuetify_example.ipynb
    debug.ipynb

