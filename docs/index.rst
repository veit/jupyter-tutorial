================
Jupyter Tutorial
================

`Jupyter notebooks <https://jupyter-notebook.readthedocs.io/>`_ are growing in
popularity with data scientists and have become the de facto standard for
rapid prototyping and exploratory analysis. They inspire experiments and
innovations enormously and as well they make the entire research process faster
and more reliable. In addition, many additional components are created that
expand the original limits of their use and enable new uses.

.. graphviz::

    digraph decide_jupyter {
        graph [fontname = "Calibri", fontsize="10", penwidth="1px",
               overlap=false];
        node [fontname = "Calibri", fontsize="10", style="bold",
              penwidth="1px", fontcolor="#640FFB"; color="#640FFB";];
        edge [fontname = "Calibri", fontsize="10", style="bold",
              penwidth="1px", fontcolor="#640FFB"; color="#640FFB";];
        tooltip="How do I decide which Jupyter packages I need?";
        // Top Level
        what [
            shape=diamond,
            label="What do you want to do?",
            tooltip="Jupyter offers you different ways how you can use the notebooks"]
        // Second Level
        singleuser [
             shape=plaintext,
             label=" ",
             tooltip="Single user"]
        hub [
            label="JupyterHub",
            tooltip="Install\nJupyterHub",
            target="_top",
            href="../hub/index.html"]
        nbconvert [
            label="nbconvert",
            tooltip="Install and\nuse nbconvert",
            target="_top",
            href="../nbconvert.html"]
        nbviewer [
            label="nbviewer",
            tooltip="Install and\nuse nbviewer",
            target="_top",
            href="../nbviewer.html"]
        kernels [
            label="Kernels",
            tooltip="Install, view and\nstart kernels",
            target="_top",
            href="../kernels/install.html"]
        extensions [
            shape=plaintext,
            label=" ",
            tooltip="Install notebook extensions"]
        embed [
            shape=plaintext,
            label="",
            tooltip="Embed notebooks in other applications"]
        examples [
            label="Enterprise\napplications",
            tooltip="Application examples at\nNetflix, Bloomberg etc.",
            target="_top",
            href="../use-cases.html"]
        // 3rd Level
        notebook [
             label="Jupyter-\nNotebook",
             tooltip="Install notebook locally",
             target="_top",
             href="../notebook/index.html"]
         jupyterlab [
             label="JupyterLab",
             tooltip="Install JupyterLab locally",
             target="_top",
             href="../jupyterlab/index.html"]
        widgets [
            label="Widgets",
            tooltip="Install and\nuse ipywidgets",
            target="_top",
            href="../ipywidgets/index.html"]
        extend [
            label="nbextensions",
            tooltip="Install and use various\nnotebook extensions",
            target="_top",
            href="../nbextensions/index.html"]
        viz [
            label="Visualise\ndata",
            tooltip="Data visualisation libraries",
            target="_top",
            href="../viz/index.html"]
        dash [
            label="Dashboards",
            tooltip="Install and\nuse Dashboards",
            target="_top",
            href="../dashboards/index.html"]
        html [
            label="in HTML",
            tooltip="Embed notebooks in\nstatic HTML",
            target="_top",
            href="../ipywidgets/embedding.html"]
        nbsphinx [
            label="nbsphinx",
            tooltip="Embed notebooks in the\nSphinx Document Generator",
            target="_top",
            href="../sphinx/nbsphinx.html"]
        executablebooks [
            label="Executable Books",
            tooltip="Bücher aus Jupyter Notebooks und MyST",
            target="_top",
            href="../sphinx/executablebooks.html"]
        // Edges
        what -> singleuser [label="Single\nuser"]
        what -> hub [label="Teamwork"]
        what -> nbconvert [label="Convert"]
        nbconvert -> nbviewer [label="Conversion\nservice"]
        what -> kernels [label="Java, R,\nJulia etc."]
        what -> extensions [label="Extend\nnotebooks"]
        what -> embed [label="Embed\nnotebooks"]
        what -> examples [label="Examples"]
        singleuser -> {notebook jupyterlab}
        extensions -> {widgets extend viz dash}
        embed -> {html nbsphinx executablebooks}
        // Arrangement
        rankdir="LR"
        {rank = same; what;}
        {rank = same; singleuser; hub; nbconvert; kernels; extensions; embed;
                examples;}
        {rank = same; widgets; extend; viz; dash;}
        {rank = same; html; sphinx}
    }

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    intro
    notebook/index
    jupyterlab/index
    hub/index
    nbconvert
    nbviewer
    kernels/index
    ipywidgets/index
    nbextensions/index
    viz/index
    dashboards/index
    sphinx/index
    use-cases
    genindex

.. Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
