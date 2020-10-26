Jupyter
=======

.. graphviz::

    digraph decide_jupyter {
        graph [fontname = "Calibri", fontsize="16"];
        node [fontname = "Calibri", fontsize="16"];
        edge [fontname = "Calibri", fontsize="16"];
        tooltip="How do I decide which Jupyter packages I need?";
        // Top Level
        what [
            shape=diamond,
            label="What do you want to do?",
            tooltip="Jupyter offers you different ways how you can use the notebooks"]
        // Second Level
        jupyter [
            label="Jupyter",
            tooltip="Install Jupyter locally",
            target="_top",
            href="../workspace/jupyter/notebook/index.html"]
        hub [
            label="JupyterHub",
            tooltip="Install\nJupyterHub",
            target="_top",
            href="../workspace/jupyter/hub/index.html"]
        nbconvert [
            label="nbconvert",
            tooltip="Install and\nuse nbconvert",
            target="_top",
            href="../workspace/jupyter/nbconvert.html"]
        nbviewer [
            label="nbviewer",
            tooltip="Install and\nuse nbviewer",
            target="_top",
            href="../workspace/jupyter/nbviewer.html"]
        kernels [
            label="Kernels",
            tooltip="Install, view and\nstart kernels",
            target="_top",
            href="../workspace/jupyter/kernels/install.html"]
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
            href="../workspace/jupyter/use-cases.html"]
        // 3rd Level
        widgets [
            label="Widgets",
            tooltip="Install and\nuse ipywidgets",
            target="_top",
            href="../workspace/jupyter/ipywidgets/index.html"]
        extend [
            label="nbextensions",
            tooltip="Install and use various\nnotebook extensions",
            target="_top",
            href="../workspace/jupyter/nbextensions/index.html"]
        viz [
            label="Visualisation",
            tooltip="Data visualisation libraries",
            target="_top",
            href="../viz/index.html"]
        dash [
            label="Dashboards",
            tooltip="Install and\nuse Dashboards",
            target="_top",
            href="../web/dashboards/index.html"]
        html [
            label="HTML",
            tooltip="Embed notebooks in\nstatic HTML",
            target="_top",
            href="../workspace/jupyter/ipywidgets/embedding.html"]
        sphinx [
            label="Sphinx",
            tooltip="Embed notebooks in the\nSphinx Document Generator",
            target="_top",
            href="../workspace/jupyter/nbsphinx.html"]
        // Edges
        what -> jupyter [label="Single\nuser"]
        what -> hub [label="Teamwork"]
        what -> nbconvert [label="Convert"]
        nbconvert -> nbviewer [label="Conversion\nservice"]
        what -> kernels [label="Java, R,\nJulia etc."]
        what -> extensions [label="Extend\nNotebook"]
        what -> embed [label="Embed\nNotebooks"]
        what -> examples [label="Examples"]
        extensions -> {widgets extend viz dash}
        embed -> {html sphinx} [label="Embed"]
        // Arrangement
        {rank = same; what;}
        {rank = same; jupyter; hub; nbconvert; kernels; extensions; embed; examples;}
        {rank = same; widgets; extend; viz; dash;}
        {rank = same; html; sphinx}
    }

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    notebook/index
    hub/index
    nbconvert
    nbviewer
    kernels/index
    ipywidgets/index
    nbextensions/index
    nbsphinx
    use-cases
