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
        singleuser [shape=plaintext,
            label="Notebook\nalleine nutzen",
            tooltip="Gehe zur Jupyter-Installationsanleitung"]
        team [
            shape=plaintext,
            label="Notebook im\nTeam nutzen",
            tooltip="Gehe zur JupyterHub-Installationsanleitung"]
        convert [
            shape=plaintext,
            label="Notebook\nkonvertieren",
            tooltip="Verwende nbconvert"]
        webconvert [
            shape=plaintext,
            label="Webservice für\nNotebook-Konvertierung",
            tooltip="Verwende nbviewer"]
        lang [
            shape=plaintext,
            label="Andere Programmier-\nsprache verwenden",
            tooltip="Installiere einen Jupyter-Kernel für R, Julia etc."]
        custom [
            shape=plaintext,
            label="Notebook\nanpassen",
            tooltip="Installiere Notebook-Erweiterungen"]
        // 3rd Level
        jupyter [
            label="Jupyter\ninstallieren",
            tooltip="Jupyter lokal installieren",
            target="_top",
            href="../first-steps/install.html"]
        hub [
            label="JupyterHub",
            tooltip="JupyterHub\ninstallieren",
            target="_top",
            href="../jupyter/jupyterhub"]
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
            label="Kernel\ninstallieren",
            tooltip="Kernel installieren, Anzeigen und Starten",
            target="_top",
            href="../jupyter/kernels/install.html"]
        // below kernel
        widgets [
            label="Widgets",
            tooltip="ipywidgets installieren und nutzen",
            target="_top",
            href="../jupyter/ipywidgets/"]
        extend [
            label="Extensions",
            tooltip="Installieren und Verwenden verschiedener Notebook-Erweiterungen",
            target="_blank",
            href="https://github.com/ipython-contrib/IPython-notebook-extensions"]
        dash [
            label="Dashboards",
            tooltip="Installieren und Verwenden von Dashboards",
            target="_blank",
            href="https://github.com/jupyter/dashboards"]
        // Edges
        what -> {singleuser team convert lang custom}
        singleuser -> jupyter
        team -> hub
        convert -> nbconvert
        nbconvert -> webconvert
        webconvert -> nbviewer
        lang -> kernel
        custom -> {widgets extend dash}
        // Arangement
        {rank = same; what;}
        {rank = same; singleuser; team; convert; lang; custom;}
        {rank = same; widgets; extend;}
        {rank = same; dash;}
    }

Inhalt
------

.. toctree::
    :maxdepth: 1

    use-cases
    ../first-steps/install
    ../first-steps/create-notebook
    config
    jupyterhub/index
    kernels/index
    nbconvert
    ipywidgets/index
    nbviewer

