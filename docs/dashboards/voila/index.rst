Voilà
=====

`Voilà <https://github.com/voila-dashboards/voila>`_ was developed by
`QuantStack <https://quantstack.net>`_.

Features
--------

* Voilà supports :doc:`interactive Jupyter widgets </ipywidgets/index>`,
  including round trips to the kernel.
  Custom widgets like :doc:`pyviz:d3js/bqplot/index`,
  :doc:`pyviz:js/ipyleaflet`,
  :doc:`pyviz:js/ipyvolume`,
  `ipympl <https://github.com/matplotlib/ipympl>`_,
  :doc:`ipysheet </ipywidgets/libs/ipysheet>`,
  `plotly <https://github.com/plotly/plotly.py>`_,
  `ipywebrtc <https://github.com/maartenbreddels/ipywebrtc>`_ etc. are also
  supported.
* Voilà does not allow arbitrary code execution by dashboard users.
* Voilà is based on Jupyter standard protocols and file formats and works with
  any :doc:`Jupyter-Kernel </kernels/index>`: C++, Python, Julia. This makes it
  a language-independent dashboard system.
* Voilà is expandable. It contains a flexible  :doc:`Template <templating>`
  system for creating extensive layouts.

Execution model
---------------

.. graphviz::

    digraph  execution_model {
        graph [fontname = "Calibri", fontsize="12"];
        node [fontname = "Calibri", fontsize="12"];
        edge [fontname = "Consolas", fontsize="12"];
        tooltip="Ausführungsmodell";
        subgraph cluster_browser {
            notebook_url [
                shape=box,
                label="Notebook url";
                style=filled;
                fillcolor="#edf8fb";
                color="#b2e2e2"];
            html_rendering [
                shape=box,
                label="HTML rendering";
                style=filled;
                fillcolor="#edf8fb";
                color="#b2e2e2"];
            init_websocket [
                shape=box,
                label="Javascript initiates Websocket\nwith the Jupyter kernel",
                style=filled;
                fillcolor="#edf8fb";
                color="#b2e2e2"];
            label="Browser";
            labeljust="l";
        }
        subgraph cluster_server {
            html_open_notebook [
                shape=box,
                label="Open the notebook and start\nthe associated kernel";
                style=filled;
                fillcolor="#bdd7e7";
                color="#2171b5"];
            html_run_notebook [
                shape=box,
                label="Run notebook cells\nOutput results\nAssign Voilà template\nConvert notebook";
                style=filled;
                fillcolor="#bdd7e7";
                color="#2171b5"];
            ws_open_notebook [
                shape=box,
                label="Open the notebook and\nstart the associated kernel";
                style=filled;
                fillcolor="#bdd7e7";
                color="#2171b5"];
            label="Server";
            labeljust="l";
        }
        // Edges
        notebook_url -> html_open_notebook [label="GET Request"]
        html_open_notebook -> html_run_notebook
        html_run_notebook -> html_rendering [label="HTTP Responses\lwith HTML or\lHTML fragments\l"]
        html_rendering -> init_websocket
        init_websocket -> ws_open_notebook [dir=both label="Web-Socket:\l- comm_msg\l- comm_info_request\l- kernel_info_request\l- shutdown_request\l"]
        // Arrangement
        {rank = same; notebook_url; html_rendering; init_websocket;}
        {rank = same; html_open_notebook; html_run_notebook; ws_open_notebook;}
    }

An important aspect of this execution model is that the frontend cannot specify
which code is executed by the backend. Unless otherwise specified with the option
``--strip-sources=False``, the source code of the rendered notebook does not
even reach the frontend. The Voilà instance of ``jupyter_server`` does not allow
execution requests by default.

.. warning::
    The current version of Voilà does not respond to the first ``GET`` request
    until all cells have been executed. This can take longer. However, work is
    being done to enable progressive rendering, see `feat: progressive cell
    rendering
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
