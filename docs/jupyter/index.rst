Jupyter
=======

Was wollt ihr machen?
---------------------

.. graphviz::

    digraph decide_jupyter {
        graph [fontname = "Calibri", fontsize="16"];
        node [fontname = "Calibri", fontsize="16"];
        edge [fontname = "Calibri", fontsize="16"];
        tooltip="Wie entscheide ich, welche Jupyter-Pakete ich benötige?";
        // Top Level
        what [
            shape=diamond,
            label="Was wollt ihr machen?",
            tooltip="Jupyter bietet euch verschiedene Möglichkeiten, wie ihr die Notebooks nutzen könnt"]
        //  style=filled, color="green"]
        // Second Level
        jupyter [
            label="Jupyter",
            tooltip="Jupyter lokal installieren",
            target="_top",
            href="../first-steps/install.html"]
        hub [
            label="JupyterHub",
            tooltip="JupyterHub\ninstallieren",
            target="_top",
            href="../jupyter/jupyterhub/index.html"]
        nbconvert [
            label="nbconvert",
            tooltip="nbconvert installieren und nutzen",
            target="_top",
            href="../jupyter/nbconvert.html"]
        nbviewer [
            label="nbviewer",
            tooltip="nbviewer installieren und nutzen",
            target="_top",
            href="../jupyter/nbviewer.html"]
        kernel [
            label="Kernel",
            tooltip="Kernel installieren, anzeigen und starten",
            target="_top",
            href="../jupyter/kernels/install.html"]
        custom [
            shape=plaintext,
            label=" ",
            tooltip="Notebook-Erweiterungen installieren"]
        // 3rd Level
        widgets [
            label="Widgets",
            tooltip="ipywidgets installieren und nutzen",
            target="_top",
            href="../jupyter/ipywidgets/"]
        extend [
            label="nbextensions",
            tooltip="Installieren und Verwenden verschiedener Notebook-Erweiterungen",
            target="_top",
            href="../jupyter/nbextensions/index.html"]
        dash [
            label="Dashboards",
            tooltip="Installieren und Verwenden von Dashboards",
            target="_top",
            href="../jupyter/dashboards/index.html"]
        // Edges
        what -> jupyter [label="Einzel-\nnutzer"]
        what -> hub [label="Team-\narbeit"]
        what -> nbconvert [label="Konvertieren"]
        nbconvert -> nbviewer [label="Konvertier-\nservice"]
        what -> kernel [label="Java, R,\nJulia etc."]
        what -> custom [label="Notebook\nerweitern"]
        custom -> {widgets extend dash}
        // Arangement
        {rank = same; what;}
        {rank = same; jupyter; hub; nbconvert; kernel; custom;}
        {rank = same; widgets; extend; dash;}
    }

.. toctree::
    :maxdepth: 1
    :caption: Inhalt

    use-cases
    ../first-steps/install
    ../first-steps/create-notebook
    shortcuts
    config
    jupyterhub/index
    kernels/index
    nbconvert
    ipywidgets/index
    nbextensions/index
    nbviewer

